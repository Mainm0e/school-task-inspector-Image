import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def extract_gps_info(image_path):
    image = Image.open(image_path)
    info = image._getexif()  
    exif_data = {}
    for tag_id, value in info.items():
        tag = TAGS.get(tag_id, tag_id)

        if tag == "GPSInfo":
            gps_data = {}
            for t in value:
                gps_tag = GPSTAGS.get(t, t)
                gps_data[gps_tag] = value[t]

            exif_data[tag] = gps_data
        else:
            exif_data[tag] = value

    return exif_data 

def extract_lat_lon(exif_data):
    if 'GPSInfo' in exif_data:
        gps_info = exif_data['GPSInfo']
        if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
            latitude = sum(float(value) / 60 ** i for i, value in enumerate(gps_info['GPSLatitude']))
            longitude = sum(float(value) / 60 ** i for i, value in enumerate(gps_info['GPSLongitude']))
            return "Lat/Lon: ({0})/ ({1})".format(latitude, longitude)

    return None



def read_hidden_message(path,key):
    # key = 'rb'
    with open(path, key) as imageFile:
        content = imageFile.read()
        offset = content.index(bytes.fromhex('FFD9'))
        imageFile.seek(offset + 2)
        binary_data = imageFile.read()
        message = binary_data.decode('utf-8')
        return message
    
def main():
    parser = argparse.ArgumentParser(description='Image Analysis')
    parser.add_argument('image', help='Path to the image file')
    parser.add_argument('-map', action='store_true', help='Extract GPS info')
    parser.add_argument('-steg', action='store_true', help='Extract hidden message')

    args = parser.parse_args()
    image_path = args.image

    if args.map:
        gps_info = extract_gps_info(image_path)
        
        if gps_info:
            lat_lon = extract_lat_lon(gps_info)
            print(lat_lon)
        else:
            print('No GPS information found in the image.')

    if args.steg:
        hidden_message = read_hidden_message(image_path,'rb')
        if hidden_message:
            print(hidden_message)
        else:
            print('No hidden message found in the image.')

if __name__ == "__main__":
    main()