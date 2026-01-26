length_of_zander=float(input('please enter length of zander: '))
if length_of_zander >= 42:
    print('The zender is within the size limit')
else:
    difference = 42 - length_of_zander
    print('The zender is outside the size limit')
    print(f'the zender is {difference} cm shorter than the size limit')





cabin_class=str(input('please enter cabin class:'))
if cabin_class == 'LUX':
    print('The cabin is upper-deck with a balcony')
elif cabin_class == 'A':
    print('The cabin is above the car deck,equipped with a window')
elif cabin_class == 'B':
    print('The cabin is windowless above the car deck')
elif cabin_class == 'C':
    print('The cabin is windowless below the car deck')
else :
    print('You entered an invalid cabin class')


Gender = str(input('please enter gender:'))
hemoglobin_value = float(input('please enter hemoglobin value: '))

if Gender == 'male':
   if hemoglobin_value >= 117 and hemoglobin_value <= 155:
        print('The hemoglobin value is normal')
   elif hemoglobin_value > 155:
        print('The hemoglobin value is high')
   elif hemoglobin_value < 117:
        print('The hemoglobin value is low')
if Gender == 'female':
   if hemoglobin_value >= 134 and hemoglobin_value <= 167:
     print('The hemoglobin value is normal')
   elif hemoglobin_value > 167:
        print('The hemoglobin value is high')
   elif hemoglobin_value < 134:
        print('The hemoglobin value is low')



year = int(input('please enter year:'))
if year / 4 == year // 4 :
    print('The year is a leap year')
elif year / 100 == year // 100 and year / 400 == year // 400:
    print('The year is a leap year')

else :
    print('The year is not a leap year')