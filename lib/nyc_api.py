import requests
import json
class GetPrograms:
  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  def school_programs(self):
    programs_list=[]
    programs= json.loads(self.get_programas())
    for program in programs:
      programs_list.append(program["agency"])

      return programs_list

programs = GetPrograms().get_programs()
print(programs)
programs=GetPrograms()

program_schools=programs.school_programs()

for school in set(program_schools):
  print(school)