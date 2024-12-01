
# Sure Bet Project

## Description
This project provides a system for identifying and executing sure bets between multiple betting platforms. It is structured into modular components for easy maintenance and extensibility.

## Project Structure
```
refactored_sure_bet/
├── crawler/         # Contains modules for handling different betting platforms
├── stats/           # Includes statistical computations for sure bets
├── tests/           # Unit tests for the project modules
├── utils/           # Utility functions (if needed in the future)
├── main.py          # Main entry point for the application
└── README.md        # Instructions and documentation
```

## Requirements
- Python 3.8 or higher
- Selenium WebDriver
- Google Chrome browser and ChromeDriver

## Installation
1. Clone the repository or extract the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure ChromeDriver is installed and in your system's PATH.

## Usage
- To run the main application:
  ```bash
  python main.py
  ```

- To execute the tests:
  ```bash
  python -m unittest discover -s tests
  ```

## Modules Overview
- **crawler/**: Handles interactions with different betting platforms.
- **stats/**: Computes statistical models for sure bets.
- **tests/**: Contains unit tests for verifying functionality.

## Contributing
Feel free to fork the repository and submit pull requests.

## License
This project is open-source and available under the MIT License.
