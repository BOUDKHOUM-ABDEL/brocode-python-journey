
def get_phone_number( country_code , area_code, first_code , last_code):

    
    phone_number = f"{country_code}-{area_code}-{first_code}-{last_code}"
    return phone_number

print(get_phone_number(1, 234, 567, 8901))  # Positional arguments
print(get_phone_number(country_code=1, area_code=234, first_code=567, last_code=8901))  # Keyword arguments
print(get_phone_number(area_code=234, last_code=8901, country_code=1, first_code=567))  # Keyword arguments in different order
 
