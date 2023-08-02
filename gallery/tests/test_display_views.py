import uuid

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
    """
       Testing the detail_room function-based view

       Testing area:
            _url_routing:
                --require_http_method=GET
                --location="/room/<room_pk>/"
                --url_params=room_pk
                --raise 404 if room not exist

            _template_name:
                "gallery/detail_room.html"

            _context_variable:
                variable passed to the tmeplates:
                    --room= the room model instance
    """
    @classmethod
    def setUpTestData(self):
        # Create one test users
        test_user1 = User.objects.create_user(username='test_user1', password='no way home ')


        Room.objects.create(
                name=f'test_room',
                owner = test_user1 ,
                )

    def test_view_exist_at_desired_location(self):
        # Get room primary key
        room_pk = Room.objects.get(name='test_room').id
        res = self.client.get(f'/room/{room_pk}') 

        self.assertEqual(res.status_code, 200)

    def test_view_accessible_by_name(self):
        room_pk = Room.objects.get(name='test_room').id
        res = self.client.get(reverse('detail-room', args=[room_pk])) 

        self.assertEqual(res.status_code, 200)

    def test_view_accessible_only_via_GET_requrest(self):
        room_pk = Room.objects.get(name='test_room').id
        # Try requesting the view via post method 
        res = self.client.post(reverse('detail-room', args=[room_pk])) 

        # assert that status code is 405 (not allowed methdo)
        self.assertEqual(res.status_code, 405)

    def test_view_raise_404_response_if_room_not_found(self):
        # generate a random uuid for the test room  
        room_pk = uuid.uuid4()
        res = self.client.get(reverse('detail-room', args=[room_pk])) 

        # Assert that view return not found error 
        self.assertEqual(res.status_code, 404)

    def test_correct_template_used(self):
        room_pk = Room.objects.get(name='test_room').id
        res = self.client.get(reverse('detail-room', args=[room_pk])) 

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'gallery/detail_room.html')

    def test_template_passed_the_room_variable(self):
        room_pk = Room.objects.get(name='test_room').id
        res = self.client.get(reverse('detail-room', args=[room_pk])) 

        self.assertEqual(res.status_code, 200)
        self.assertTrue('room' in res.context)
        self.assertEqual(res.context['room'].pk , room_pk)
