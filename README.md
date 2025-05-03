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
