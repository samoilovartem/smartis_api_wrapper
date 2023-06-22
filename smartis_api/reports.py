from smartis_api.api import SmartisAPI


class ReportsAPI(SmartisAPI):
    """
    ReportsAPI is a subclass of SmartisAPI that provides methods specifically for handling reports in the Smartis API.
    """

    def get_report(self, report_data: dict[str, any]) -> dict[str, any]:
        """
        Get a report from the API.

        Parameters:
        report_data (dict): The data required to get the report.

        Returns:
        dict: The report from the API as a dictionary.
        """
        get_report_endpoint = 'reports/getReport'
        response = self.make_request(get_report_endpoint, data=report_data)
        return response

    def get_all_reports(self):
        """
        Get all reports from the API. This method is yet to be implemented.
        """
        # TODO: implement this method
        pass
