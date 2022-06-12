<h1>Elliptic Bitcoin Classification Project</h1>
<n>SwissAI Hackathon by Deep Learning Labs</b>
<hr></hr>
This repository contains project files for SwissAI Hackathon organized by Deep Learning Labs.

<h3>Deployed App</h3>
<a href="https://share.streamlit.io/alihussainia/swissai/main">Link</a>

<h3>Data: Elliptic Data Set</h3>
The Elliptic Dataset is a graph network of Bitcoin transactions with handcrafted features. All features are constructed using only publicly available information.

The <a href="https://www.groundai.com/project/anti-money-laundering-in-bitcoin-experimenting-with-graph-convolutional-networks-for-financial-forensics/1">Elliptic DataSet</a> maps Bitcoin transactions to real entities in two categories:

Legal: exchanges, wallet providers, miners, licit services, etc.
Ilicit: scams, malware, terrorist, organization, ransomware, Ponzi shcemes, etc

A given transaction is licit/legal if the entity that generated it was licit.

There are fewer ilicit (Class 0) transactions than the licit ones. (Class 1).

Features Each node has associated 166 features. 94 represent local information (timestep, number of inputs/outputs, transaction fee, output volume and aggregated figures) and 72 features represent aggregated features (obtained by aggregating transaction information such as maximum, minimum, standard deviation, correlation coefficients of neighbor transactions).

Temporal Information A time step is associated with each node, representing an stimated of the time when the transaction is confirmed. There are 49 distinct timesteps evenly spaced with an interval of 2 weeks.
