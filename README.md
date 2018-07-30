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
  6. Compare the results for both with a 0.000000000001% tolerance and print the results

## Results

### Tolerance

Given the [latest code][gwlfe-drexeleds-develop], the numbers match:

```shell
$ make -s tolerance

huc08__1751.json matches to a tolerance of 1e-14
huc12__60101.json matches to a tolerance of 1e-14
huc08__1750.json matches to a tolerance of 1e-14
huc10__9392.json matches to a tolerance of 1e-14
huc08__1748.json matches to a tolerance of 1e-14
huc12__53956.json matches to a tolerance of 1e-14
huc10__2208.json matches to a tolerance of 1e-14
huc08__1773.json matches to a tolerance of 1e-14
huc10__38.json matches to a tolerance of 1e-14
huc10__1340.json matches to a tolerance of 1e-14
huc10__3176.json matches to a tolerance of 1e-14
huc12__60099.json matches to a tolerance of 1e-14
huc08__1747.json matches to a tolerance of 1e-14
huc10__12968.json matches to a tolerance of 1e-14
huc10__3928.json matches to a tolerance of 1e-14
huc10__11444.json matches to a tolerance of 1e-14
huc08__92.json matches to a tolerance of 1e-14
huc12__55174.json matches to a tolerance of 1e-14
huc10__3179.json matches to a tolerance of 1e-14
huc10__1341.json matches to a tolerance of 1e-14
huc12__60100.json matches to a tolerance of 1e-14
```

### Timing

On my computer, a 2015 i5 13" MacBook Pro, there is significant speedup in the
GWLF-E model, and slight slowdowns in reading and writing files:

```shell
$ make -s timing

huc08
* Average read_input_file speedup: -11.26%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: 6.97%
* Average run_gwlfe speedup: 82.80%
* Average write_output_file speedup: -42.99%
* Average total speedup: 78.57%

huc10
* Average read_input_file speedup: -19.21%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: 1.46%
* Average run_gwlfe speedup: 79.11%
* Average write_output_file speedup: 9.03%
* Average total speedup: 74.17%

huc12
* Average read_input_file speedup: -12.52%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: 1.57%
* Average run_gwlfe speedup: 79.07%
* Average write_output_file speedup: 1.25%
* Average total speedup: 73.99%

Total
* Average read_input_file speedup: -15.34%
* Average prepare_input_gms speedup: 0.00%
* Average read_input_gms speedup: 3.06%
* Average run_gwlfe speedup: 80.15%
* Average write_output_file speedup: -7.69%
* Average total speedup: 75.38%
```

[gwlfe]: https://github.com/WikiWatershed/gwlf-e
[gwlfe-063]: https://github.com/WikiWatershed/gwlf-e/releases/tag/0.6.3
[gwlfe-pr81]: https://github.com/WikiWatershed/gwlf-e/pull/81
[gwlfe-drexeleds]: https://github.com/drexeleds/gwlf-e
[gwlfe-drexeleds-develop]: https://github.com/drexeleds/gwlf-e/commit/9e058445537dd32d1916f76c4b73ca64261771cd
[pipenv]: https://github.com/pypa/pipenv
