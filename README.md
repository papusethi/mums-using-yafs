# Multi User Multi Server Task Offloading in Mobile Edge Computing

## Requirements
- You have to import YAFS simulator in your system to simulate the scenario.
- We are using PyCharm to run this project.

## 1. Clustering of WD using K-Means Algorithm
- Firstly, we are generating a CSV file which has the X coordinate and Y coordinate of Wireless Devices's. As we are assuming that the WD's are scattered in a location.
- Secondly, we are using the Elbow Method to choose the optimal number of clusters required.
- Lastly, we are providing the CSV file of WD to the K-Means algorithm, and it generates a nice scatter graph which represents the clusters with different colors.

## 2. Offloading Decision Making using Fuzzy Logic
- To make the offloading decision of WD's, we are using the Fuzzy Logic algorithm.
- Task size, Network Bandwidth and Delay are considered in the Antacedant part and for the Consequent part we are taking the decision.
- For the fuzzification we are taking the three scales like Small, Medium and Large.
- After comutation we are getting a defuzzifed value, and then we are comparing that value with a Threshold hold value which is predefinded by us.
- Based on that comparision we are taking the decision whether to offload the task to the Mobile Edge Computing server or locally execute that task.

## 3. Simulation in YAFS
- As we have taken the decision to make the offloading for a particular device. Then the scenario becomes one to one (meaning One WD who wants to offload the task and One MEC Sever who will compute the task).
- Change the parameters like Cloud device Hardware configuration and Source and Destin device Hardware configuration.
- Also you can change the simulation time based on you requirements.
- Now analyze the outputs that you are getting in the form of CSV files which is located at the results directory of the same file hierarchy.

---: So this is the project that we have done in our academic minor project session. :---

Last but not the least, I would like to Thank to all my team members and our mentor for their guidance and support.

Thank you and Regrads.
Enjou your day and have fun.
