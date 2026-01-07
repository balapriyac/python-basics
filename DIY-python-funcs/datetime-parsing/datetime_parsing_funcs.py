from datetime import datetime, timedelta
import re

def parse_relative_time(time_string, reference_time=None):
    """
    Convert relative time strings to datetime objects.

    Examples: "2 hours ago", "3 days ago", "1 week ago"
    """
    if reference_time is None:
        reference_time = datetime.now()

    # Normalize the string
    time_string = time_string.lower().strip()

    # Pattern: number + time unit + "ago"
    pattern = r'(\d+)\s*(second|minute|hour|day|week|month|year)s?\s*ago'
    match = re.match(pattern, time_string)

    if not match:
        raise ValueError(f"Cannot parse: {time_string}")

    amount = int(match.group(1))
    unit = match.group(2)

    # Map units to timedelta kwargs
    unit_mapping = {
        'second': 'seconds',
        'minute': 'minutes',
        'hour': 'hours',
        'day': 'days',
        'week': 'weeks',
    }

    if unit in unit_mapping:
        delta_kwargs = {unit_mapping[unit]: amount}
        return reference_time - timedelta(**delta_kwargs)
    elif unit == 'month':
        # Approximate: 30 days per month
        return reference_time - timedelta(days=amount * 30)
    elif unit == 'year':
        # Approximate: 365 days per year
        return reference_time - timedelta(days=amount * 365)

# Test the function
result1 = parse_relative_time("2 hours ago")
result2 = parse_relative_time("3 days ago")
result3 = parse_relative_time("1 week ago")

print(f"2 hours ago: {result1}")
print(f"3 days ago: {result2}")
print(f"1 week ago: {result3}")

def extract_date_from_text(text, current_year=None):
    """
    Extract dates from natural language text.

    Handles formats like:
    - "January 15th, 2024"
    - "March 3rd"
    - "Dec 25th, 2023"
    """
    if current_year is None:
        current_year = datetime.now().year

    # Month names (full and abbreviated)
    months = {
        'january': 1, 'jan': 1,
        'february': 2, 'feb': 2,
        'march': 3, 'mar': 3,
        'april': 4, 'apr': 4,
        'may': 5,
        'june': 6, 'jun': 6,
        'july': 7, 'jul': 7,
        'august': 8, 'aug': 8,
        'september': 9, 'sep': 9, 'sept': 9,
        'october': 10, 'oct': 10,
        'november': 11, 'nov': 11,
        'december': 12, 'dec': 12
    }

    # Pattern: Month Day(st/nd/rd/th), Year (year optional)
    pattern = r'(january|jan|february|feb|march|mar|april|apr|may|june|jun|july|jul|august|aug|september|sep|sept|october|oct|november|nov|december|dec)\s+(\d{1,2})(?:st|nd|rd|th)?(?:,?\s+(\d{4}))?'

    matches = re.findall(pattern, text.lower())

    if not matches:
        return None

    # Take the first match
    month_str, day_str, year_str = matches[0]

    month = months[month_str]
    day = int(day_str)
    year = int(year_str) if year_str else current_year

    return datetime(year, month, day)

text1 = "The meeting is scheduled for January 15th, 2026 at 3pm"
text2 = "Please respond by March 3rd"
text3 = "Deadline: Dec 25th, 2026"

date1 = extract_date_from_text(text1)
date2 = extract_date_from_text(text2)
date3 = extract_date_from_text(text3)

print(f"From '{text1}': {date1}")
print(f"From '{text2}': {date2}")
print(f"From '{text3}': {date3}")

def parse_flexible_date(date_string):
    """
    Parse dates in multiple common formats.

    Tries various formats and returns the first match.
    """
    date_string = date_string.strip()

    # List of common date formats
    formats = [
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%d-%m-%Y',
        '%d/%m/%Y',
        '%m/%d/%Y',
        '%d.%m.%Y',
        '%Y%m%d',
        '%B %d, %Y',
        '%b %d, %Y',
        '%d %B %Y',
        '%d %b %Y',
    ]

    # Try each format
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue

    # If nothing worked, raise an error
    raise ValueError(f"Unable to parse date: {date_string}")

