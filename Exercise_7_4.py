List_of_all = []

class Movie:
  def __init__(self, title, year, genre, recreate):
    self.title = title
    self.year = year
    self.genre = genre
    self.recreate = recreate

    self.recreate = 0

  def play(self, step=1):
    self.recreate += step

  def __str__(self):
    return f'{self.title} ({self.year})'


class Series:
  def __init__(self, stitle, syear, sgenre, sepisode, sseason, srecreate):
    self.stitle = stitle
    self.syear = syear
    self.sgenre = sgenre
    self.sepisode = sepisode
    self.sseason = sseason
    self.srecreate = srecreate

  def play(self, step=1):
    self.srecreate += step

  def __str__(self):
    return f'{self.stitle} S{self.sseason}E{self.sepisode}'

Indiana_Movie = Movie(title = 'Indiana', year = '2024', genre = 'documentary', recreate = 0)
List_of_all.append(Indiana_Movie)
print(Indiana_Movie)

Bad_Kid = Series(stitle='Bad Kid', syear='2024', sgenre='comedy', sepisode='01', sseason='01', srecreate=0)
List_of_all.append(Bad_Kid)
print(Bad_Kid)

print(List_of_all)
