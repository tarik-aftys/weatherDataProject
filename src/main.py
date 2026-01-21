import os
import sys
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
extract_script = os.path.join(script_dir, "extract.py")
transform_script = os.path.join(script_dir, "transform.py")
csv_file = os.path.join(project_dir, "data", "processed", "weather_clean.csv")


def run_extract():
    result = subprocess.run([sys.executable, extract_script], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Extraction réussie\n")
        return True
    else:
        print("Erreur lors de l'extraction:")
        print(result.stderr)
        return False

def run_transform():
    result = subprocess.run([sys.executable, transform_script], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Transformation réussie\n")
        return True
    else:
        print("Erreur lors de la transformation:")
        print(result.stderr)
        return False


def main():
    
    if not run_extract():
        print("\nLe pipeline a échoué à l'étape d'extraction")
        sys.exit(1)
    
    if not run_transform():
        print("\nLe pipeline a échoué à l'étape de transformation")
        sys.exit(1)
    

    
    print("Pipeline terminé avec succès!")

if __name__ == "__main__":
    main()

