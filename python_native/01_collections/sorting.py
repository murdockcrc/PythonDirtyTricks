# Sorting

## Sorting with keys

airports = [
    ('MROC', 'San Jose, CR'),
    ('KLAS', 'Las Vegas, USA'),
    ('EDDM', 'Munich, DE'),
    ('LSZH', 'Zurich, CH'),
    ('VNLK', 'Lukla, NEP')
]

sorted_airports = dict(sorted(airports, key=lambda x:x[0]))

print(sorted_airports)