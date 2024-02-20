# INSPECTOR-IMAGE
<span style="color:red;">Warning:</span>This tool was developed for educational purposes only.

## Instruction
[Install Python](https://www.python.org/downloads/)
#### Install pip for download packages
* Execute the following command in your terminal:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
*  Install these packages for this program.

```
for mac
python3 pip install Pillow
python3 pip install pyexiv2
```

## Usage

```
python3 main.py -<flag> <image name>

```
> Image needs to be inside the 'resources' folder and must be a JPEG file.

#### flags
- *map*  function is employed to extract GPS information from the EXIF metadata of an image, enabling the retrieval of latitude and longitude coordinates, and subsequently returning the geolocation data."

- *steg*  extracts a hidden message from the provided image using steganography

#### Example

```
python3 main.py -map image.jpeg

Lat/Lon: (32.0866296534937)/ (34.885130555555556)
```


## Educational Purpose

- This tool is intended for educational purposes only. It is designed to demonstrate the principles of passive reconnaissance and OSINT, and to raise awareness about the privacy, security, ethical, and legal considerations associated with using such tools.
