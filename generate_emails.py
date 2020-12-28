#generate email addresses from lists
#list of domains
#list names with randomly generated suffixes and numbers

import random



def main():
	user_input = int(input("How many random emails do you want generated?\n>"))
	
	
	for x in range(user_input):
		domains = ["hotmail.com", "outlook.com", "yahoo.com", 
			"aol.com", "protonmail.com", "pm.me", "cali4nialove.com"]
		random_domains = random.choice(domains)
		special_characters = ["_", "-"]
		shuffle_special_characters = random.choice(special_characters)
	
		names_of_kids = ["Emma",
		"Olivia",
		"Ava",
		"Isabella",
		"Sophia",
		"Charlotte",
		"Mia",
		"Amelia",
		"Harper",
		"Evelyn",
		"Alex",
		"Noah",
		"William",
		"James",
		"Oliver",
		"Benjamin",
		"Elijah",
		"Lucas",
		"Mason",
		"Logan"]
		
		surnames = ["Smith",
		"Johnson",
		"Oliveira",
		"Williams",
		"Brown",
		"Jones",
		"Garcia",
		"Miller",
		"Davis",
		"Rodriguez",
		"Martinez",
		"Hernandez",
		"Lopez",
		"Gonzales",
		"Wilson",
		"Anderson",
		"Thomas",
		"Taylor",
		"Moore",
		"Jackson",
		"Martin",
		"Lee",
		"Perez",
		"Thompson",
		"White",
		"Harris",
		"Sanchez",
		"Clark",
		"Ramirez",
		"Lewis",
		"Robinson",
		"Walker",
		"Young",
		"Allen",
		"King",
		"Wright",
		"Scott",
		"Torres",
		"Nguyen",
		"Hill",
		"Flores",
		"Green",
		"Adams",
		"Nelson",
		"Baker",
		"Hall",
		"Rivera",
		"Campbell",
		"Mitchell",
		"Carter",
		"Roberts",
		"Gomez",
		"Phillips",
		"Evans",
		"Turner",
		"Diaz",
		"Parker",
		"Cruz",
		"Edwards",
		"Collins",
		"Reyes",
		"Stewart",
		"Morris",
		"Morales",
		"Murphy",
		"Cook",
		"Rogers",
		"Gutierrez",
		"Ortiz",
		"Morgan",
		"Cooper",
		"Peterson",
		"Bailey",
		"Reed",
		"Kelly",
		"Howard",
		"Ramos",
		"Kim",
		"Cox",
		"Ward",
		"Richardson",
		"Watson",
		"Brooks",
		"Chavez",
		"Wood",
		"James",
		"Bennet",
		"Gray",
		"Mendoza",
		"Ruiz",
		"Hughes",
		"Price",
		"Alvarez",
		"Castillo",
		"Sanders",
		"Patel",
		"Myers",
		"Long",
		"Ross",
		"Foster",
		"Jimenez"]
		random_surnames = random.choice(surnames)
    
		random_kids_names = random.choice(names_of_kids) 
		
		numbers_to_shuffle = list(range(1,500))
		random_shuffled_numbers = random.choice(numbers_to_shuffle)
		
		formatting_for_addresses = (
		f"{random_kids_names}.{random_surnames}{shuffle_special_characters}{random_shuffled_numbers}@{random_domains}")

		
		print(formatting_for_addresses)





	
	

main()
print("\nAll Done!")
