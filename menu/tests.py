from django.test import TestCase, Client
from .models import Menu
from .templatetags.menu_tag import get_menu


class MenuModelTest(TestCase):
    def setUp(self) -> None:
        self.parent = Menu.objects.create(title='Title_1', url='parent')
        self.children_1 = Menu.objects.create(title='Title_1_1', parent_id=self.parent.id, url='child1')
        self.children_2 = Menu.objects.create(title='Title_1_2', parent_id=self.parent.id, url='child2')
        self.children_1_1 = Menu.objects.create(title='Title_1_1_1', parent_id=self.children_1.id, url='child1_1')
        self.children_1_2 = Menu.objects.create(title='Title_1_1_2', parent_id=self.children_1.id, url='child1_2')

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
    def test_view_false(self):
        c = Client()
        response = c.get("")
        assert response.status_code == 404
    def test_view(self):
        c = Client()
        response = c.get("/11")
        assert response.status_code == 200


class MenuTag(TestCase):
    def setUp(self) -> None:
        self.parent = Menu.objects.create(title='Title_1', branch=1, url='parent')
        self.parent2 = Menu.objects.create(title='Title_2', branch=2, url='parent2')
        self.children_1 = Menu.objects.create(title='Title_1_1', parent_id=self.parent.id, url='children1')
        self.parent3 = Menu.objects.create(title='Title3', branch=3, url='parent3')
        self.children_2 = Menu.objects.create(title='Title_1_2', parent_id=self.parent.id, url='children2')
        self.parent4 = Menu.objects.create(title='Title4', branch=4, url='parent4')
        self.children_1_1 = Menu.objects.create(title='Title_1_1_1', parent_id=self.children_1.id, url='children1_1')
        self.children3_1 = Menu.objects.create(title='Title3_1', parent_id=self.parent3.id, url='children3_1')
        self.children_1_2 = Menu.objects.create(title='Title_1_1_2', parent_id=self.children_1.id, url='children_1_2')
        self.item = Menu.objects.all().values()
    def test_template_tag(self) -> str:
        print('Вот он!!!', get_menu(self.item))
        assert get_menu(self.item) ==  '<ul><li><a href="/parent">Title_1</a></li>' \
                                       '<ul><li><a href="/children1">Title_1_1</a></li>' \
                                       '<ul><li><a href="/children1_1">Title_1_1_1</a></li>' \
                                       '</li>' \
                                       '<li><a href="/children_1_2">Title_1_1_2</a></li>' \
                                       '</li></ul>' \
                                       '</li><li><a href="/children2">Title_1_2</a></li>' \
                                       '</li></ul></li>' \
                                       '<li><a href="/parent2">Title_2</a></li></li>' \
                                       '<li><a href="/parent3">Title3</a></li>' \
                                       '<ul><li><a href="/children3_1">Title3_1</a></li>' \
                                       '</li></ul></li>' \
                                       '<li><a href="/parent4">Title4</a></li></li></ul>'

class Signals(TestCase):
    def setUp(self) -> None:
        self.parent = Menu.objects.create(title='Title_1', branch=1, url='parent')
        self.children_1 = Menu.objects.create(title='Title_1_1', parent_id=self.parent.id, url='children1')
        self.children_2 = Menu.objects.create(title='Title_1_2', parent_id=self.parent.id, url='children2')
        self.children_1_1 = Menu.objects.create(title='Title_1_1_1', parent_id=self.children_1.id, url='children1_1')
        obj = Menu.objects.get(pk=self.children_1_1.pk)
        print(obj.parent_id)
        obj.parent_id = self.parent.id
        obj.save()
        print(obj.parent_id)

    def test_signal(self) -> str:
        assert Menu.objects.get(title='Title_1_1_1').level == Menu.objects.get(title='Title_1_1').level