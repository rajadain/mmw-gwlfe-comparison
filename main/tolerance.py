import os
import json
import argparse

from dictdiffer import diff

diffs = {}

argp = argparse.ArgumentParser(
    description='Compare GWLF-E Output to given tolerance')
argp.add_argument('tolerance', metavar='T', type=float,
                  help='How much difference to tolerate.')
argp.add_argument('--single', action='store_true', default=False,
                  help='Operate on single run results. Default false.')

args = argp.parse_args()

drexeldir = '../drexeleds/output_single/{}' \
            if args.single else '../drexeleds/output/{}'

for filename in os.listdir('../tests/'):
    with open(drexeldir.format(filename)) as d:
        with open('../wikiwatershed/output/{}'.format(filename)) as w:
            dv = json.load(d)
            wv = json.load(w)

            diffs[filename] = list(diff(wv, dv, tolerance=args.tolerance))

for filename, changes in diffs.iteritems():
    if not changes:
        print('{} matches to a tolerance of {}'
              .format(filename, args.tolerance))
        continue

    print('{} differs:'.format(filename))
    for change in changes:
        label = '[{}]'.format(change[1]) \
            if isinstance(change[1], basestring) \
            else ''.join('[{}]'.format(x) for x in change[1])
        value = '{:0.2f}%'.format(100 * (change[2][0] -
                                         change[2][1]) / change[2][0]) \
            if change[2][0] != 0 \
            else '{:0.2f} absolute'.format(change[2][0] - change[2][1])

        print('{}{}: {}'.format(filename, label, value))
