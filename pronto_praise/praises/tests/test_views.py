from django.core.urlresolvers import reverse
from django.test import TestCase


class PraiseListView(TestCase):
    def test_praise_list_view_should_be_accessible(self):
        response = self.client.get(reverse('praise_list'))
        self.assertEqual(response.status_code, 200)

    def test_praise_list_view_should_have_title_saying_pronto_praise(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<title>Pronto Praise</title>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_use_jquery_and_semantic_ui(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<link rel="stylesheet" type="text/css" ' \
            'href="/static/semantic/semantic.min.css">'
        self.assertContains(response, expected, status_code=200)
        expected = '<script\n    src="https://code.jquery.com/' \
            'jquery-3.1.1.min.js"\n    ' \
            'integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDY' \
            'GmIJLv2b8="\n    crossorigin="anonymous"></script>'
        self.assertContains(response, expected, status_code=200)
        expected = '<script src="/static/semantic/semantic.min.js"></script>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_have_header_saying_praise(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<h1 class="ui header">Praise</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_have_praise_with_info_as_expected(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<div class="praise"><div class="praise-body">' \
            '<h3>Mils</h3><div><p>Listen and speak with care!</p></div>' \
            '<div class="ui items"><div class="item"><div class="extra">' \
            '<div class="ui right floated"><a href="#">' \
            '<i class="heart icon"></i></a>+ 0</div></div></div></div></div>' \
            '<strong>zkan</strong><br />Sept 1, 2016'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="praise"><div class="praise-body">' \
            '<h3>P\'Kan</h3><div><p>Cool and handsome!</p></div>' \
            '<div class="ui items"><div class="item"><div class="extra">' \
            '<div class="ui right floated"><a href="#">' \
            '<i class="heart icon"></i></a>+ 2</div></div></div></div></div>' \
            '<strong>Mils</strong><br />Sept 6, 2016'
        self.assertContains(response, expected, status_code=200)


class PraiseAddView(TestCase):
    def test_praise_add_view_should_be_accessible(self):
        response = self.client.get(reverse('praise_add'))
        self.assertEqual(response.status_code, 200)

    def test_praise_add_view_should_have_header_saying_write_praise(self):
        response = self.client.get(reverse('praise_add'))

        expected = '<h1 class="ui header">Write your Praise :)</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_add_view_should_have_write_praise_form(self):
        response = self.client.get(reverse('praise_add'))

        expected = '<form class="ui form" method="post" action=".">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value='
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="text" name="to" ' \
            'placeholder="Whom do you want to write to?">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="text" name="by" placeholder="Pim Ch">'
        self.assertContains(response, expected, status_code=200)

        expected = '<textarea></textarea>'
        self.assertContains(response, expected, status_code=200)

        expected = '<button class="ui button" type="submit">Submit</button>'
        self.assertContains(response, expected, status_code=200)
