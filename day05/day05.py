
dr = "destination_range_start"
sr = "source_range_start"
rlen = "range_length"
def create_mapping(ranges):
    def f(source):
        for r in ranges:
            if source in range(r[sr],r[sr]+r[rlen]):
                return (source - r[sr]) + r[dr]
        return source
    return f

def parse_section(section):
    ranges = []
    for line in section.split('\n')[1:]:
        ranges.append(parse_line(line))
    return ranges

def parse_line(line):
    splitline = line.split()
    rangeObject = {
        dr: int(splitline[0]),
        sr: int(splitline[1]),
        rlen: int(splitline[2])
    }
    return rangeObject

with open("day05.input") as input:
    almanac = input.read()
sections = almanac.split('\n\n')

seeds = [int(i) for i in sections[0].split()[1:]]

seedToSoil = create_mapping(parse_section(sections[1]))
soilToFertilizer = create_mapping(parse_section(sections[2]))
fertilizerToWater = create_mapping(parse_section(sections[3]))
waterToLight = create_mapping(parse_section(sections[4]))
lightToTemperature = create_mapping(parse_section(sections[5]))
TemperatureToHumidity = create_mapping(parse_section(sections[6]))
HumidityToLocation = create_mapping(parse_section(sections[7]))

print(sorted([HumidityToLocation(TemperatureToHumidity(lightToTemperature(waterToLight(fertilizerToWater(soilToFertilizer(seedToSoil(i))))))) for i in seeds])[0])