# A Simple Staging Script (still in developmet)
This is a simple script to move our plots from a staging dir to the final destination dirs.

## Usage
1) Clone the repo
``` bash
git clone https://github.com/Hydrix/simple_staging_script
```

2) Move to the dir
``` bash
cd simple_staging_script
```
3) Config your staging dir to monitor and your(s) destination(s) dir(s) with your favorite edior
``` bash
vi config.yaml
```

4) Run the script
``` bash
python3 staging_script
```
Note: this script requires ``` bash sudo``` as ``` python3 shutil``` requires it 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
