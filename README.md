# Scaled
Thoughts and ideas on how to scale

## Intention

I have created and maintained systems to work for clients of various sizes. Some clients processed a few hundred orders a day, while others handled a few hundred orders per minute at a single facility.

Scaling for a few hundred orders a day is relatively easy. Often, I didn't have to tune or modify anything.

Scaling for customers that process a few hundred orders per minute is a very different challenge. Consider a client with multiple fulfillment warehouses that needs to process shipments quickly. This customer must ship hundreds of orders per minute. Multiple systems need to communicate with each other, such as a warehouse execution system that interacts with a warehouse management system. Both systems may rely on third-party components to handle tasks like:

- Determining the quickest pick path for a collection of cartons.
- Identifying which fulfillment center has the inventory to meet the agreed-upon delivery time.
- Deciding whether an order split between warehouses can group items into a single carton (e.g., shipping a bowling ball and a fragile item from the same fulfillment center still requires two cartons).
- Calculating the cheapest shipping method that meets the delivery deadline.
- Providing a reporting system with metrics for all of these processes or a specialized vertical slice.

While I have worked on the above problems and many others in logistics software, I will focus on the last item—reporting systems—because it easily demonstrates scaling issues. This repository will generate order data for multiple clients and show, in stages with examples, how scaling can be achieved. The plan is to use both PostgreSQL and MongoDB to demonstrate that both can be scaled for reporting using different techniques. Often, developers focus on technology to scale, but I argue that scaling can often be achieved with the tools you already have.

Some solutions are quick fixes, while others require more work or rework. Sometimes, a temporary solution is all that can be done while systems are reworked or rebuilt.

**The process is just as important as the solution.**

## Technology

### Backend Language

I will start with a technology that is often labeled as slow: Python. Python has a reputation for being slow in reporting applications, but I argue that database calls and data organization are more critical than the backend technology. Each backend call will include timing information for how long the request took and how long the database calls took. Both metrics will help determine whether Python is truly the bottleneck or if the issue lies elsewhere.

### Database Layer

For reporting software, I have often heard that SQL solutions do not scale well. I want to test this claim. I will start with PostgreSQL to establish a baseline. From there, I will also include a MongoDB backend. The goal is to compare both technologies to determine whether the technology itself is the issue or if the problem lies elsewhere.

### Other Technology

I plan to use React to display the data in charts and graphs. I have not yet decided which library I will use for this purpose.

Each stage will include a Docker Compose file so that others can validate or challenge my results.

## Layout

There will be an overall README file explaining each step and my thought process at each stage of scaling the reporting system. Each stage will have its own code to demonstrate how changes affected the speed and memory usage of the reporting system. I will also include steps to reproduce the data used at each stage. This way, even though numbers may vary between machines, the magnitude of changes will remain consistent.

Each stage will be contained in a `stages` folder, with all files for that stage included within the folder.

## Original Data

The `postal.csv` file is derived from an Excel file called `ZIP_Locale_Detail.xls`, which I downloaded from the U.S. Census Bureau. I removed all postal codes except those for the 50 states.

All orders, items, and tenant UUIDs are generated. I anticipate that I may need to revisit how order times are generated and switch to something like a shuffle bag. For now, I am using Python's built-in `random` library.

Orders are generated and placed in an `orders` folder. Each folder under `orders` is named after a date. Each file in those folders is named after a tenant's UUID and contains all the orders for that tenant on that day.

I then import these orders into a database. I am currently building the first phase in SQLite and will switch to the aforementioned databases when ready.

## How To Run

The project has three major components that need to be ran. They are the data generator, front end and stages. Each component is explained below.

### Data Generator

Found at the root of the `src` directory. The `generator.py` script in combination with a `config.json` file will generate data for the backend APIs that are found in each of the stage folders. The `config.json` file will tell how many days worth of data needs to be generated along with how many orders and how big they are. This is done for each tenant.

Since the same generated data is used by each backend stage, this script only needs to be ran one time. It has no external dependencies and has been tested with Python 3.10+.

This script will generate an `orders` directory filled with order information for many tenants. The different backend stages have an `importer.py` script that they use to convert this data into the format that their respective stage needs.

## Conclusion

I hope to learn more about scaling and what it takes to "move the needle" for clients with large-scale needs. I want to publish this repository so others can see what has been done and decide for themselves whether a "slow technology" is the issue preventing scaling or if the problem lies elsewhere.

I aim to start a conversation about what that "something else" might be.
