from django.test import TestCase
from .models import Menu

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
        print(Menu.objects.all())
        print(Menu.objects.all().values())
        Menu.objects.all().delete()