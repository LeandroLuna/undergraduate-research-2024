from PIL import Image
import numpy as np

def generate_id_from_image(image: Image.Image) -> int:         
    image_array = np.array(image)
        
    pixel_sum = np.sum(image_array)
    
    return int(pixel_sum)