from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )


    def test_models_have_correct_post_names(self):
        post = PostModelTest.post
        expected_post_name = post.text
        self.assertEqual(expected_post_name, str(post))


    def test_models_have_correct_group_names(self):
        group = PostModelTest.group
        expected_group_name = group.title
        self.assertEqual(expected_group_name, str(group))


    def test_verbose_name(self):
        task = PostModelTest.post
        field_verboses = {
            'group': 'Группа',
            'text': 'Текст поста',
            'author': 'Автор',
            'pub_date': 'Дата публикации',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_help_text(self):
        task = PostModelTest.post
        field_help_texts = {
            'group': 'Группа, к которой будет относиться пост',
            'text': 'Введите текст поста',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).help_text, expected_value)