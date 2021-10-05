def http_error(status):
	match status:
		case 400:
			retrun "Bad request"
			
		case 401 | 403:
			return "Not allowed"
		
		
		case 404:
			return "Not found"
		
		case 418:
			return "I'm a teapot"
		
		
		case _ "
		
			return "Something's wrong with the internet"

		
		
def match_point:
	case (0,0):
		print("Origin")
		
	case(0,y):
		print(f" x= 0 y = {}")
		
	case(x,0):
		print(f" x = {x}, y= 0")
		
		
	case (x,y):
		print(f"x = {x}, y = {y}")
		
		
		
	case _ :
		raise ValueError( "Not a point")
		
