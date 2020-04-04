from HashTable import HashTable



def quiz_dictionaries():
    print("## quiz dicts##")
    locations = {'North America': {'USA': ['Mountain View']}}
    locations['Asia'] = {'India': 'Bangalore'}
    locations['North America']['USA'].append('Atlanta')
    locations['Africa'] = {'Egypt': 'Cairo'}
    locations['Asia']['China'] = 'Shanghai'

    #print(locations)

    ## all usa cities
    print("1")
    cities = locations['North America']['USA']

    for e in sorted(cities):
        print(e)

    # all asian country cities
    print("2")
    sorted_by_value = sorted((v,k) for (k,v) in locations['Asia'].items())
    for key, value in sorted_by_value:
        print("{0} - {1}".format(key,value))


def quiz_hash_table_naive():
    print("## quiz string keys practice")
    ht = HashTable()
    print(ht._calculate_hash_value('UDACITY'))
    'UACITY not yet stored'
    print(ht.lookup('UDACITY'))
    #test store
    ht.store('UDACITY')
    'UDACITY is stored should be looked up'
    print('expect hash of 8658 returned')
    print(ht.lookup('UDACITY'))
    #test store edge case  (expect lookup to not return hash, from non stored string)
    print('expect no hash returned')
    print(ht.lookup('UDACIOUS'))
    ht.store('UDACIOUS')
    #expect hash to be returned
    print(ht.lookup('UDACIOUS'))


#---------------------------------------------------------------------#
def main():
    quiz_dictionaries()
    quiz_hash_table_naive()

if __name__ == '__main__':
        main()