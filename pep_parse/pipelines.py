import csv
import datetime as dt

from . settings import BASE_DIR, RESULTS_DIR, DATETIME_FORMAT


class PepParsePipeline:
    """
    Обрабатывает каждый из item-объектов для PEP.
    Считает кол-во PEP по каждому статусу
    и записывает итоговый результат в csv файл.
    """

    def open_spider(self, spider):
        """Создает словарь для подсчета PEP."""
        self.status_counter = {}

    def process_item(self, item, spider):
        """
        Считает кол-во PEP, относящихся к каждому статусу,
        и общее кол-во PEP.
        """
        self.status_counter[item['status']] = self.status_counter.get(
            item['status'], 0) + 1
        self.status_counter['Total'] = self.status_counter.get('Total', 0) + 1
        return item

    def close_spider(self, spider):
        """Записывает итоговый результат в файл."""
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус', 'Количество'])
            total = self.status_counter.pop('Total')
            writer.writerows(sorted(self.status_counter.items()))
            writer.writerow(['Total', total])
