class Report:
    def __init__(self, report_id, title, description):
        self.report_id = report_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {
            "report_id": self.report_id,
            "title": self.title,
            "description": self.description
        }
