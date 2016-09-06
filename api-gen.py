#!/usr/bin/python
# -*- coding: utf-8; -*-

import copy
from datetime import datetime
import sys
import os, os.path
import json

generic_api = {
	'api': '0.4.14',
	'name': 'Freifunk Vogtland',

	'contact': {
		'email': 'kontakt@freifunk-vogtland.net',
		'facebook': 'https://www.facebook.com/vogtland.freifunk.net',
		'ml': 'info@freifunk-vogtland.net',
		'twitter': '@FreifunkV',
	},
	'feeds': [
		{
			'category': 'blog',
			'name': 'Freifunk Vogtland Blog',
			'type': 'rss',
			'url': 'http://vogtland.freifunk.net/?feed=rss2',
		},
	],
	'nodeMaps': [
		{
			'interval': '1min',
			'mapType': 'geographical',
			'technicalType': 'meshviewer',
			'url': 'http://vogtland.freifunk.net/map/',
		},
	],
	'state': {
		'focus': [
			'infrastructure/backbone',
			'Public Free Wifi',
			'Social Community Building',
			'Free internet access',
		],
		'lastchange': '1970-01-01T01:00:00Z',
		'nodes': 0
	},
	'techDetails': {
		'firmware': {
				'docs': 'https://github.com/FreifunkVogtland/site-ffv',
				'name': 'Gluon',
				'url': 'http://firmware.freifunk-vogtland.net/',
				'vpnaccess': 'automatic',
		},
		'legals': [
			'vpnnational',
			'vpninternational',
		],
		'networks': {
			'ipv4': [
				{
					'network': '10.149.0.0/16',
				},
			],
			'ipv6': [
				{
					'network': '2001:bc8:3f13:ffc2::/64',
				},
			],
		},
		'routing': [
			'batman-adv',
		],
		'updatemode': [
			'autoupdate',
		],
	},
	'url': 'http://freifunk-vogtland.net/',

	# TODO
	# "support":{  
	# 	"donations":{  
	# 		"bankaccount":{  
	# 			"IBAN":"",
	# 			"BIC":"",
	# 		},
	# 		"campaigns":[  
	# 			{  
	# 				"provider":"betterplace",
	# 				"projectid":"",
	# 			},
	# 			{  
	# 				"provider":"boost",
	# 				"projectid":"",
	# 			},
	# 		],
	# 	},
	# },
}

cities = {
	"A" : {
		'location': {
			'city': 'Adorf',
			'country': 'DE',
			'lat': 50.316667,
			'lon': 12.266667,
		},
	},
	"AE" : {
		'location': {
			'city': 'Auerbach',
			'country': 'DE',
			'lat': 50.509444,
			'lon': 12.4,
		},
	},
	"BE" : {
		'location': {
			'city': 'Bad Elster',
			'country': 'DE',
			'lat': 50.281944,
			'lon': 12.234722,
		},
	},
	"FST" : {
		'location': {
			'city': 'Falkenstein',
			'country': 'DE',
			'lat': 50.466667,
			'lon': 12.366667,
		},
	},
	"MKN" : {
		'location': {
			'city': 'Markneukirchen',
			'country': 'DE',
			'lat': 50.316667,
			'lon': 12.316667,
		},
	},
	"OEL" : {
		'location': {
			'city': 'Oelsnitz',
			'country': 'DE',
			'lat': 50.416667,
			'lon': 12.166667,
		},
	},
	"PL" : {
		'location': {
			'city': 'Plauen',
			'country': 'DE',
			'lat': 50.483333,
			'lon': 12.116667,
		},
	},
	"RDW" : {
		'location': {
			'city': 'Rodewisch',
			'country': 'DE',
			'lat': 50.516667,
			'lon': 12.416667,
		},
	},
	"TR" : {
		'location': {
			'city': 'Treuen',
			'country': 'DE',
			'lat': 50.5425,
			'lon': 12.302222,
		},
	},
}

def dump_json(data, filename):
	with open(filename, 'w') as f:
		json.dump(data, f)
		f.flush()
		os.fsync(f.fileno())

def count_nodes(nodes, prefix):
	nodes_ffv = filter(lambda n: n['nodeinfo']['hostname'].startswith(prefix + '-'), nodes['nodes'])

	return len(nodes_ffv)

def generate_city_data(nodes, prefix):
	apidata = copy.deepcopy(generic_api)

	for replacekey in cities[prefix]:
		apidata[replacekey] = cities[prefix][replacekey]

	apidata['state']['lastchange'] = datetime.utcnow().isoformat() + 'Z'
	apidata['state']['nodes'] = count_nodes(nodes, prefix)

	return apidata

def main():
	if len(sys.argv) != 3:
		print("./api-gen.py NODESJSON OUTPATH")
		sys.exit(1)

	nodesjson = sys.argv[1]
	outpath = sys.argv[2]

	# load
	nodes = json.load(open(nodesjson))

	# store
	for prefix in cities:
		data = generate_city_data(nodes, prefix)

		outfile = os.path.join(outpath, prefix +'-api.json')
		outfiletmp = os.path.join(outpath, prefix +'-api.json.tmp')

		dump_json(data, outfiletmp)
		os.rename(outfiletmp, outfile)

if __name__ == "__main__":
	main()
