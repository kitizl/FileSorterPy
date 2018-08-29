# FileSorterPy
A python script that moves and arranges videos (any file, really) into it's own respective folders based on the timestamp, which is usually the filename.

## Usage

Clone this repo and move the script to the folder containing the files. Then run the python script using `python filesort.py`

You should find your videos organized in folders starting from the year of recording, the month of recording all the way down to the day of recording.

NOTE : This works only if the filename format is like the following : `yyyymmdd-nnnnnn` where yyyy is the year, mm is the month, dd is the day and nnnnnn is a six-digit number.

---

This was built for automating the process of organizing my video files for [my YouTube channel](www.youtube.com/ThePrimevalVoid). I realize this isn't the best script to do the job, but it works. Performance improvements might happen in the future when I find free time to update the script.

This script might be useful to those who probably make their living on daily vlogs or editing daily vlogs, or have a large backlog of footage that needs to be edited into a single vlog.

## TODO:

- [ ] Add flags to select the directory that contains the files that need to be sorted
- [ ] Add helptext
