from aliens import Alien
import matplotlib.pyplot as plt
from alien_def import gen_aliens


al=gen_aliens(20,20,20,5)
for a in al:
    plt.scatter(a.x_cord,a.y_cord,s=a.health)
plt.show()