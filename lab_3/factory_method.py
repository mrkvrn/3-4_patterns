from abc import ABC, abstractmethod

class LoggingSystem(ABC):
    @abstractmethod
    def record_message(self, text):
        pass

class DiskLogger(LoggingSystem):
    def record_message(self, text):
        print(f"Запись в файловый журнал: {text}")

class TerminalLogger(LoggingSystem):
    def record_message(self, text):
        print(f"Вывод в терминал: {text}")


class LoggerCreator(ABC):
    @abstractmethod
    def produce_logger(self):
        pass

class DiskLoggerCreator(LoggerCreator):
    def produce_logger(self):
        return DiskLogger()

class TerminalLoggerCreator(LoggerCreator):
    def produce_logger(self):
        return TerminalLogger()

# Тестирование
print("\n Factory Method Test")
disk_factory = DiskLoggerCreator()
terminal_factory = TerminalLoggerCreator()

disk_logger = disk_factory.produce_logger()
terminal_logger = terminal_factory.produce_logger()

disk_logger.record_message("ERROR 404")
terminal_logger.record_message("Приложение успешно инициализировано")
