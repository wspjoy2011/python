def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    if not isinstance(facing, str):
        return 'First argument must be a string type.'
    if not isinstance(turn, int):
        return 'Second argument must be an integer type'
    if facing not in directions:
        return f'First argument must be one of the listed: {directions} '
    return directions[(directions.index(facing) + turn // 45) % len(directions)]



