import random
def main():
   tplayer = 1
   sinput = 1
   er = 0

   cpile = random.choice([4,5,6])
   lpile = random.choice([2, 3, 4])
   rpile = random.choice([6,7,8])

   p1 = input('Enter 1st player'+"'"+'s name: ')
   p2 = input('Enter 2nd player'+"'"+'s name: ')

   prs = [p1,p2]

   player = random.choice(prs)


   while ((lpile+cpile+rpile) != 0):
       if tplayer == 0:
           tplayer = 1

       if er == 0:
           print('*****'+player+"'"+'s turn*****')
           print(f'L:{lpile}   C:{cpile}   R:{rpile}')

       if tplayer >= 1 and sinput == 1:
           choose_pile = input('Choose a pile to take from (L/C/R): ')
           tplayer = 1

       if choose_pile in 'Ll':
           if lpile == 0:
               print('There are no beads in the left pile.')
               tplayer = 2
               er = 1
       elif choose_pile in 'Cc':
           if cpile == 0:
               print('There are no beads in the center pile.')
               tplayer = 2
               er = 1
       elif choose_pile in 'Rr':
           if rpile == 0:
               print('There are no beads in the Right pile.')
               tplayer = 2
               er = 1



       if choose_pile in 'LlCcRr' and tplayer == 1:
           beads = int(input('Choose a number of beads to take (1/2/3): '))

           if beads >=1 and beads <= 3:
               if choose_pile in 'Ll':
                   if beads > lpile:
                       print('The left pile has less than '+str(beads)+' beads in it.')
                       tplayer = 0
                       er = 1
                       sinput = 0
                   else:
                       lpile -= beads
                       tplayer = 1
               elif choose_pile in 'Cc':
                   if beads > cpile:
                       print('The center pile has less than '+str(beads)+' beads in it.')
                       tplayer = 0
                       er = 1
                       sinput = 0
                   else:
                       cpile -= beads
                       tplayer = 1
               elif choose_pile in 'Rr':
                   if beads > rpile:
                       print('The right pile has less than '+str(beads)+' beads in it.')
                       tplayer = 0
                       er = 1
                       sinput = 0
                   else:
                       rpile -= beads
                       tplayer = 1
           else:
               if beads > 3:
                   print('You can'+"'"+'t take more than three beads.')
               elif beads == 0:
                   print('You must take at least one bead.')
               else:
                   print('Please Choose a number of beads from (1/2/3).')
               tplayer = 0
               er = 1
               sinput = 0

           if tplayer == 1:
               if prs.index(player) == 0:
                   player = p2
                   er = 0
                   sinput = 1
               else:
                   player = p1
                   er = 0
                   sinput = 1
       elif choose_pile not in 'LlCcRr':
           print('You must select a valid pile. (L/C/R)')
           er = 1


   print('Game over!')
   print(player+' wins!!')

main()
