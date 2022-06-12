<h1>Elliptic Bitcoin Classification Project</h1>
<n>SwissAI Hackathon by Deep Learning Labs</b>
<hr></hr>
This repository contains project files for SwissAI Hackathon organized by Deep Learning Labs.

<h3>Deployed App</h3> 
<a href="https://share.streamlit.io/alihussainia/swissai/main">Link</a>

<h3>Data: Elliptic Data Set</h3>

The Elliptic Dataset is a graph network of Bitcoin transactions with handcrafted features. All features are constructed using only publicly available information.

The <a href="https://www.kaggle.com/datasets/ellipticco/elliptic-data-set">Elliptic DataSet</a> maps Bitcoin transactions to real entities in two categories:

licit: exchanges, wallet providers, miners, licit services, etc.

Ilicit: scams, malware, terrorist, organization, ransomware, Ponzi shcemes, etc

A given transaction is licit/legal if the entity that generated it was licit.

There are fewer ilicit (Class 0) transactions than the licit ones. (Class 1) with:

<b>Features</b>: Each node has associated 166 features. 94 represent local information (timestep, number of inputs/outputs, transaction fee, output volume and aggregated figures) and 72 features represent aggregated features (obtained by aggregating transaction information such as maximum, minimum, standard deviation, correlation coefficients of neighbor transactions).

<b>Temporal Information</b> A time step is associated with each node, representing an stimated of the time when the transaction is confirmed. There are 49 distinct timesteps evenly spaced with an interval of 2 weeks.

References:
[1] Elliptic, www.elliptic.co.

[2] M. Weber, G. Domeniconi, J. Chen, D. K. I. Weidele, C. Bellei, T. Robinson, C. E. Leiserson, "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics", KDD ’19 Workshop on Anomaly Detection in Finance, August 2019, Anchorage, AK, USA.
