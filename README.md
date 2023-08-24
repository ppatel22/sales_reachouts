# Sales reachouts script

Run this script to quickly reach out to hundreds of potential clients in minutes, all through the CLI.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)

## Description

This code allows MITCap members to quickly send out emails to potential clients using a SMTP client Python package to connect to the email servers and Pandas to organize the companies. There are two .csv files in this repository that should be continuously updated: `companies_reached.csv` and `master_list.csv`. `companies_reached.csv` stores the companies that we have already emailed. `master_list.csv` stores all of the company contacts we have found thus far. 

## Getting Started

### Prerequisites

After cloning this repository, please run `pip install pandas smtplib`. Note that the `email.mime` import comes with the Python install by default.

### Installation

Clone this repository in a local directory on your computer. Confirm that the `companies_reached.csv` and `master_list.csv` are up-to-date before running the `mitcap_reachouts.py` file.

## Usage

Replace the placeholder sender email address with your own email address. Also replace your name with the placeholder in the body of the email. For ease of use, you can search for `***` and replace with the correct information. Run the `mitcap_reachouts.py`. For every email the script wants to send, your CLI will print the outgoing message and prompt you to enter `y` or `n` before sending the email.

## Contributing

If there are any issues with this code that you would like to report, please submit an open issue or email me at [princep@mit.edu](mailto:princep@mit.edu). If you are able to contribute to this project, feel free to submit a pull request with your suggested changes.


