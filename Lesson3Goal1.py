contacts = {
	'Haynes': {'phone': '123-456-7890',
				'twitter': '@abcdefg',
				'github': 'abcdefg'},

	'Monica': {'phone': '987-654-0321',
				'twitter': '@lmnop',
				'github': 'lmnop'},

	'Emily': {'phone': '555-555-5555',
				'github': 'zyxwvut'},

	'Clarise': {'phone': '111-111-1111',
				'twitter': '@srqponm',
				'github': 'srqponm'}
}

#Goal 1
for contact in contacts.keys():
	print "{0}'s contact information is:".format(contact), "\n\tPhone:", contacts.get(contact).get('phone'), "\n\t", "Twitter:", contacts.get(contact).get('twitter'), "\n\tGithub:", contacts.get(contact).get('github'), "\n"
