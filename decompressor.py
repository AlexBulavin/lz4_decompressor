#Author Alex Bulavin 31/12/2024
#This id a little script to decompress .lz4 type of files. For instance Firefox save sessions history in such format
#So to be able to read it, you can use this script
#First to install python itself and .lz4 library.
#Save this file wherever you like
#Then run it from command line or terminal like this:
#>python3 decompressor.py <input_file.jsonlz4> <output_file.json>
#Where instead of <input_file.jsonlz4> write the pass and source filename
#And instead of <output_file.json> write the pass and output filename
import lz4.block
import sys

if len(sys.argv) != 3:
   print("Usage: python3 decompress.py <input_file.jsonlz4> <output_file.json>")
   sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'rb') as f:
   data = f.read()

# Check for Mozilla's LZ4 file marker
if data[:8] != b'mozLz40\0':
   print("Invalid file format.")
   sys.exit(1)

# Strip Mozilla's custom header and decompress
decompressed_data = lz4.block.decompress(data[8:])

with open(output_file, 'wb') as f:
   f.write(decompressed_data)

print(f"Decompressed to {output_file}.")
