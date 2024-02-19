import argparse

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
    parser = argparse.ArgumentParser(description='Extract hidden message from an image file.')
    parser.add_argument('image', help='Path to the image file')
    
    args = parser.parse_args()
    
    image_path = args.image
    key = 'rb'
    
    try:
        hidden_message = read_hidden_message(image_path, key)
        print('Hidden Message:\n', hidden_message)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()