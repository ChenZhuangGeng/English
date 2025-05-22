import random

def shuffle_lines_in_file(input_filepath: str, output_filepath: str):
    """
    Reads lines from a file, shuffles them, and writes them to a new file.

    Args:
        input_filepath: Path to the input file.
        output_filepath: Path to the output file where shuffled lines will be saved.
    """
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
        return
    except Exception as e:
        print(f"Error reading file '{input_filepath}': {e}")
        return

    if not lines:
        print(f"Warning: Input file '{input_filepath}' is empty or contains no lines to shuffle.")
        try:
            # Create an empty output file if the input is empty
            with open(output_filepath, 'w', encoding='utf-8') as f_out:
                pass 
            print(f"Empty output file '{output_filepath}' created as input was empty.")
        except Exception as e:
            print(f"Error creating empty output file '{output_filepath}': {e}")
        return

    random.shuffle(lines)

    try:
        with open(output_filepath, 'w', encoding='utf-8') as f_out:
            f_out.writelines(lines)
        print(f"Successfully shuffled '{input_filepath}' and saved to '{output_filepath}'.")
    except Exception as e:
        print(f"Error writing to file '{output_filepath}': {e}")

if __name__ == '__main__':
    input_file = "完整5995.txt"
    output_file = "shuffled_完整5995.txt"
    shuffle_lines_in_file(input_file, output_file)
