
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

def parse_seeds(seedInput):
    seeds = []
    seedRanges = []
    for i in range(len(seedInput))[::2]:
        #seeds += [a for a in range(seedInput[i],seedInput[i]+seedInput[i+1])]
        seedRanges.append((seedInput[i],seedInput[i]+seedInput[i+1]))
    seedRanges.sort(key=lambda x:x[0])
    return seedRanges

def overlap(p1,p2):
    (x,y) = p1
    (m,n) = p2
    notOverlaps = []
    overlaps = []
    if max(x,y) < min(m,n) or max(m,n) < min(x,y):
        notOverlaps.append((x,y))
    else:
        s = sorted([x,y,m,n])
        overlaps.append((s[1],s[2]))
        if s[0] != m:
            notOverlaps.append((s[0],s[1]))
        if s[-1] != n:
            notOverlaps.append((s[2],s[3]))
    return (overlaps, notOverlaps)

def get_possible_destinations(ranges, sections):
    destinations = []
    for section in sections:
        newRanges = set()
        for r in ranges:
            (overlaps, notOverlaps) = overlap(r,(section[sr],section[sr]+section[rlen]))
            # print(overlaps, notOverlaps)
            for o in overlaps:
                destinations.append(((o[0] - section[sr]) + section[dr], (o[1] - section[sr]) + section[dr]))
            newRanges.update(notOverlaps)
        ranges = newRanges
    # handle things with no overlap
    destinations += ranges
    return destinations

with open("day05.input") as input:
    almanac = input.read()
almanacSections = almanac.split('\n\n')

rangeToCheck = parse_seeds([int(i) for i in almanacSections[0].split()[1:]])
for section in almanacSections[1:]:
    rangeToCheck = get_possible_destinations(rangeToCheck, parse_section(section))
    # print(rangeToCheck)
print(min(start for start, _ in rangeToCheck))