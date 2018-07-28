import os
import json

from dictdiffer import diff

diffs = {}

for filename in os.listdir('../tests/'):
    with open('../drexeleds/output/{}'.format(filename)) as d:
        with open('../wikiwatershed/output/{}'.format(filename)) as w:
            dv = json.load(d)
            wv = json.load(w)

            # Diff with 1% tolerance
            diffs[filename] = list(diff(wv, dv, tolerance=0.01))

for filename, changes in diffs.iteritems():
    if not changes:
        continue

    for change in changes:
        label = '[{}]'.format(change[1]) \
            if isinstance(change[1], basestring) \
            else ''.join('[{}]'.format(x) for x in change[1])
        value = '{:0.2f}%'.format(100 * (change[2][0] -
                                         change[2][1]) / change[2][0]) \
            if change[2][0] != 0 \
            else '{:0.2f} absolute'.format(change[2][0] - change[2][1])

        print('{}{}: {}'.format(filename, label, value))
