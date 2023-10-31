from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from authentication.models import CustomUser

class Command(BaseCommand):
    help = 'Set up roles and permissions'

    def handle(self, *args, **options):
        # Create groups (roles)
        admin_group, created = Group.objects.get_or_create(name='Admin')
        moderator_group, created = Group.objects.get_or_create(name='Moderator')
        attendee_group, created = Group.objects.get_or_create(name='Attendee')

        # Assign permissions to groups
        admin_permissions = Permission.objects.filter(codename__in=['can_add_event', 'can_change_event', 'can_delete_event'])
        admin_group.permissions.set(admin_permissions)

        # Example: Assign users to groups
        admin_user = CustomUser.objects.get(email='manuravi564@gmail.com')
        admin_user.groups.add(admin_group)

        # Repeat the process for other groups and their respective permissions
        # You can add more user-to-group assignments here if needed

        self.stdout.write(self.style.SUCCESS('Roles and permissions set up successfully.'))
