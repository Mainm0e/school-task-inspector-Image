import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def read_hidden_message(path, key='rb'):
    with open(path, key) as imageFile:
        content = imageFile.read()
        offset = content.index(bytes.fromhex('FFD9'))
        imageFile.seek(offset + 2)
        binary_data = imageFile.read()
        message = binary_data.decode('utf-8')
        return message

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("400x400")

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Create widgets
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Select Image", command=self.load_image)
        self.button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpeg")])

        if file_path:
            # Open the image file using Pillow
            image = Image.open(file_path)

            # Resize the image if needed
            # image = image.resize((width, height), Image.ANTIALIAS)

            # Convert the image to Tkinter PhotoImage format
            tk_image = ImageTk.PhotoImage(image)

            # Update the label with the new image
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image

            # Read and display the hidden message
            hidden_message = read_hidden_message(file_path)
            self.show_hidden_message(hidden_message)

    def show_hidden_message(self, message):
        if message:
            hidden_message_label = tk.Label(self.root, text="Hidden Message:")
            hidden_message_label.pack()

            hidden_message_text = tk.Text(self.root, height=5, width=40)
            hidden_message_text.insert(tk.END, message)
            hidden_message_text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
