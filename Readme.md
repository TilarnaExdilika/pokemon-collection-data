# Pokémon Data Collection

## Data Sources

The data in this project is collected from the following sources:

- TCG data: [PkmnCards](https://pkmncards.com/sets/)
- Pokédex data
- Pokémon Showdown

## Description

This is a comprehensive Pokémon data collection, including detailed information about Pokémon and Pokémon Trading Card Game (TCG) sets.

## Directory Structure

- `pokemon-tcg-collections/`: Main directory containing TCG sets
- `pokedex/`: Contains Pokédex data
- `showdown-data/`: Contains data related to Pokémon Showdown

## Using get_tools.py

![Demo Run Tools](/screenshots/demo_create_folder.png)
![Demo Run Tools](/screenshots/demo_download.png)

`get_tools.py` is a tool for downloading and organizing Pokémon TCG set data.

### How to use

1. Open terminal or command prompt

2. download `pokemon-tcg-collections/get_tools.py`:

   ```bash
   download or copy file get_tools.py
   ```

3. Run the script:

   ```bash
   python get_tools.py
   ```

4. Wait for the folder creation and download process to complete

### Features

- Creates directory structure for TCG sets
- Downloads card images from online sources
- Organizes images into corresponding folders

### Note

- Ensure you have a stable internet connection when running the script
- The process may take some time depending on the number of sets and images to be downloaded

## Additional Data

- The file `pokedex/pokemons.json` contains detailed information about Pokémon
- The file `showdown-data/pokedex.json` contains Pokédex data for Pokémon Showdown

## Contributing

If you want to contribute to this project, please create a pull request or report issues in the Issues section.

## License

.
