import argparse
import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    clean_data(args.input, args.output)
