# Project Details

This repository contains code to analyze Apache server logs to find the most visited website using Apache Hadoop's Pig script extended using Python's User-defined Functions (UDF). It was run on an Ubuntu instance deployed on the Oracle's VMware with the help of Vagrant.

# Contents

- *shareFiles/pig_script .py* contains code to compute the page hits and store them.
- *shareFiles/script .py* contains the Python UDF to parse the sample Apache logs.
- *shareFiles/sample_log* contains the sample logs on which the scripts are run.