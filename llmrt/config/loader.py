from .models import ScanInput
import yaml

def payload_loader(payload_file):
    with open(payload_file, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML: {exc}")
            return []
    return [ScanInput(**item) for item in data]

