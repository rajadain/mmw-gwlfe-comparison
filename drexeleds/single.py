import os
import json
import argparse

from StringIO import StringIO
from timeit import default_timer

from gwlfe import gwlfe, Parser

argp = argparse.ArgumentParser(description='Run GWLF-E on Single File')
argp.add_argument('filename', metavar='F', type=str,
                  help='Name of the file to process')

filename = argp.parse_args().filename

print('Processing {}...'.format(filename))

stages = [
    'read_input_file',
    'prepare_input_gms',
    'read_input_gms',
    'run_gwlfe',
    'write_output_file',
    'total',
]

timing = {s: 0 for s in stages}

start_time = default_timer()

filepath = os.path.abspath(
    os.path.join(__file__, '../../tests/', filename))

with open(filepath, 'r') as input_json:
    mapshed_data = json.load(input_json)
    timing['read_input_file'] = default_timer()

    # Round Areas
    mapshed_areas = [round(a, 1) for a in mapshed_data['Area']]
    mapshed_data['Area'] = mapshed_areas

    # Prepare input GMS
    pre_z = Parser.DataModel(mapshed_data)
    output = StringIO()
    writer = Parser.GmsWriter(output)
    writer.write(pre_z)
    output.seek(0)
    timing['prepare_input_gms'] = default_timer()

    # Read input GMS
    reader = Parser.GmsReader(output)
    z = reader.read()
    timing['read_input_gms'] = default_timer()

    # Run the model
    result, _ = gwlfe.run(z)
    timing['run_gwlfe'] = default_timer()

    # Write to file
    outpath = os.path.abspath(
        os.path.join(__file__, '../output_single/', filename))

    with open(outpath, 'w') as outfile:
        json.dump(result, outfile)
        timing['write_output_file'] = default_timer()

    # Save timings
    timing['total'] = timing['write_output_file'] - start_time
    for s in range(len(stages) - 2, 1, -1):
        timing[stages[s]] -= timing[stages[s - 1]]
    timing['read_input_file'] -= start_time

    timepath = outpath + '.timing'
    with open(timepath, 'w') as timefile:
        json.dump(timing, timefile)

end_time = default_timer()

print('Processed {} in {} seconds.'
      .format(filename, end_time - start_time))
