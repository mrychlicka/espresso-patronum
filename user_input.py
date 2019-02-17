from termcolor import cprint
from pyfiglet import figlet_format


class UserInput:
    """ Class represents user input """

    def get_coffee_type(self, hideASCII=False, hideDebugPrint=False):
        """
        Take user choice - which coffee drink wants to be done
        @hideASCII: boolean - if True ascii drawings is not shown, if False it is
        @hideDebugPrint: boolean - if True printed text is not shown, if False it is
        Returns typed coffee type, False if user input is wrong
        """
        for i in xrange(2):
            drink_number = raw_input("Pick coffe drink or turn off coffee machine - type \'1\' for espresso, \n"
                                     "\'2\' - cappuccino, \'3\' - latte macchiato or "
                                     "\'exit\' to turn off coffee machine: ")

            drinks = {"1": "espresso",
                      "2": "capuccino",
                      "3": "latte macchiato"}

            for key in drinks:
                if drink_number == key:
                    drink_type = drinks[key]
                    return drink_type

            if drink_number == "exit":
                if not hideASCII:
                    cprint(figlet_format("TURNED OFF", font="standard"), "white")
                if not hideDebugPrint:
                    print "Coffee machine turned off"
                exit(0)
            else:
                if i == 0:
                    print "Wrong input. Try again"
                else:
                    print "Wrong input. Coffee drink cannot be done"
                    exit(0)
        return False

    def get_coffee_strength(self):
        """
        Take user choice - coffee strength
        Returns typed coffee strength, False if user input is wrong
        """
        for i in xrange(2):
            coffee_strength_number = raw_input("Pick coffee strength - type \' 1\' if you want weak coffee, "
                                               "\'2\' for normal or \'3\' for strong coffee: ")
            if coffee_strength_number == "1":
                coffee_strength = 3
                return coffee_strength
            if coffee_strength_number == "2":
                coffee_strength = 5
                return coffee_strength
            if coffee_strength_number == "3":
                coffee_strength = 7
                return coffee_strength
            else:
                if i == 0:
                    print "Wrong input. Try again"
                else:
                    print "Wrong input. Coffee drink cannot be made"
                    exit(0)
        return False