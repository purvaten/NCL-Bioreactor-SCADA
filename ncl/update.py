"""File to update database values based on values obtained from bioreactor.

Run as - python manage.py shell < update.py
"""

from scada.models import Values
pr = 3.4
t = 19.3
p = 2.3
l = 1.0
p1 = Values(name='dj', pressure=pr, temperature=t, ph=p, levels=l)
p1.save()

