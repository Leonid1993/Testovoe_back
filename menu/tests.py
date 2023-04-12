from django.test import TestCase, Client
from .models import Menu
from .templatetags.menu_tag import draw_menu, get_menu


class MenuModelTest(TestCase):
    def setUp(self) -> None:
        self.parent = Menu.objects.create(title='Title_1')
        self.children_1 = Menu.objects.create(title='Title_1_1', parent_id=self.parent.id)
        self.children_2 = Menu.objects.create(title='Title_1_2', parent_id=self.parent.id)
        self.children_1_1 = Menu.objects.create(title='Title_1_1_1', parent_id=self.children_1.id)
        self.children_1_2 = Menu.objects.create(title='Title_1_1_2', parent_id=self.children_1.id)

    def test_menu(self):
        parent_id = Menu.objects.get(title='Title_1').id
        assert [child.title for child in Menu.objects.all().filter(parent_id=parent_id)] == ['Title_1_1', 'Title_1_2']
        assert Menu.objects.get(title='Title_1_1').parent_id == self.parent.pk
        assert Menu.objects.get(title='Title_1_2').parent_id == self.parent.pk
        parent_id = Menu.objects.get(title='Title_1_1').id
        assert [child.title for child in Menu.objects.all().filter(parent_id=parent_id)] == ['Title_1_1_1', 'Title_1_1_2']
        assert Menu.objects.get(title='Title_1_1_1').parent_id == self.children_1.pk
        assert Menu.objects.get(title='Title_1_1_2').parent_id == self.children_1.pk

    def tearDown(self) -> None:
        Menu.objects.all().delete()


class BaseViewTest(TestCase):
    def test_view(self):
        c = Client()
        response = c.get("")
        assert response.status_code == 200
    def test_view_false(self):
        c = Client()
        response = c.get("/11")
        assert response.status_code == 404


class MenuTag(TestCase):
    def setUp(self) -> None:
        self.parent = Menu.objects.create(title='Title_1')
        self.parent2 = Menu.objects.create(title='Title_2')
        self.children_1 = Menu.objects.create(title='Title_1_1', parent_id=self.parent.id)
        self.parent3 = Menu.objects.create(title='Title3')
        self.children_2 = Menu.objects.create(title='Title_1_2', parent_id=self.parent.id)
        self.parent4 = Menu.objects.create(title='Title4')
        self.children_1_1 = Menu.objects.create(title='Title_1_1_1', parent_id=self.children_1.id)
        self.children3_1 = Menu.objects.create(title='Title3_1', parent_id=self.parent3.id)
        self.children_1_2 = Menu.objects.create(title='Title_1_1_2', parent_id=self.children_1.id)
        self.item = Menu.objects.all().values()
    def test_template_tag(self):
        print('Вот он!!!', get_menu(self.item), '|||')
        assert get_menu(self.item) == '<ul>'