# Test different formats
dates = [
    "2026-01-15",
    "15/01/2026",
    "01/15/2026",
    "15.01.2026",
    "20260115",
    "January 15, 2026",
    "15 Jan 2026"
]

for date_str in dates:
    parsed = parse_flexible_date(date_str)
    print(f"{date_str:20} -> {parsed}")

def parse_duration(duration_string):
    """
    Parse duration strings into timedelta objects.

    Handles formats like:
    - "1h 30m 45s"
    - "2:45:30" (H:M:S)
    - "90 minutes"
    - "1.5 hours"
    """
    duration_string = duration_string.strip().lower()

    # Try colon format first (H:M:S or M:S)
    if ':' in duration_string:
        parts = duration_string.split(':')
        if len(parts) == 2:
            # M:S format
            minutes, seconds = map(int, parts)
            return timedelta(minutes=minutes, seconds=seconds)
        elif len(parts) == 3:
            # H:M:S format
            hours, minutes, seconds = map(int, parts)
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)

    # Try unit-based format (1h 30m 45s)
    total_seconds = 0

    # Find hours
    hours_match = re.search(r'(\d+(?:\.\d+)?)\s*h(?:ours?)?', duration_string)
    if hours_match:
        total_seconds += float(hours_match.group(1)) * 3600

    # Find minutes
    minutes_match = re.search(r'(\d+(?:\.\d+)?)\s*m(?:in(?:ute)?s?)?', duration_string)
    if minutes_match:
        total_seconds += float(minutes_match.group(1)) * 60

    # Find seconds
    seconds_match = re.search(r'(\d+(?:\.\d+)?)\s*s(?:ec(?:ond)?s?)?', duration_string)
    if seconds_match:
        total_seconds += float(seconds_match.group(1))

    if total_seconds > 0:
        return timedelta(seconds=total_seconds)

    raise ValueError(f"Unable to parse duration: {duration_string}")

# Test cases
durations = [
    "1h 30m 45s",
    "2:45:30",
    "90 minutes",
    "1.5 hours",
    "45s",
    "2h 15m"
]

for duration in durations:
    parsed = parse_duration(duration)
    print(f"{duration:15} -> {parsed}")

def parse_iso_week_date(iso_week_string):
    """
    Parse ISO week date format: YYYY-Www-D

    Example: "2024-W03-2" = Week 3 of 2024, Tuesday

    ISO week numbering:
    - Week 1 is the week with the first Thursday of the year
    - Days are numbered 1 (Monday) through 7 (Sunday)
    """
    # Parse the format: YYYY-Www-D
    parts = iso_week_string.split('-')

    if len(parts) != 3 or not parts[1].startswith('W'):
        raise ValueError(f"Invalid ISO week format: {iso_week_string}")

    year = int(parts[0])
    week = int(parts[1][1:])  # Remove 'W' prefix
    day = int(parts[2])

    if not (1 <= week <= 53):
        raise ValueError(f"Week must be between 1 and 53: {week}")

    if not (1 <= day <= 7):
        raise ValueError(f"Day must be between 1 and 7: {day}")

    # Find January 4th (always in week 1)
    jan_4 = datetime(year, 1, 4)

    # Find Monday of week 1
    week_1_monday = jan_4 - timedelta(days=jan_4.weekday())

    # Calculate the target date
    target_date = week_1_monday + timedelta(weeks=week - 1, days=day - 1)

    return target_date

iso_dates = [
    "2024-W01-1",  # Week 1, Monday
    "2024-W03-2",  # Week 3, Tuesday
    "2024-W10-5",  # Week 10, Friday
]

for iso_date in iso_dates:
    parsed = parse_iso_week_date(iso_date)
    print(f"{iso_date} -> {parsed.strftime('%Y-%m-%d (%A)')}")


