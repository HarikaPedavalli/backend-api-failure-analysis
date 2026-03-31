from models import Report

reports = []

def get_all_reports():
    return [report.to_dict() for report in reports]

def create_report(data):
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()

    if not title or not description:
        return {"error": "Title and description are required"}, 400

    report = Report(len(reports) + 1, title, description)
    reports.append(report)
    return report.to_dict(), 201
