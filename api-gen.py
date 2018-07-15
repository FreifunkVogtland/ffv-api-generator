#!/usr/bin/python3
# -*- coding: utf-8; -*-

import copy
import json
import os
import os.path
import sys

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
            'url': 'https://mapdata.freifunk-vogtland.net/',
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
                    'network': '10.204.0.0/16',
                },
            ],
            'ipv6': [
                {
                    'network': '2a03:2260:200f::/48',
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
                "IBAN": "DE30870958245000772005",
                "BIC": "GENODEF1PL1",
            },
        },
    },
}

cities = {
    "A": {
        'location': {
            'city': 'Adorf',
            'country': 'DE',
            'lat': 50.316667,
            'lon': 12.266667,
        },
    },
    "AE": {
        'location': {
            'city': 'Auerbach',
            'country': 'DE',
            'lat': 50.509444,
            'lon': 12.4,
        },
    },
    "BB": {
        'location': {
            'city': 'Bad Brambach',
            'country': 'DE',
            'lat': 50.216667,
            'lon': 12.316667,
        },
    },
    "BE": {
        'location': {
            'city': 'Bad Elster',
            'country': 'DE',
            'lat': 50.281944,
            'lon': 12.234722,
        },
    },
    "B": {
        'location': {
            'city': 'Bergen',
            'country': 'DE',
            'lat': 50.476389,
            'lon': 12.279167,
        },
    },
    "BOE": {
        'location': {
            'city': 'Bösenbrunn',
            'country': 'DE',
            'lat': 50.397222,
            'lon': 12.1,
        },
    },
    "EIC": {
        'location': {
            'city': 'Eichigt',
            'country': 'DE',
            'lat': 50.35,
            'lon': 12.166667,
        },
    },
    "ELL": {
        'location': {
            'city': 'Ellefeld',
            'country': 'DE',
            'lat': 50.483333,
            'lon': 12.4,
        },
    },
    "ELS": {
        'location': {
            'city': 'Elsterberg',
            'country': 'DE',
            'lat': 50.6,
            'lon': 12.166667,
        },
    },
    "FST": {
        'location': {
            'city': 'Falkenstein',
            'country': 'DE',
            'lat': 50.466667,
            'lon': 12.366667,
        },
    },
    "GB": {
        'location': {
            'city': 'Grünbach',
            'country': 'DE',
            'lat': 50.452778,
            'lon': 12.362778,
        },
    },
    "HDG": {
        'location': {
            'city': 'Heinsdorfergrund',
            'country': 'DE',
            'lat': 50.622222,
            'lon': 12.372222,
        },
    },
    "K": {
        'location': {
            'city': 'Klingenthal',
            'country': 'DE',
            'lat': 50.357126,
            'lon': 12.468452,
        },
    },
    "LE": {
        'location': {
            'city': 'Lengenfeld',
            'country': 'DE',
            'lat': 50.569454,
            'lon': 12.364973,
        },
    },
    "L": {
        'location': {
            'city': 'Limbach',
            'country': 'DE',
            'lat': 50.583889,
            'lon': 12.252778,
        },
    },
    "MKN": {
        'location': {
            'city': 'Markneukirchen',
            'country': 'DE',
            'lat': 50.316667,
            'lon': 12.316667,
        },
    },
    "MTL": {
        'location': {
            'city': 'Mühlental',
            'country': 'DE',
            'lat': 50.451944,
            'lon': 12.481389,
        },
    },
    "MH": {
        'location': {
            'city': 'Muldenhammer',
            'country': 'DE',
            'lat': 50.435556,
            'lon': 12.462778,
        },
    },
    "N": {
        'location': {
            'city': 'Netzschkau',
            'country': 'DE',
            'lat': 50.616667,
            'lon': 12.25,
        },
    },
    "NSZ": {
        'location': {
            'city': 'Neuensalz',
            'country': 'DE',
            'lat': 50.518056,
            'lon': 12.220556,
        },
    },
    "NMK": {
        'location': {
            'city': 'Neumark',
            'country': 'DE',
            'lat': 50.666667,
            'lon': 12.35,
        },
    },
    "NST": {
        'location': {
            'city': 'Neustadt',
            'country': 'DE',
            'lat': 50.466667,
            'lon': 12.333333,
        },
    },
    "OEL": {
        'location': {
            'city': 'Oelsnitz',
            'country': 'DE',
            'lat': 50.416667,
            'lon': 12.166667,
        },
    },
    "PMF": {
        'location': {
            'city': 'Pausa-Mühltroff',
            'country': 'DE',
            'lat': 50.58225,
            'lon': 11.992194,
        },
    },
    "PL": {
        'location': {
            'city': 'Plauen',
            'country': 'DE',
            'lat': 50.483333,
            'lon': 12.116667,
        },
    },
    "POE": {
        'location': {
            'city': 'Pöhl',
            'country': 'DE',
            'lat': 50.566667,
            'lon': 12.15,
        },
    },
    "RC": {
        'location': {
            'city': 'Reichenbach',
            'country': 'DE',
            'lat': 50.620802,
            'lon': 12.303262,
        },
    },
    "RDW": {
        'location': {
            'city': 'Rodewisch',
            'country': 'DE',
            'lat': 50.516667,
            'lon': 12.416667,
        },
    },
    "RBH": {
        'location': {
            'city': 'Rosenbach',
            'country': 'DE',
            'lat': 50.54,
            'lon': 12.040556,
        },
    },
    "S": {
        'location': {
            'city': 'Schöneck',
            'country': 'DE',
            'lat': 50.366667,
            'lon': 12.316667,
        },
        "address": {
            "Name": "hateotu.de (bei GK)",
            "Street": "Waldstraße 7",
            "Zipcode": "08261"
        }
    },
    "SBG": {
        'location': {
            'city': 'Steinberg',
            'country': 'DE',
            'lat': 50.538889,
            'lon': 12.477778,
        },
    },
    "T": {
        'location': {
            'city': 'Theuma',
            'country': 'DE',
            'lat': 50.47,
            'lon': 12.2225,
        },
    },
    "TDF": {
        'location': {
            'city': 'Tirpersdorf',
            'country': 'DE',
            'lat': 50.434722,
            'lon': 12.254167,
        },
    },
    "TR": {
        'location': {
            'city': 'Treuen',
            'country': 'DE',
            'lat': 50.5425,
            'lon': 12.302222,
        },
    },
    "TRI": {
        'location': {
            'city': 'Triebel',
            'country': 'DE',
            'lat': 50.35,
            'lon': 12.133333,
        },
    },
    "WEI": {
        'location': {
            'city': 'Weischlitz',
            'country': 'DE',
            'lat': 50.447222,
            'lon': 12.059722,
        },
    },
    "WER": {
        'location': {
            'city': 'Werda',
            'country': 'DE',
            'lat': 50.4375,
            'lon': 12.305556,
        },
    },
}


