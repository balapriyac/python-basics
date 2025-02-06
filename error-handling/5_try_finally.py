class ImageProcessor:
    def __init__(self):
        self.temp_files = []
    
    def process_image(self, image_path):
        temp_output = f"temp_{image_path}"
        self.temp_files.append(temp_output)
        
        try:
            # Process the image
            raw_data = self.load_image(image_path)
            processed = self.apply_filters(raw_data)
            self.save_image(processed, temp_output)
            return self.upload_to_cloud(temp_output)
        finally:
            # Clean up temporary files
            for temp_file in self.temp_files:
                try:
                    os.remove(temp_file)
                except OSError:
                    logging.error(f"Failed to remove temp file: {temp_file}")
            self.temp_files = []
          
