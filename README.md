# EsportsPulse

A lightweight Python tool for quickly gathering, aggregating, and parsing global esports news and data.

![License](https://img.shields.io/github/license/jianlang829/esportspulse)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## Overview

EsportsPulse is designed to simplify the process of collecting esports information from various sources. Whether you're a developer building an esports app, a data analyst studying gaming trends, or an enthusiast who wants to stay updated, this tool provides a straightforward way to access structured esports data.

## Sample

![效果图](效果图.jpg '效果图')

## Features

- **Multi-game Support**: Covers major esports titles including LOL, DOTA2, CS:GO, Valorant, and more
- **Real-time Updates**: Fetches latest news, match results, and schedule information
- **Structured Data**: Outputs data in JSON/CSV format for easy processing
- **Custom Filters**: Allows filtering by game, tournament, team, or player
- **Lightweight**: Minimal dependencies, easy to integrate into existing projects
- **Rate Limiting**: Built-in protection to respect source website policies

## Installation

Or install from source:

```bash
git clone https://github.com/jianlang829/esportspulse.git
cd esportspulse
```

## Documentation

### Available Methods

- `get_news(game=None, limit=10)`: Fetch latest news articles
- `get_upcoming_matches(game=None, days=7)`: Get scheduled matches
- `get_recent_results(game=None, days=7)`: Retrieve recent match results
- `get_teams(game=None)`: Get information about professional teams
- `get_players(team=None)`: Get player statistics and profiles
- `get_tournaments(game=None)`: Get current and upcoming tournaments
- `save_to_json(data, filename)`: Save data to JSON file
- `save_to_csv(data, filename)`: Save data to CSV file

## Data Sources

EsportsPulse aggregates information from various reputable esports news sites and APIs. Please respect the terms of service of these sources when using the data.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring their use complies with applicable laws and website terms of service.

---

Made with ❤️ for the esports community
