from django.core.management.base import BaseCommand
from myapp.models import Department, Team, CustomUser, HealthCard

class Command(BaseCommand):
    help = 'Sets up initial data for the SkyHealthCheck system'

    def handle(self, *args, **kwargs):
        # Create Departments
        dept1 = Department.objects.create(name="Engineering Dept")
        dept2 = Department.objects.create(name="Product Dept")

        # Create Teams for Engineering Dept
        team1 = Team.objects.create(name="Alpha Team", department=dept1)
        team2 = Team.objects.create(name="Beta Team", department=dept1)
        team3 = Team.objects.create(name="Gamma Team", department=dept1)

        # Create Teams for Product Dept
        team4 = Team.objects.create(name="Delta Team", department=dept2)
        team5 = Team.objects.create(name="Epsilon Team", department=dept2)
        team6 = Team.objects.create(name="Zeta Team", department=dept2)

        # Create Health Cards (10 cards)
        cards = [
            "Delivering Value", "Easy to Release", "Fun", "Learning", "Mission",
            "Speed", "Support", "Teamwork", "Quality", "Innovation"
        ]
        for card_name in cards:
            HealthCard.objects.create(name=card_name, description=f"Description for {card_name}")

        # Create Users (Engineers, Team Leaders, Department Leaders, Senior Managers)
        # Department Leaders
        dept_leader1 = CustomUser.objects.create_user(
            username="dept_leader1@example.com", email="dept_leader1@example.com",
            password="Pass@123", role="department_leader", first_name="Dept", last_name="Leader1"
        )
        dept_leader2 = CustomUser.objects.create_user(
            username="dept_leader2@example.com", email="dept_leader2@example.com",
            password="Pass@123", role="department_leader", first_name="Dept", last_name="Leader2"
        )
        dept1.leader = dept_leader1
        dept2.leader = dept_leader2
        dept1.save()
        dept2.save()

        # Team Leaders
        team_leader1 = CustomUser.objects.create_user(
            username="team_leader1@example.com", email="team_leader1@example.com",
            password="Pass@123", role="team_leader", first_name="Team", last_name="Leader1"
        )
        team_leader2 = CustomUser.objects.create_user(
            username="team_leader2@example.com", email="team_leader2@example.com",
            password="Pass@123", role="team_leader", first_name="Team", last_name="Leader2"
        )
        team1.leader = team_leader1
        team4.leader = team_leader2
        team1.save()
        team4.save()

        # Engineers (5 per team)
        for team in [team1, team2, team3, team4, team5, team6]:
            for i in range(5):
                engineer = CustomUser.objects.create_user(
                    username=f"engineer_{team.name.lower()}_{i+1}@example.com",
                    email=f"engineer_{team.name.lower()}_{i+1}@example.com",
                    password="Pass@123", role="engineer", first_name=f"Engineer", last_name=f"{team.name}{i+1}"
                )
                engineer.team = team
                engineer.save()

        # Senior Manager
        senior_manager = CustomUser.objects.create_user(
            username="senior_manager@example.com", email="senior_manager@example.com",
            password="Pass@123", role="senior_manager", first_name="Senior", last_name="Manager"
        )

        self.stdout.write(self.style.SUCCESS('Initial data setup completed!'))