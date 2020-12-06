passports = []

new_entry = True
for line in open('input.txt', 'r').read().split('\n')[:-1]:
    if line == '':
        new_entry = True
        continue
    if new_entry:
        passports.append(line.split(' '))
        new_entry = False
    else:
        passports[-1].extend(line.split(' '))

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
valid_passports = 0
for passport in passports:
    fields_found = []
    for entry in passport:
        fields_found.append(entry.split(':')[0])
    fields_found = set(fields_found)
    if len(required_fields - fields_found) == 0:
        valid_passports += 1

print(f'valid passports = {valid_passports}')
