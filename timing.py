import os
import json

stages = [
    'read_input_file',
    'prepare_input_gms',
    'read_input_gms',
    'run_gwlfe',
    'write_output_file',
    'total',
]

groups = ['huc08', 'huc10', 'huc12']

speedup = {
    group: {s: [] for s in stages}
    for group in groups
}

count = {group: 0 for group in groups}

for filename in os.listdir('tests/'):
    group = filename[:5]
    count[group] += 1

    with open('./drexeleds/output/{}.timing'.format(filename)) as d:
        with open('./wikiwatershed/output/{}.timing'.format(filename)) as w:
            dt = json.load(d)
            wt = json.load(w)

            for s in stages:
                speedup[group][s].append((wt[s] - dt[s]) / wt[s])

avg_speedup = {
    group: {
        stage: sum(values) / count[group]
        for stage, values in timing.iteritems()
    } for group, timing in speedup.iteritems()
}

total_speedup = {
    stage: [x for group in groups for x in speedup[group][stage]]
    for stage in stages
}

total_count = sum(count.itervalues())

for group in groups:
    print('\n{}'.format(group))

    for stage in stages:
        print('* Average {} speedup: {:0.2f}%'.format(
            stage, 100 * avg_speedup[group][stage]))

print('\nTotal')

for stage in stages:
    print('* Average {} speedup: {:0.2f}%'.format(
        stage, 100 * sum(total_speedup[stage]) / total_count))
