# file-system-debug

An attempt to generate some synthetic files, recurisvely. 

NOTE THIS CAN GENERATE A TON OF FILES VERY QUICKLY. 

Be sure to pip-install python packages `click` and `tqdm`. 

Example invocation:
```
%  python generate-files.py --recurse-levels=2 --branch-factor=100 --leaf-number=33 --file-size=10 ./out
This will generate 330000 directories
This will generate 0.0033 GB of data

100%|█████████████████████████████████████████| 100/100 [01:18<00:00,  1.27it/s]
```

Run this script with ```--dryrun`` to just calculate use (but not create files)

For my purposes, I think I am aiming for 100M 4kB files, and will split on directories such that a reasonable simulation would be:


```
%  python generate-files.py --recurse-levels=4 --branch-factor=26 --leaf-number=200 --file-size=4000 ./out --dryrun
This will generate 91395200 directories
This will generate 365.5808 GB of data
```


