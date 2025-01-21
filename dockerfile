#Get the based image we want
FROM rocker/binder:latest

#Set the root user to install packages

USER root

#Add all the content in the current directory to the rstudio

ADD . /home/rstudio/TOPSTSCHOOL-DISASTERS

#Install the required R packages

RUN Rscript -e "install.packages(c('sf', 'stars', 'osmdata', 'aws.s3', 'httr2', 'ncdf4', 'concaveman', 'dbscan', 'dplyr', 'ggplot2', 'tidyterra', 'terra', 'knitr', 'kableExtra', 'units'))"

#copy the privillege and ownership of the folder to the user

RUN chown -R rstudio /home/rstudio/TOPSTSCHOOL-DISASTERS

CMD ["/init"]