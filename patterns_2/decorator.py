import abc


class IProcessor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def process(self):
        pass


class Transmitter(IProcessor):
    def __init__(self, data: str):
        self.__data = data

    def process(self):
        print(f"Данные {self.__data} переданы по каналу связи")


class Shell(IProcessor):
    def __init__(self, pr: IProcessor):
        self._processor = pr

    @abc.abstractmethod
    def process(self):
        self._processor.process()


class HammingCoder(Shell):
    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print("Наложен помехоустойчивый код Хэмминга->", end="")
        self._processor.process()


class Encryptor(Shell):
    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print("Шифрование данных->", end="")
        self._processor.process()


if __name__ == "__main__":
    transmitter: IProcessor = Transmitter("12345")
    transmitter.process()
    print("=======")
    hamming_coder: Shell = HammingCoder(transmitter)
    hamming_coder.process()
    print("=======")
    encryptor: Shell = Encryptor(hamming_coder)
    encryptor.process()
