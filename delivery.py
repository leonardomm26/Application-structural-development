from person import Person
from address import Address
from package import Package
from typing import List


class Delivery(object):
    """
    Class used to represent a Delivery
    """

    def __init__(self, id_delivery: int = 0, date: str = "01-01-1900", time: int = 0, sender: Person = Person(),
                 receiver: Person = Person(), sender_address: Address = Address(),
                 receiver_address: Address = Address(), contact: Person = Person(), items: List[Package] = None):
        """ Delivery constructor object.
        :param id_delivery: id of the delivery.
        :type id_delivery: int
        :param date: date of the delivery.
        :type date: str
        :param time: time of the delivery.
        :type time: int
        :param sender: who send the delivery.
        :type sender: Person object
        :param receiver: who will receive the delivery.
        :type receiver: Person object
        :param sender_address: address of person that send the delivery.
        :type sender_address: Address object
        :param receiver_address: Address of person that receive the delivery.
        :type receiver_address: Address object
        :param contact: different person that will can receive the delivery.
        :type contact: Person object
        :param items: list of packages to send in the delivery.
        :type items: List[Package object]
        """

        self.__id_delivery = id_delivery
        self.__date = date
        self.__time = time
        self.__sender = sender
        self.__receiver = receiver
        self.__sender_address = sender_address
        self.__receiver_address = receiver_address
        self.__contact = contact
        self.__items = items if items is not None else []

    @property
    def id_delivery(self) -> int:
        """ Returns id_delivery of the delivery
        :returns: id of delivery.
        :rtype: int
        """
        return self.__id_delivery
    
    @id_delivery.setter
    def id_delivery(self, id_delivery: int):
        """The id of the delivery.
        :param id_delivery: id of delivery.
        :type: int
        """
        self.__id_delivery = id_delivery
    
    @property
    def date(self) -> str:
        """Returns date of the delivery.
        :returns: date of delivery.
        :rtype: str 
        """
        return self.__date
    
    @date.setter
    def date(self, date: str):
        """The date of the delivery.
        :param date: date of delivery.
        :type: str
        """
        self.__date = date

    @property
    def time(self) -> int:
        """Returns time of the delivery.
        :returns: time of delivery.
        :rtype: int
        """
        return self.__time

    @time.setter
    def time(self, time: int):
        """The time of the delivery.
        :param time: time of delivery.
        :type: int
        """
        self.__time = time

    @property
    def sender(self) -> Person:
        """Returns the person that send delivery.
        :returns: person that send delivery.
        :rtype: Person
        """
        return self.__sender

    @sender.setter
    def sender(self, sender: Person()):
        """Who send the delivery.
        :param sender: person that send delivery.
        :type: Person object
        """
        self.__sender = sender

    @property
    def receiver(self) -> Person:
        """Returns the person that receive delivery.
        :returns: person that receive delivery.
        :rtype: Person object
        """
        return self.__receiver

    @receiver.setter
    def receiver(self, receiver: Person()):
        """Who receive the delivery.
        :param receiver: person that receive delivery.
        :type: Person object
        """
        self.__receiver = receiver

    @property
    def sender_address(self) -> Address:
        """Returns address of person that send delivery.
        :returns: address of person
        :rtype: Address object
        """
        return self.__sender_address

    @sender_address.setter
    def sender_address(self, sender_address: Address()):
        """The address that who send delivery.
        :param sender_address: address of person that send delivery.
        :type: Address object
        """
        self.__sender_address = sender_address

    @property
    def receiver_address(self) -> Address:
        """Returns address of person that receive delivery.
        :returns: address of person.
        :rtype: Address object
        """
        return self.__receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address: Address()):
        """The address that who receive delivery.
        :param receiver_address: address of person.
        :type: Address object
        """
        self.__sender_address = receiver_address

    @property
    def contact(self) -> Person:
        """Returns person registered like contact.
        :returns: person registered like contact.
        :rtype: Person object
        """
        return self.__contact

    @contact.setter
    def contact(self, contact: Person()):
        """Person registered like contact.
        :param contact: person who will be the contact.
        :type: Person object
        """
        self.__contact = contact

    @property
    def items(self) -> List[Package]:
        """Returns list of package for delivery.
        :returns: list of package.
        :rtype: List[Package object]
        """
        return self.__items

    @items.setter
    def items(self, items: list):
        """A list with package of delivery.
        :param items: list of packages for delivery.
        :type: List[Package object]
        """
        self.__items = items

    def __str__(self):
        """Returns str of delivery
        :returns: str delivery
        :rtype: str
        """
        return '({0},\n {1},\n {2},\n {3},\n {4},\n {5},\n {6},\n {7},\n {8})'.format(
            self.__id_delivery, self.__date, self.__time, self.__sender, self.__receiver, self.__sender_address,
            self.__receiver_address, self.__contact, self.__items)

    def __eq__(self, other: object):
        """Returns the true value of equality of two deliveries.
        :param other: delivery to compare.
        :type: object
        :returns: True or False.
        :rtype: bool
        """
        if not isinstance(other, Delivery):
            return False
        return self.__id_delivery == other.__id_delivery and self.__date == other.__date and \
            self.__time == other.__time and self.__sender == other.__sender and \
            self.__receiver == other.__receiver and self.__sender_address == other.__sender_address and \
            self.__receiver_address == other.__receiver_address and self.__contact == other.__contact and \
            self.__items == other.__items
