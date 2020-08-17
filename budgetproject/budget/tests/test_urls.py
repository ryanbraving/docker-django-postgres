from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):
    # SimpleTestCase is used anytie that you don't need to interact with DB

    def test_list_url_is_resolved(self):
        url = reverse('list')
        print (resolve(url))
        self.assertEqual(resolve(url).func , project_list)

    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.view_class , ProjectCreateView)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=['some_slug'])
        self.assertEqual(resolve(url).func , project_detail)
