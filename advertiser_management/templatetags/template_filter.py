from django import template

register = template.Library()


@register.filter(name='smooth_timedelta')
def smooth_timedelta(time_delta_obj):
    """Convert a datetime.timedelta object into Days, Hours, Minutes, Seconds."""
    secs = time_delta_obj.total_seconds()
    time = ""
    if secs > 86400:  # 60sec * 60min * 24hrs
        days = secs // 86400
        time += "{} days".format(int(days))
        secs = secs - days * 86400

    if secs > 3600:
        hrs = secs // 3600
        time += " {} hours".format(int(hrs))
        secs = secs - hrs * 3600

    if secs > 60:
        mins = secs // 60
        time += " {} minutes".format(int(mins))
        secs = secs - mins * 60

    if secs > 0:
        time += " {} seconds".format(int(secs))
    return time
