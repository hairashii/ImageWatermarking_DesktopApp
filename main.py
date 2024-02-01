import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        # Create widgets
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.watermark_entry = tk.Entry(root, width=30)
        self.watermark_entry.insert(0, "Aira")
        self.watermark_entry.pack(pady=5)

        self.watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            print(f"Image selected: {self.image_path}")

    def add_watermark(self):
        if hasattr(self, 'image_path'):
            image = Image.open(self.image_path)

            watermark_text = self.watermark_entry.get()
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()  # customize the font here

            # Position the watermark at the bottom-right corner
            text_width, text_height = draw.textsize(watermark_text, font)
            position = (image.width - text_width - 10, image.height - text_height - 10)

            # Add the watermark
            draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))

            # Save the new image
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if output_path:
                image.save(output_path)
                print(f"Watermarked image saved to: {output_path}")
        else:
            print("Please upload an image first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
