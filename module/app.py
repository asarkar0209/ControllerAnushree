"""
This is the implementation of data preparation for sklearn using Xpresso
abstract pipeline component
"""
import os
import sys
from data_prep.app.data_fetch import Modularization

__author__ = "Anushree_Sarkar"


from xpresso.ai.core.data.pipeline.abstract_pipeline_component import \
    AbstractPipelineComponent


class DataPrep(AbstractPipelineComponent):
    """ Implementation of data preparation required for your project.
        DataPrep -> comes by default as your component name, modify as needed.
    """

    def __init__(self,dataset):
        """We can use Modularization class for reading the data, see __main__ for example.
               Declare all class level variable in the constructor.
               e.g - Model, customized dataset etc."""
        # super() contains the name of the component.
        super().__init__(name="DataPrep")
        self.dataset =dataset

        print("Data load completed")



    def start(self, run_name):
        super().start(xpresso_run_name=run_name) #keep it as it is.
        print("Preparing data")
        self.dataset=self.dataset+1
       # Write Code here!
        self.completed()

    def send_metrics(self):
        """  self.report_status() is an AbstractPipelineComponent class method, sends the status to the controller,
               which is saved in database, and can be used later for comparision. It accepts json. """

        report_status = {"status": {"status": "data_preparation"},
                         "metric": {
                             "data_size_x": "send your data",
                             "data_size_y": "send your data"}
                         }
        self.report_status(status=report_status)


    def completed(self, push_exp=True):
        """ After the experiments on your data like cleanup, training model, EDA on data, save your information into a file and """

        output_dir = "/data/kaggle_dataset"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.dataset.to_csv(os.path.join(output_dir,"added1_train.csv"),index=False)
        print("Data saved")
        self.completed(push_exp=True)
#       self.completed() is a parent class method, and arg 'push_exp' if made True, pushes the data into versioning system.


if __name__ == "__main__":
    # XPRESSO_PACKAGE_PATH=$PWD/../xpresso_ai enable_local_execution=true python app/app.py
    #Using Modularization.fetch() to read dataset, we just feed the file path as args.

    dataset= Modularization.fetch(filepaths="data/dataset_name/dataset.csv")
    data_prep = DataPrep(dataset)
    data_prep.start(run_name=sys.argv[1])
