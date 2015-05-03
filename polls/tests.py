from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question
from django.core.urlresolvers import reverse


class QuestionMethodTest(TestCase):
	def test_was_published_recently_with_future_question(self):
		""" was_published_recently() should return False
		for Questions whose pub_date is in the future"""
		time = timezone.now()+datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		""" was published recently should return False
		for questions whose pub_date is older than 1 day"""
		time = timezone.now()-datetime.timedelta(days=30)
		old_question = Question(pub_date=time)
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""was_published_recently should return True for questions
		whose pub_date is within the last day"""
		time = timezone.now()-datetime.timedelta(hours=1)
		recent_question = Question(pub_date=time)
		self.assertEqual(recent_question.was_published_recently(), True)


def create_question(question_text, days):
	"""Creates a new question with the giving question text published the given
	number of days offset to now(negative for questions published in the past,
		positve for questions that have yet to be published)"""
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTest(TestCase):
	def test_index_view_with_no_question(self):
		"""if no question does not exist, an appropriate message should be displayed"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_a_past_question(self):
		"""Questions with a pub_date in the past should be displayed in the 
		index page"""
		create_question(question_text='past question', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: past question>'])

	def test_index_view_with_a_future_question(self):
		"""Question with pub date in the future should not be displayes in the index page"""
		create_question(question_text='future question', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_future_question_and_past_question(self):
		"""Even if both past and future question exists, only past questions should be published"""
		create_question(question_text='past question', days=-30)
		create_question(question_text='future question', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: past question>'])

	def test_index_view_with_two_past_questions(self):
		"""the question index page must display multiple questions"""
		create_question(question_text='first question', days=-30)
		create_question(question_text='second question', days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: second question>',
                                                                           '<Question: first question>'])

class QuestionIndexDetailTest(TestCase):
	"""the detail view of a question in the future should return 404 question not found"""
	def test_detail_view_with_a_future_question(self):
		future_question = create_question(question_text='future question', days=5)
		response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
		self.assertEqual(response.status_code, 404)

	def test_detail_view_with_past_question(self):
		past_question = create_question(question_text='past question', days=-5)
		response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
		self.assertEqual(response.status_code, 200)
