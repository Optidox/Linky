# Linky

Linky is a Discord bot for archiving links in their own channel

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

If you want to add Linky to your Discord server, use this link: https://discord.com/oauth2/authorize?client_id=732003064688410675&permissions=83968&scope=bot

### Prerequisites

Python 3 is the only requirement for running Linky.

### Installing

If you wish to modify or run your own instance of Linky, first appropriately configure a bot in the Discord Developer Portal (permissions needed are read message history, send messages, and embed links) do the following:

1. Clone this repository with git
```git clone https://github.com/optidox/Linky```
2. Install the packages listed in [requirements.txt](requirements.txt)
```pip install -r requirements.txt```
3. Create a .env file with the following structure:

```
DISCORD_TOKEN=your-token
```

## Running the tests

To run Linky, navigate to your Linky directory with a command line and type:
```python Linky.py```

Linky can be run in the background in Linux with:
```nohup python Linky.py &```

## Built With

* [discord.py](https://discordpy.readthedocs.io/en/latest/)

## Author

* **Matthew Sims** - [Optidox](https://github.com/Optidox)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) for details

## Acknowledgments

Thank you to [Will Schoeder](https://www.youtube.com/channel/UCcRdUHUuBqU9uCsEuG39Nmg) for sponsoring this project.

