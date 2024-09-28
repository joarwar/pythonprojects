import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
rm.list_resources
print(rm.list_opened_resources)
print(rm.list_resources_info)