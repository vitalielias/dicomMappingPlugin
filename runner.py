import jammato
import sys

map_json_path = sys.argv[1]
metadata_files_location = sys.argv[2]
mapped_metadata = sys.argv[3]

# schema_path = '/Users/elias/Desktop/MatWerk_Projects/jammato_test/JaMMaTo-main/example/metadata_maps/map_full_path.json'
# dicom_path  = '/Users/elias/Desktop/MatWerk_Projects/jammato_test/JaMMaTo-main/example/dicom_files/MRIm1.dcm'

jammato.dicom_mapping.Dicom_Mapping(map_json_path, metadata_files_location, mapped_metadata)