# README

This folder is dedicated to integrating the [m6r](https://github.com/m6r-ai/m6rc) file format into the threat model tool. The m6r file format is designed to facilitate the creation of threat models.

## Purpose

Add support for m6r files within the threat model tool.


## Contents

- **m6r_importer.py**: Script to import m6r files into the threat model tool.
- **m6r_exporter.py**: Script to export threat models from the tool into m6r format.
- **m6r_utils.py**: Utility functions to handle m6r file operations.
- **examples/**: Example m6r files to demonstrate the integration.

## Getting Started

To get started with m6r files in the threat model tool, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/m6r-ai/m6rc.git
    ```

2. Navigate to the [ai](http://_vscodecontentref_/0) folder:
    ```sh
    cd threat-model-tool/ai
    ```

3. Use the provided scripts to import or export m6r files:
    ```sh
    python m6r_importer.py path/to/your/file.m6r
    python m6r_exporter.py path/to/output/file.m6r
    ```

## Documentation

For detailed documentation on the m6r file format and its capabilities, please refer to the [m6r GitHub repository](https://github.com/m6r-ai/m6rc).

## Contributing

Contributions to improve the integration of m6r files into the threat model tool are welcome. Please submit pull requests or open issues on the GitHub repository.
