class Calculator:
    def __init__(self, first_prompt="Enter the first number: ", operator_prompt="Enter the operator: ",
                 second_prompt="Enter the second number: ", halt_prompt="Would you like to continue? ",
                 goodbye_msg="Bye!"):
        self.__first_prompt = first_prompt
        self.__operator_prompt = operator_prompt
        self.__second_prompt = second_prompt
        self.__halt_prompt = halt_prompt
        self.__goodbye_msg = goodbye_msg
        self.__num1 = None
        self.__operator = None
        self.__num2 = None
        self.__calculations = []

    @staticmethod
    def get_number(prompt):
        while True:
            try:
                num = input(prompt+" ").strip()
                if num.startswith('.') or num.startswith('-.') or num == '-' or num.startswith('+'):
                    raise ValueError
                num = int(num)
                return float(num)
            except ValueError:
                print("Invalid input. Try to provide a valid number.")

    @staticmethod
    def get_operator(prompt):
        while True:
            operator = input(prompt+" ").strip()
            if operator in ['+', '-', '*', '/']:
                return operator
            else:
                print("You may only enter one of the following operators: + - * /")

    @staticmethod
    def halt(prompt):
        while True:
            response = input(prompt+" ").strip()
            if response in ['y', 'yes', 'Y', 'YES', 'Yes']:
                return True
            elif response in ['n', 'no', 'N', 'NO', 'No']:
                return False
            else:
                print("Invalid response. Please enter [Y|N].")

    def calculate(self):
        self.__num1 = (self.get_number(self.__first_prompt))
        self.__operator = self.get_operator(self.__operator_prompt)
        self.__num2 = (self.get_number(self.__second_prompt))
        result = None

        if self.__operator == '+':
            result = self.__num1 + self.__num2
        elif self.__operator == '-':
            result = self.__num1 - self.__num2
        elif self.__operator == '*':
            result = self.__num1 * self.__num2
        elif self.__operator == '/':
            if self.__num2 == 0:
                print("Error: division by zero")
            else:
                result = self.__num1 / self.__num2

        if result is not None:
            return float(result)

    def run(self):
        while True:
            result = self.calculate()
            self.__calculations.append(result)
            print("{} {} {} = {}".format(int(self.__num1), self.__operator, int(self.__num2), result))

            if not self.halt(self.__halt_prompt):
                break
        if len(self.__calculations) == 1:
            print("You carried out 1 calculation. The result was: {}"
                  .format(self.__calculations[0]))
        else:
            print("You carried out {} calculations. The results were: {}"
                  .format(len(self.__calculations), "; ".join([str(i) for i in self.__calculations])))
        if self.__goodbye_msg:
            print(self.__goodbye_msg)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    myobject = Calculator()
    myobject.run()
    print(myobject.get_number("Enter the number:"))

