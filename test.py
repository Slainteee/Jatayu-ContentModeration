
import app
import unittest



class apitest(unittest.TestCase):

	def setUp(self):
		print("==> Setting up the env for tests!!")
		app.app.config['Testing']=True
		self.app = app.app.test_client()

	# Check for response type(200)
	def test_response(self):
		resp = self.app.get('/')
		assert "200 OK" == resp.status

if __name__=="__main__":
	unittest.main()

