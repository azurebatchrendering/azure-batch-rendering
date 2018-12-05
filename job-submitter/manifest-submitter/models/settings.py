
class TemplateSettings(object):
    """
    Self contained template settings class. Holds paths to the JSON tempaltes 
    and the parameter mapper python module.
    """
    def __init__(self,
        job_template_file_path: str, job_parameter_file_path: str, parameter_mapper_file_path: str,
        mapper_module_name: str):
        """
        :param `str` job_template_file_path: 
            Path on disk to the job template JSON file.
        :param `str` job_parameter_file_path:
            Path on disk to the job template parameter JSON file.
        :param `str` parameter_mapper_file_path: 
            Path on disk to the Python module that maps the parameter settings from 
            the manifest job definition to the job.parameter.json object.    
        :param `str` mapper_module_name:
            Name of the parameter mapper module name. This is gererally the name of 
            the file without the file extension.
        """
        self.job_template_file_path = job_template_file_path
        self.job_parameter_file_path = job_parameter_file_path
        self.parameter_mapper_file_path = parameter_mapper_file_path
        self.mapper_module_name = mapper_module_name