def dump_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
        f.flush()
        os.fsync(f.fileno())


def filter_nodes_city(meshviewer, prefix):
    domain_code = 'ffv_' + prefix.lower()
    nodelist_city = {
        'nodes': [],
        'updated_at': meshviewer['timestamp'],
        'version': '1.0.1',
    }

    for node in meshviewer['nodes']:
        if 'site_code' not in node:
            continue

        if node['site_code'] != domain_code:
            continue

        if 'node_id' not in node:
            continue

        if 'hostname' not in node:
            continue

        if 'lastseen' not in node:
            continue

        if 'is_online' not in node:
            continue

        if 'clients' not in node:
            continue

        entry = {
            'name': node['hostname'],
            'id': node['node_id'],
            'status': {
                'lastcontact': node['lastseen'],
                'clients': node['clients'],
                'online': node['is_online'],
            },
        }

        if 'location' in node and 'latitude' in node['location'] and 'longitude' in node['location']:
            entry['position'] = {
                'lat': node['location']['latitude'],
                'long': node['location']['longitude'],
            }

        nodelist_city['nodes'].append(entry)

    return nodelist_city


def generate_city_data(nodelist, prefix):
    apidata = copy.deepcopy(generic_api)

    for replacekey in cities[prefix]:
        apidata[replacekey] = cities[prefix][replacekey]

    apidata['state']['lastchange'] = nodelist['updated_at']
    apidata['state']['nodes'] = len(nodelist['nodes'])
    apidata['nodeMaps'][0]['url'] += 'nodelist-%s.json' % (prefix)

    return apidata


def main():
    if len(sys.argv) != 3:
        print("./api-gen.py MESHVIEWERJSON OUTPATH")
        sys.exit(1)

    meshviewerjson = sys.argv[1]
    outpath = sys.argv[2]

    # load
    meshviewer = json.load(open(meshviewerjson))

    # store
    for prefix in cities:
        nodelist_city = filter_nodes_city(meshviewer, prefix)
        data = generate_city_data(nodelist_city, prefix)

        outfile = os.path.join(outpath, 'ffapi-%s.json' % (prefix))
        outfiletmp = os.path.join(outpath, 'ffapi-%s.json.tmp' % (prefix))

        outnodelist = os.path.join(outpath, 'nodelist-%s.json' % (prefix))
        outnodelisttmp = os.path.join(outpath, 'nodelist-%s.json.tmp' %
                                               (prefix))

        dump_json(data, outfiletmp)
        dump_json(nodelist_city, outnodelisttmp)

        os.rename(outfiletmp, outfile)
        os.rename(outnodelisttmp, outnodelist)


if __name__ == "__main__":
    main()
