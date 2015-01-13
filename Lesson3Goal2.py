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

# Sample output:
# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @abc </td>
# <td> Github: @abc </td>
# </tr>
# </table>

#Goal 1
#for contact in contacts.keys():
#	print "{0}'s contact information is:".format(contact), "\n\tPhone:", contacts.get(contact).get('phone'), "\n\t", "Twitter:", contacts.get(contact).get('twitter'), "\n\tGithub:", contacts.get(contact).get('github'), "\n"

#Goal 2  
for contact in contacts.keys():          
	print """<tableborder="1">\n<tr>\n<td colspan="2"> {0} </td>""".format(contact), """\n</tr>\n<tr>\n<td> Phone:""", contacts.get(contact).get('phone'), """</td>\n<td> Twitter:""", contacts.get(contact).get('twitter'), """</td>\n<td> Github:""", contacts.get(contact).get('github'), """</td>\n</tr>\n</table>"""







