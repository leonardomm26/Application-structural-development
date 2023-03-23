class Address(object):
    """
    Class to represent an address
    """

    def __init__(self, department: str = "Department", city: str = "City", neighborhood: str = "Neighborhood",
                 information: str = "Address Information", detail="Address Detail"):
        """Address constructor object.
        :param department: department of the address.
        :type department: str
        :param city: city of the address.
        :type city: str
        :param neighborhood: neighborhood of the address.
        :type neighborhood: str
        :param information: specifications of the address like street or avenue
        :type information: str
        :param detail: extra information of the address.
        :type detail: str
        """
        self.__department = department
        self.__city = city
        self.__neighborhood = neighborhood
        self.__information = information
        self.__detail = detail

    @property
    def department(self) -> str:
        """Returns department of the address.
        :returns: department of address.
        :rtype: str
        """
        return self.__department

    @department.setter
    def department(self, department: str):
        """The department of the address.
        :param department: department of address.
        :type: str
        """
        self.__department = department

    @property
    def city(self) -> str:
        """Returns the city of the address.
        :returns: city of address.
        :rtype: str
        """
        return self.__city

    @city.setter
    def city(self, city: str):
        """The city of the address.
        :param city: city of address.
        :type: str
        """
        self.__city = city

    @property
    def neighborhood(self) -> str:
        """Returns the neighborhood of the address
        :returns: neighborhood of address
        :rtype: str
        """
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str):
        """The neighborhood of the address
        :param neighborhood: neighborhood of address
        :type: str
        """
        self.__neighborhood = neighborhood

    @property
    def information(self) -> str:
        """Returns the information (specifications) of the address.
        :returns: information of address
        :rtype: str
        """
        return self.__information

    @information.setter
    def information(self, information: str):
        """The information (specifications) of the address.
        :param information: information of address.
        :type: str
        """
        self.__information = information

    @property
    def detail(self) -> str:
        """Returns details (more information) of the address.
        :returns: detail of address.
        :rtype: str
        """
        return self.__detail

    @detail.setter
    def detail(self, detail: str):
        """The detail (more information) of the address.
        :param detail: detail of address.
        :types: str
        """
        self.__detail = detail

    def __str__(self):
        """Returns str of address.
        :returns: string with address information.
        :returns: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.__department, self.__city, self.__neighborhood, self.__information, self.__detail)

    def __eq__(self, other: object):
        """Returns te true value of equality of two address.
        :param other:An Address object to compare
        :type: object
        :returns: True or False
        :rtype: bool
        """
        if not isinstance(other, Address):
            return False

        return self.__department == other.__department and self.__city == other.__city \
            and self.__neighborhood == other.__neighborhood and self.__information == other.__information \
            and self.__detail == other.__detail
