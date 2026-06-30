import pandas as pd


def load_blackbox_csv(path):
    """
    Loads any Blackbox CSV regardless of how many metadata lines
    precede the actual table.
    """

    header_line = None

    with open(path, "r", encoding="utf-8", errors="ignore") as f:

        for i, line in enumerate(f):

            if line.startswith('"loopIteration"'):
                header_line = i
                break

    if header_line is None:
        raise RuntimeError(
            f"Could not find Blackbox data header in\n{path}"
        )

    df = pd.read_csv(path, skiprows=header_line)

    # Remove quotation marks from column names
    df.columns = df.columns.str.replace('"', '', regex=False)

    # Convert everything possible into numbers
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="ignore")

    return df