from src.models import Apartment
from src.manager import Manager
from src.models import Parameters
def test_manager_loads_all_tenants():
    parameters = Parameters()
    manager = Manager(parameters)
    
    expected_names = [
        "Jan Nowak",
        "Adam Kowalski",
        "Ewa Adamska"
    ]
    assert len(manager.tenants) > 0, "Słownik najemców jest pusty, upewnij się, że plik JSON zawiera dane."
    
    for tenant_key, tenant in manager.tenants.items():
        assert tenant.name in expected_names, f"Najemca {tenant.name} nie znajduje się na liście oczekiwanych najemców!"

def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key
