import os, sys
from signLanguage.components import data_ingestion
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion

# NOTE: without () w.r.t bappy
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig() # Why we need it? To input url into data_ingestion method?

    # method to start downloading then extracting input data, that output data will be stored in artifacts folder feature store
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("bla bla bla")
            logging.info("Getting data from URL")
        
            # Running Dataingestion contructor
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config 
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("")
            logging.info("Exited the start_data_ingestion method in TrainPipeline class")

            return data_ingestion_artifact
        
        except Exception as e:
            raise SignException(e, sys)
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise SignException(e, sys)
        
    
    

    