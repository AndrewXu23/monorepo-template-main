class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.messages = []  # Initialize messages list in the created instance
            print("Logger created exactly once")
        else:
            print("logger already created")
        return cls._instance

    def add_message(self, message):
        self.messages.append(message)


def main():
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
