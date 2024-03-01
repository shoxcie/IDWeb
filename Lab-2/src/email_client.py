import smtplib
from email.mime.text import MIMEText
from email.header import Header

import imaplib
import email
from email.utils import parseaddr
from email.utils import parsedate_to_datetime
from email.header import decode_header
from tzlocal import get_localzone
import base64


class SMTP:
	__session: smtplib.SMTP | None = None
	__username: str
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.logout()
		if exc_type is not None:
			print(f"[SMTP_EXCEPT]: {exc_type} occurred with: {exc_val}")
	
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
				print("[SMTP_LOG]: Successful logout")
		return status
	
	def login(self, username: str, password: str) -> bool:
		status = False
		if self.__session is not None:
			print("[SMTP_WARN]: Already logged in")
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
			print("[SMTP_EXCEPT]:", type(e), e)
			self.logout()
		finally:
			if status:
				print("[SMTP_LOG]: Successful login")
			return status
	
	def send(self, address: str, subject: str, text: str):
		mime = MIMEText(text, 'plain', 'utf-8')
		mime['Subject'] = Header(subject, 'utf-8')
		self.__session.sendmail(self.__username, address, mime.as_string())


class IMAP:
	__session: imaplib.IMAP4_SSL | None = None
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.logout()
		if exc_type is not None:
			print(f"[IMAP_EXCEPT]: {exc_type} occurred with: {exc_val}")
	
	def logout(self) -> bool:
		status = True
		if self.__session:
			status = (
					'OK' == self.__session.close()[0] and
					'BYE' == self.__session.logout()[0]
			)
			self.__session = None
			if status:
				print("[IMAP_LOG]: Successful logout")
		return status
	
	def login(self, username: str, password: str) -> bool:
		status = False
		if self.__session is not None:
			print("[IMAP_WARN]: Already logged in")
			self.logout()
		
		try:
			domain = username.split('@')[1]
			host = f'smtp.{domain}'
			
			self.__session = imaplib.IMAP4_SSL(host)
			
			status = (
				'OK' == self.__session.login(username, password)[0] and
				'OK' == self.__session.select('INBOX', readonly=True)[0]
			)
		except Exception as e:
			print("[IMAP_EXCEPT]:", type(e), e)
			self.logout()
		finally:
			if status:
				print("[IMAP_LOG]: Successful login")
			return status
