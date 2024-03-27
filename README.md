# NCAA Baseball Statistics Platform

This project aims to develop a comprehensive platform for NCAA baseball sabermetrics. The platform consists of several components that work together to collect, calculate, store, and present the sabermetrics data.

## Components

* **ncaabsb**: A custom R library build on top of the `baseballr` package. This library contains custom functions to collect data from `baseballr` and calculate the desired sabermetrics.
* **Database**: A database system to store the collected data and calculated sabermetrics. The database will be updated daily using automation tasks.
* **Backend API**: A REST API that fetches data by querying the database. This API will serve as the interface between the frontend and the database.
* **Frontend**: A user-facing web applicatoin that interacts with the backend API to display the sabermetrics data in a user-friendly manner

## Getting Started

Development has not began for all parts of the project yet, so this section does not yet apply.

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/smomara/ncaa_bsb_stats_platform.git`
2. Install the necessary dependencies for each component (instructions in respective directories)
3. Set up the database and configure the connection details
4. Run the automation tasks to populate the database with initial data
5. Start the backend API server
6. Launch the frontend application

Detailed instructions for each step will be found in the respective component's directory.

## Contributing

As a group member, you can contribute to the project by:
* Implementing new features or enhancements in any of the components
* Fixing bugs or addressing issues reported in the issue tracker
* Reviewing and providing feedback on pull requests from other group members

Please make sure to submit pull requests for review before merging into the main branch.