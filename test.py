
import app
import unittest



class apitest(unittest.TestCase):

	def setUp(self):
		print()
		print("==> Setting up the env for tests!!")
		app.app.config['Testing']=True
		self.app = app.app.test_client()

	def tearDown(self):
		print("==> Tearing down after tests!! \n")
	
	# Check for response type(200)
	def test_response(self):
		resp = self.app.get('/')
		self.assertEqual(resp.status_code,200)

	# Check for return type(application/json)
	def test_content(self):
		resp = self.app.get('/')
		self.assertEqual(resp.content_type, "application/json")
if __name__=="__main__":
	unittest.main()

