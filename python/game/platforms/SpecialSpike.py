import constants
import pygame
from Spike import Spike
from MovingSpike import MovingSpike
class SpecialSpike(MovingSpike):
    """ This is a fancier platform that can actually move. """

    change_x_r = 0
    change_x_l = 0
    change_y_u = 0
    change_y_d = 0
    pause_up = 0
    pause_down = 0
    pause_right = 0
    pause_left = 0
    
    pause = False
    time = 0


    def update(self):
        """ Special case of the moving spikes"""

        MovingSpike.update(self)



    def boundaries(self):

        # Check the boundaries and see if we have a pause and if we need to reverse direction.

        """
        up/down plateforms
        """
        #case where we have a pause down
        if self.rect.bottom > self.boundary_bottom and not self.pause:
            self.change_y = 0
            self.pause = True
            self.time = self.pause_down

        #if we have to wait, i.e. pause == True
        if self.rect.bottom > self.boundary_bottom and self.pause:
            if self.time > 0:
                self.time -= 1
            else:
                self.change_y = self.change_y_u #set the speed from bottom to top
                self.pause = False


        #case where we have a pause up
        if self.rect.top < self.boundary_top and not self.pause:
            self.change_y = 0
            self.pause = True
            self.time = self.pause_up

        #if we have to wait, i.e. pause == True
        if self.rect.top < self.boundary_top and self.pause:
            if self.time > 0:
                self.time -= 1
            else:
                self.change_y = self.change_y_d #set the speed from top to bottom
                self.pause = False




        """
        left/right plateforms
        """
        cur_pos = self.rect.x - self.level.world_shift

        #case where we have a pause on the left
        if cur_pos < self.boundary_left and not self.pause:
            self.change_x = 0
            self.pause = True
            self.time = self.pause_left

        if cur_pos < self.boundary_left and self.pause:
            if self.time > 0:
                self.time -= 1
            else:
                self.change_x = self.change_x_r
                self.pause = False

        
        #case where we have a pause on the left
        if cur_pos > self.boundary_right and not self.pause:
            self.change_x = 0
            self.pause = True
            self.time = self.pause_right

        if cur_pos > self.boundary_left and self.pause:
            if self.time > 0:
                self.time -= 1
            else:
                self.change_x = self.change_x_l
                self.pause = False