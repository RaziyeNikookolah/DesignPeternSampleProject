from generate_report_task import GenerateReport
from transfer_money_task import TransferMoney


if __name__ == "__main__":
    task = GenerateReport()
    task.execut()
    task = TransferMoney()
    task.execut()
