class Package(object):
    """
    Class used to represent a Package
    """

    WGR_100 = 1

    def __init__(self, id_package: int = 0, weight: float = 1.0, description: str = "Description",
                 cost: float = 1.0):
        """Package constructor object
        :param id_package: id of the package.
        :type id_package: int
        :param weight: weight of the package.
        :type weight: float
        :param description: description of the package.
        :type description: str
        :param cost: cost of the package.
        :type cost: float
        """
        self.__id_package = id_package
        self.__weight = weight
        self.__description = description
        self.__cost = cost

    @property
    def id_package(self) -> int:
        """Returns id_package of the package.
        :returns: id of package.
        :rtype: int
        """
        return self.__id_package

    @id_package.setter
    def id_package(self, id_package: int):
        """The id of the package.
        :param id_package: id of package.
        :type: int
        """
        self.__id_package = id_package

    @property
    def weight(self) -> float:
        """Returns weight of the package.
        :returns: weight of package.
        :rtype: float
        """
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        """The weight of the package.
        :param weight: weight of package.
        :type weight: int
        """
        self.__weight = weight

    @property
    def description(self) -> str:
        """Returns description of the package.
        :returns: description of package.
        :rtype: str
        """
        return self.__description

    @description.setter
    def description(self, description: str):
        """The description of the package.
        :param description: description of package.
        :type: str
        """
        self.__description = description

    @property
    def cost(self) -> float:
        """Returns the cost of the cost.
        :returns: cost of package.
        :rtype: float
        """
        return self.__cost

    @cost.setter
    def cost(self, cost: float):
        """The cost of the package.
        :param cost: cost of package.
        :type: float
        """
        self.__cost = cost

    def calculate(self) -> float:
        """Returns the total cost of the package
        """
        pass

    def __str__(self):
        """Returns str of package.
        :returns: string with package information.
        :rtype: str
        """
        return '({0}, {1}, {2}, {3})'.format(self.__id_package, self.__weight, self.__description, self.__cost)

    def __eq__(self, other: object):
        """Returns the true value of equality of two packages.
        :param other: package for do it comparative.
        :type: object
        :returns: True or False.
        :rtype: bool
        """
        if not isinstance(other, Package):
            return False
        return self.__id_package == other.__id_package and self.__weight == other.__weight and self.__cost == other.__cost \
            and self.__description == other.__description


class StandardPackage(Package):
    """
    Class used to represent Standard Package.
    """

    def calculate(self) -> float:
        """Returns the total cost for StandardPackage.
        :returns: weight * cost * WGR_100
        :rtype: float
        """
        return self.__cost * self.__weight * self.WGR_100


class OverWeightPackage(Package):
    """
    Class used to represent Over Weight Package.
    """

    def __init__(self, id_package: int = 0, weight: float = 1.0, description: str = "Description",
                 cost: float = 1.0, overweight: float = 1.0):
        """OverWeightPackage constructor object.
        :param overweight: cost for extra weight of package.
        :type: float
        """
        super().__init__(id_package, weight, description, cost)
        self.__overweight = overweight

    @property
    def overweight(self) -> float:
        """Returns cost for the extra weight of package.
        :returns: overweight of OverWeightPackage.
        :rtype: float
        """
        return self.__overweight

    @overweight.setter
    def overweight(self, overweight: float):
        """The cost for extra weight of package.
        :param overweight: overweight of OverWeightPackage
        :type: float
        """
        self.__overweight = overweight

    def calculate(self) -> float:
        """Returns the total cost for OverWeightPackage.
        :returns: weight * cost * WGR_100 * overweight
        :rtype: float
        """
        return self.weight * self.cost * self.WGR_100 * self.__overweight

    def __str__(self):
        """Returns str of OverWeightPackage
        :returns: string with OverWeightPackage
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_package, self.weight, self.description, self.cost,
                                                  self.__overweight)

    def __eq__(self, other: object):
        """Returns the true value of equality of two OverWeightPackage
        :param other:An OverWeightPackage object to compare.
        :type: object
        :returns: True or False.
        :rtype: bool
        """
        if not super().__eq__(other):
            return False
        if not isinstance(other, OverWeightPackage):
            return False
        return self.__overweight == other.__overweight
