"""Unit 1 discussion: inheritance, namespaces, and copying."""

from copy import copy, deepcopy


# TODO 1: Create a parent class.
# Includes a class variable, instance variables, constructor, and display method.
class ParentClass:
    device_category = "Network Device"

    def __init__(self, hostname: str, ip_address: str):
        if not hostname or not hostname.strip():
            raise ValueError("Hostname cannot be empty")
        if not ip_address or not ip_address.strip():
            raise ValueError("IP address cannot be empty")
        self.hostname = hostname
        self.ip_address = ip_address

    def display_info(self):
        return f"Device: {self.hostname}, IP: {self.ip_address}"

    def __str__(self):
        return self.display_info()


# TODO 2: Create a child class that inherits from the parent class.
# Adds a class variable, two instance variables, a method, and an override.
class ChildClass(ParentClass):
    vendor = "Dell"

    def __init__(self, hostname: str, ip_address: str, location: str, ports=None):
        super().__init__(hostname, ip_address)
        self.location = location
        # A new list is created for each switch to avoid sharing mutable data.
        self.ports = deepcopy(ports) if ports is not None else []

    def add_port(self, port_number: int, vlan: int):
        if port_number <= 0 or vlan < 1 or vlan > 4094:
            raise ValueError("Port must be positive and VLAN must be 1 through 4094")
        if any(port["number"] == port_number for port in self.ports):
            raise ValueError(f"Port {port_number} already exists")
        self.ports.append({"number": port_number, "settings": {"vlan": vlan}})

    def display_info(self):
        return (f"{super().display_info()}, Vendor: {type(self).vendor}, "
                f"Location: {self.location}, Ports: {self.ports}")


def demonstrate_namespaces():
    # TODO 3: Demonstrate class namespaces and instance namespaces.
    print("\n=== Namespace Demonstration ===")
    switch_a = ChildClass("SW-A", "10.0.0.10", "Server room")
    switch_b = ChildClass("SW-B", "10.0.0.11", "Office")
    print("Class variable through class:", ChildClass.vendor)
    print("Class variable through object:", switch_a.vendor)
    switch_a.maintenance_ticket = "INC-104"
    print("Switch A instance namespace:", switch_a.__dict__)
    print("Switch B instance namespace:", switch_b.__dict__)
    print("Child class namespace keys:", sorted(ChildClass.__dict__.keys()))
    print("Ticket exists only on A:", hasattr(switch_a, "maintenance_ticket"),
          hasattr(switch_b, "maintenance_ticket"))


def demonstrate_copying():
    # TODO 4: Demonstrate shallow and deep copying with nested mutable data.
    print("\n=== Copy Demonstration ===")
    original = ChildClass("SW-C", "10.0.0.12", "Lab")
    original.add_port(1, 32)
    shallow = copy(original)
    deep = deepcopy(original)

    # A shallow copy shares the nested ports list with the original.
    # A deep copy creates independent nested lists and dictionaries.
    original.ports[0]["settings"]["vlan"] = 35
    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)
    assert shallow.ports[0]["settings"]["vlan"] == 35
    assert deep.ports[0]["settings"]["vlan"] == 32


def main():
    # TODO 5: Create and test parent and child objects and run demonstrations.
    print("=== Unit 1 OOP Assignment ===")
    device = ParentClass("Gateway", "10.0.0.1")
    print("\nParent object:", device.display_info())

    switch = ChildClass("Core-SW", "10.0.0.2", "Data center")
    switch.add_port(1, 32)
    switch.add_port(2, 40)
    print("Child object:", switch.display_info())
    print("Inherited category:", switch.device_category)

    # TODO 6: Student-created extension: input checks and independent switch ports.
    empty_switch = ChildClass("Spare-SW", "10.0.0.3", "Storage")
    print("Empty switch ports:", empty_switch.ports)
    assert empty_switch.ports == []
    assert switch.ports != empty_switch.ports
    for bad_port, bad_vlan in [(0, 32), (3, 5000), (1, 32)]:
        try:
            switch.add_port(bad_port, bad_vlan)
        except ValueError as error:
            print("Handled invalid port configuration:", error)
    assert len(switch.ports) == 2

    demonstrate_namespaces()
    demonstrate_copying()
    print("\nAll demonstration checks passed.")


if __name__ == "__main__":
    main()
