import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SMTP:
	__session: smtplib.SMTP | None = None
	__username: str
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.logout()
		if exc_type is not None:
			print(f"[EXCEPT]: {exc_type} occurred with: {exc_val}")
	
	@staticmethod
	def __is_code_200(*args) -> bool:
		for typ in args:
			if 200 <= typ < 300:
				return True
		return False
	
	def logout(self) -> bool:
		status = True
		if self.__session is not None:
			status = self.__is_code_200(self.__session.quit()[0])
			self.__session = None
			self.__username = ''
			if status:
				print("[LOG]: Successful logout")
		return status
	
	def login(self, username: str, password: str) -> bool:
		status = False
		if self.__session is not None:
			print("[WARN]: Already logged in")
			return status
		
		try:
			domain = username.split('@')[1]
			host = f'smtp.{domain}'
			
			self.__session = smtplib.SMTP(host, 587)
			self.__username = username
			
			status = self.__is_code_200(
				self.__session.starttls()[0],
				self.__session.login(username, password)[0]
			)
		except Exception as e:		# IndexError, smtplib.SMTPException, OSError #
			self.logout()
			print("[EXCEPT]:", type(e), e)
		finally:
			if status:
				print("[LOG]: Successful login")
			return status
	
	def send(self, address: str, subject: str, text: str):
		mime = MIMEText(text, 'plain', 'utf-8')
		mime['Subject'] = Header(subject, 'utf-8')
		self.__session.sendmail(self.__username, address, mime.as_string())
