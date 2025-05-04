# scaled
Thoughts and ideas on how to scale

## Intention

I have had created and maintained systems to work for clients of various sizes. Some clients ran a few hundred orders a day others a few hundred a minute at a single facility.

Scaling for a few hundred clients a day is very easy. Often times I didn't have to tune or modify anything.

Scaling for customers that ran a few hundred orders in a minute is a very different issue. Consider a client that has multiple fulfillment warehouses and needs to process shipments to go out the door. This customer needs to ship hundreds of orders in the a minute. There will be multiple systems that need to talk to each other. A warehouse execution system that needs information from the warehouse management system. Both of these systems will probably be composed of or use 3rd party systems to simple things like:

- Determining the quickest pick path for a collection of cartons.
- Determining which fulfillment center has the inventory so the customer can get their order in the agreed upon time.
- If an order needs to be split between warehouses, can we the grouped items ship in a single carton (for example shipping a bowling ball and something glass from the same fulfillment center still requires 2 cartons).
- What is the cheapest shipping method that will get to the customer in the agreed upon time.
- A reporting system that has metrics of all of these items or just a specialized vertical slice.

While I have worked on the above problems and many others with logistics software, I will be focusing on the last item because it easily demonstrates scaling issues. This repository will generate order data for multiple clients and then show in stages with examples how things can be scaled. The plan is to use both PostGRES and MongoDB to show that both can be scaled for reporting using different techniques. Often times developers focus on technology to scale, I argue that scaling can be accomplished with what you currently have.

Some solutions are quick fixes, some require more work and rework. Sometimes a temporary solution is all that we can do while things must be reworked or redone.

**The process is just as important as the solution.**

## Technology

### Backend Language

I will be starting out with technology that is purposely labeled as slow. I will be using Python as a backend because people give it a reputation for being slow with reporting technology. I argue that our database calls and the way we organize our data will be more important than the backend technology. Each backend call will include timing for how long a request took and how long the database calls took. Both will be important to determine if Python is truly the bottleneck or if it is something else.

### Database Layer

For reporting software, I have been told many times that a SQL solution does not scale well. I think this needs to be put to the test. I will start with PostGRES to get a baseline of where we are at. From there I will also include a MongoDB backend. I want to compare both to see if the technology is truly the issue or if it is something else.

### Other Technology

I plan on using React to display the data in charts and graphs. I am not sure what library I will be using.

Each stage will have a docker compose file so that others can validate or dispute my results.

## Layout

I think there will be an overall readme file that is used to explain each step and what I am thinking at that stage or scaling the reporting system. Each stage will have its own code to show how changes affected the speed and memory usage of the reporting system. I will also be including the steps to reproduce the data that I am using at each step, that way even though numbers may be different between machines the magnitude of a change will be consistent.

Each stage will be in a stages folder. All files for that stage will be included within that folder.

## Original Data

The `postal.csv` file is from an excel file called `ZIP_Locale_Detail.xls` that I downloaded from the census department. I removed all postal codes exception those for the 50 states.

## Conclusion

I hope to learn more about scaling and what it takes to move the needle for clients that have large needs. I want to publish this repository so that others can see what has been done and then decide for themselves if a "slow technology" is the issue that is preventing the scaling or if it is something else.

I am trying to start a conversation on what the something else is.
