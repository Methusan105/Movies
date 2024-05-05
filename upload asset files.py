import os

release_file_path = r"C:\Users\Methu\Videos\GK\Guntur.Kaaram.zip"

# Assuming you want to iterate from 2 to 29
for i in range(1, 8):
    file_number = f"{i:03d}"  # Format the number with leading zeros
    file_path = f'{release_file_path}.{file_number}'
    
    command = f'gh release upload GK "{file_path}" --clobber'
    
    # Execute the command
    os.system(command)
