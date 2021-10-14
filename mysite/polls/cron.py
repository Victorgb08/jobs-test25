from .models import User, Text

def my_scheduled_job():
  User.objects.create(name="Victor", age=22,job="dev")
  user = User.objects.get(name="Victor")
  Text.objects.create(user=user,body="Meu texto é muito legal prestem bastante atenção", title="Titulo teste")