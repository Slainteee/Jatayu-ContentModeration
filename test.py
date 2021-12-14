try:
	from app import app
	import unittest
except Exception as e:
	print("{}".format(e))


class apitest(unittest.TestCase):

	# Check for response type(200)
	def test_response(self):
		tester = app.test_client(self)
		response = tester.get("")
		statuscode = response.status_code
		self.assertEqual(statuscode,200)

if __name__=="__main__":
	unittest.main()

