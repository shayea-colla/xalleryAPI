from django.test import TestCase
from django.urls import reverse

from gallery.models import Room
from accounts.models import User

class TestListAllRoomsView(TestCase):
    """
        Class for testing the listAllRooms class-based view

        Testing area:
            _url routing:
                url = '/' (index)
                name = 'list-all-rooms'
            _template_name:
                'gallery/list_all_rooms.html'
            _pagination:
                20 room per page
            
    """
    @classmethod
    def setUpTestData(self):

        # Create two test users
        test_user1 = User.objects.create_user(username='test_user1', password='no way home ')
        test_user2 = User.objects.create_user(username='test_user2', password='no way home ')


        # create 30 rooms, 15 room for each user
        num_rooms = 30
        for i in range(num_rooms):
            Room.objects.create(
                    name=f'test_room_{i}',
                    owner = test_user1 if i % 2 else test_user2,
                    )
    
    def test_view_exist_at_desired_location(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_view_accessible_by_name(self):
        res = self.client.get(reverse('list-all-rooms'))
        self.assertEqual(res.status_code, 200)

    def test_view_use_correct_template(self):
        res = self.client.get(reverse('list-all-rooms'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'gallery/list_all_rooms.html')

    def test_paginating_is_twentee(self):
        res = self.client.get(reverse('list-all-rooms'))
        self.assertEqual(res.status_code, 200)

        self.assertTrue('is_paginated' in res.context)
        self.assertTrue(res.context['is_paginated'] == True)
        self.assertTrue(len(res.context['room_list']) == 20)

    def test_lists_all_rooms(self):
        res = self.client.get(reverse('list-all-rooms') + '?page=2')
        self.assertEqual(res.status_code, 200)
        self.assertTrue('is_paginated' in res.context)
        self.assertTrue(res.context['is_paginated'] == True)
        self.assertTrue(len(res.context['room_list']) == 10)




class TestDetailRoomView(TestCase):
    pass
