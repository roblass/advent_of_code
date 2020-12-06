# not 113 or 174
import re
import sys

passports = []

new_entry = True
for line in open(sys.argv[1], 'r').read().split('\n')[:-1]:
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
        valid = True
        key, value = entry.split(':')
        try:
            if key == 'byr':
                assert len(value) == 4
                assert int(value) >= 1920
                assert int(value) <= 2002
            elif key == 'iyr':
                assert len(value) == 4
                assert int(value) >= 2010
                assert int(value) <= 2020
            elif key == 'eyr':
                assert len(value) == 4
                assert int(value) >= 2020
                assert int(value) <= 2030
            elif key == 'hgt':
                if value[-2:] == 'cm':
                    assert int(value[:-2]) >= 150
                    assert int(value[:-2]) <= 193
                elif value[-2:] == 'in':
                    assert int(value[:-2]) >= 59
                    assert int(value[:-2]) <= 76
                else:
                    valid = False
            elif key == 'hcl':
                assert re.match(r"^#[0-9a-f]{6}$", value)
            elif key == 'ecl':
                assert value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            elif key == 'pid':
                assert len(value) == 9
                _ = int(value)
        except:
            #print(f'key = {key} is fucked with {value}')
            valid = False
        if valid:
            fields_found.append(key)
    fields_found = set(fields_found)
    if len(required_fields - fields_found) == 0:
        valid_passports += 1
    else:
        print(f'{passport}')

print(f'valid passports = {valid_passports}')
