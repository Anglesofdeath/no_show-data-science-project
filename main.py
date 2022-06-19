import logging

from src.data_processing import DataProcessing
from src.model import Model


def main():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Running machine learning pipeline")

    data_processor = DataProcessing()

    logger.info("Data Processing Complete")
    
    clean_data = data_processor.clean_data()
    logger.info("Clean_data complete")
    modeling = Model(clean_data)
    modeling.build_model()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter