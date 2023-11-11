
class ProcessingDna():
    # Создаем индивидуальный пакет свойств для конкретного запроса
    def __init__(self, dna: str, features_client):
        self.dna = dna
        self.features_client = features_client
        self.features = {
            'length': 'Не указано',
            'cg_count': 'Не указано',
            'molecular_weight': 'Не указано',
            'count_nuc': 'Не указано',
        }

    # Расчет длины ДНК
    def count_len_dna(self):
        self.features['length'] = str(len(self.dna))

    # Расчет % CG нуклеотидов
    def count_cg(self):
        count = 0
        for i in range(len(self.dna) - 1): #Так как индексы начинаются с 0, а минимальная длина с 1
            if self.dna[i:i+2] == 'CG': #Не включительно +2
                count += 1
        percent_cg = count*2/len(self.dna)
        formatted_average = "{:.1f}".format(percent_cg)  # указываем кол-во знаков после запятой({:.1f}) для более красивого вывода
        self.features['cg_count'] = formatted_average

    # Расчет молекулярного веса ДНК
    def count_molec_weight(self):
        weight = 0
        for i in self.dna:
            if i == 'T' or i == 'C':
                weight += 1
            elif i == 'A' or i == 'T':
                weight += 2
        self.features['molecular_weight'] = str(weight)
        self.features['count_nuc'] = str(52)

    # Выбор исполняемых функций в зависимости от выбранных свойств
    def performing_functions(self):
        features_handlers_vocab = {
            'length': self.count_len_dna,
            'cg_count': self.count_cg,
            'molecular_weight': self.count_molec_weight,
        }
        #Сравниваем запрашиваемые свойства с атрибутами словаря выбора функции, если ключи равны, то выполняется функция для подсчета конкретного свойства
        for el, function in features_handlers_vocab.items():
            if el in self.features_client:
                function()

        return self.features