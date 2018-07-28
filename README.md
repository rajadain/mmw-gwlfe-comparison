# MMW GWLF-E Comparison

This repo is compares the performance of [GWLF-E][gwlfe] at [0.6.3][gwlfe-063]
against the [improvements made by Drexel][gwlfe-pr81] in [their
fork][gwlfe-drexeleds].

## Prerequisites

  * Python 2.7
  * [Pipenv][pipenv]

## Running the Comparison

Check out this branch and run `make`. This will:

  1. Install GWLF-E 0.6.3 in the `wikiwatershed` directory
  2. Install GWLF-E drexeleds#develop in the `drexeleds` directory
  3. Install dependencies for result interpretation in the `main` directory
  4. Run both versions against the tests in `tests` directory
      * These tests were compiled using stored data from a number of MapShed
        runs on a local database using the `extra/tests.sql` query
  5. Compare the timings for both and print the results
  6. Compare the results for both with a 1% tolerance and print the results

## Results

### Tolerance

Unfortunately, all but one files had significant differences in the results:

```shell
$ make -s tolerance | cut -f 1 -d\[ | uniq | sort

huc08__1747.json
huc08__1748.json
huc08__1750.json
huc08__1751.json
huc08__1773.json
huc10__11444.json
huc10__12968.json
huc10__1340.json
huc10__1341.json
huc10__2208.json
huc10__3176.json
huc10__3179.json
huc10__38.json
huc10__3928.json
huc10__9392.json
huc12__53956.json
huc12__55174.json
huc12__60099.json
huc12__60100.json
huc12__60101.json
```

The one file that did not have differences was `huc08__92.json`.

The total number of differences across the 20 files is 2249.

```shell
$ make -s tolerance | wc -l

    2249
```

If I delete one or more of the `tests/*.json` files, the tolerance results vary
wildly. It is hard to tell if this is a bug in the output generation code or in
the new GWLF-E itself.

### Timing

On my computer, a 2016 i5 13" MacBook Pro, there is significant speedup in the
GWLF-E model, and slight slowdowns in reading and writing GMS files:

```shell
$ make timing
bash -c "cd main; pipenv run python timing.py"

huc08
* Average read_input_file speedup: -3.48%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: -4.00%
* Average run_gwlfe speedup: 81.17%
* Average write_output_file speedup: -5.83%
* Average total speedup: 76.15%

huc10
* Average read_input_file speedup: 0.77%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: -0.06%
* Average run_gwlfe speedup: 80.59%
* Average write_output_file speedup: -1.44%
* Average total speedup: 75.34%

huc12
* Average read_input_file speedup: 0.67%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: -0.10%
* Average run_gwlfe speedup: 80.54%
* Average write_output_file speedup: -0.20%
* Average total speedup: 75.25%

Total
* Average read_input_file speedup: -0.47%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: -1.20%
* Average run_gwlfe speedup: 80.74%
* Average write_output_file speedup: -2.40%
* Average total speedup: 75.55%
```

[gwlfe]: https://github.com/WikiWatershed/gwlf-e
[gwlfe-063]: https://github.com/WikiWatershed/gwlf-e/releases/tag/0.6.3
[gwlfe-pr81]: https://github.com/WikiWatershed/gwlf-e/pull/81
[gwlfe-drexeleds]: https://github.com/drexeleds/gwlf-e
[pipenv]: https://github.com/pypa/pipenv
