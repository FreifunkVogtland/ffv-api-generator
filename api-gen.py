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
		'irc': 'irc://chat.freenode.net/ffv',
	},
	'feeds': [
		{
			'category': 'blog',
			'name': 'Freifunk Vogtland Blog',
			'type': 'rss',
			'url': 'https://vogtland.freifunk.net/feed/',
		},
	],
	'nodeMaps': [
		{
			'interval': '1min',
			'technicalType': 'nodelist',
			'url': 'https://vpn01.freifunk-vogtland.net/ffv/',
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
	'url': 'https://vogtland.freifunk.net/',
	"support": {
		"donations": {
			"bankaccount": {
				"IBAN":"DE30870958245000772005",
				"BIC":"GENODEF1PL1",
			},
		},
	},
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
	"BB" : {
		'location': {
			'city': 'Bad Brambach',
			'country': 'DE',
			'lat': 50.216667,
			'lon': 12.316667,
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
	"B" : {
		'location': {
			'city': 'Bergen',
			'country': 'DE',
			'lat': 50.476389,
			'lon': 12.279167,
		},
	},
	"BBN" : {
		'location': {
			'city': 'Bösenbrunn',
			'country': 'DE',
			'lat': 50.397222,
			'lon': 12.1,
		},
	},
	"EI" : {
		'location': {
			'city': 'Eichigt',
			'country': 'DE',
			'lat': 50.35,
			'lon': 12.166667,
		},
	},
	"ELL" : {
		'location': {
			'city': 'Ellefeld',
			'country': 'DE',
			'lat': 50.483333,
			'lon': 12.4,
		},
	},
	"ELS" : {
		'location': {
			'city': 'Elsterberg',
			'country': 'DE',
			'lat': 50.6,
			'lon': 12.166667,
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
	"HDG" : {
		'location': {
			'city': 'Heinsdorfergrund',
			'country': 'DE',
			'lat': 50.622222,
			'lon': 12.372222,
		},
	},
	"K" : {
		'location': {
			'city': 'Klingenthal',
			'country': 'DE',
			'lat': 50.357126,
			'lon': 12.468452,
		},
	},
	"LEN" : {
		'location': {
			'city': 'Lengenfeld',
			'country': 'DE',
			'lat': 50.569454,
			'lon': 12.364973,
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
	"MTL" : {
		'location': {
			'city': 'Mühlental',
			'country': 'DE',
			'lat': 50.451944,
			'lon': 12.481389,
		},
	},
	"NSZ" : {
		'location': {
			'city': 'Neuensalz',
			'country': 'DE',
			'lat': 50.518056,
			'lon': 12.220556,
		},
	},
	"NMK" : {
		'location': {
			'city': 'Neumark',
			'country': 'DE',
			'lat': 50.666667,
			'lon': 12.35,
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
	"POE" : {
		'location': {
			'city': 'Pöhl',
			'country': 'DE',
			'lat': 50.566667,
			'lon': 12.15,
		},
	},
	"RC" : {
		'location': {
			'city': 'Reichenbach',
			'country': 'DE',
			'lat': 50.620802,
			'lon': 12.303262,
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
	"S" : {
		'location': {
			'city': 'Schöneck',
			'country': 'DE',
			'lat': 50.366667,
			'lon': 12.316667,
		},
	},
	"SBG" : {
		'location': {
			'city': 'Steinberg',
			'country': 'DE',
			'lat': 50.538889,
			'lon': 12.477778,
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

def filter_nodes_city(nodelist, prefix):
	nodelist_city = copy.copy(nodelist)
	nodelist_city['nodes'] = list(filter(lambda n: n['name'].startswith(prefix + '-'), nodelist['nodes']))
	return nodelist_city

def generate_city_data(nodelist, prefix):
	apidata = copy.deepcopy(generic_api)

	for replacekey in cities[prefix]:
		apidata[replacekey] = cities[prefix][replacekey]

	apidata['state']['lastchange'] = datetime.utcnow().isoformat() + 'Z'
	apidata['state']['nodes'] = len(nodelist['nodes'])
	apidata['nodeMaps'][0]['url'] += 'nodelist-%s.json' % (prefix)

	return apidata

def main():
	if len(sys.argv) != 3:
		print("./api-gen.py NODELIST OUTPATH")
		sys.exit(1)

	nodelistjson = sys.argv[1]
	outpath = sys.argv[2]

	# load
	nodelist = json.load(open(nodelistjson))

	# store
	for prefix in cities:
		nodelist_city = filter_nodes_city(nodelist, prefix)
		data = generate_city_data(nodelist_city, prefix)

		outfile = os.path.join(outpath, 'ffapi-%s.json' % (prefix))
		outfiletmp = os.path.join(outpath, 'ffapi-%s.json.tmp' % (prefix))

		outnodelist = os.path.join(outpath, 'nodelist-%s.json' % (prefix))
		outnodelisttmp = os.path.join(outpath, 'nodelist-%s.json.tmp' % (prefix))

		dump_json(data, outfiletmp)
		dump_json(nodelist_city, outnodelisttmp)

		os.rename(outfiletmp, outfile)
		os.rename(outnodelisttmp, outnodelist)

if __name__ == "__main__":
	main()
