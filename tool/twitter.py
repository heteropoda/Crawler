
from tool.time import formate_time2time_stamp, time_now_formate, time_stamp2formate_time


def q_format(kwargs):

        def since_until(since=None, until=None):
            out = ''
            if until:
                out += 'until:{} '.format(until)
            if since:
                out += 'since:{} '.format(since)
            return out

        q = ''
        for i in kwargs.get('words', []):
            if isinstance(i, str):
                q += '"{}" '.format(i)
            elif isinstance(i, list):
                q += '({}) '.format(' OR '.join(['"{}"'.format(j) for j in i]))
                
        for i in kwargs.get('none_words', []):
            q += '-"{}" '.format(i)

        if kwargs.get('from'):
            q += '({}) '.format(' OR '.join(['from:{}'.format(i) for i in kwargs['from']]))

        if not kwargs.get('step'):
            yield q + since_until(kwargs.get('since'), kwargs.get('until'))
        else:
            since_p = formate_time2time_stamp(kwargs['since'] if kwargs.get('since') else '2006-01-01')
            until_p = formate_time2time_stamp(kwargs['until'] if kwargs.get('until') else time_now_formate().split(' ')[0])
            step = step_format(kwargs['step'])
            while(since_p < until_p):
                next = since_p + step
                yield q + since_until(time_stamp2formate_time(since_p), time_stamp2formate_time(next))
                since_p = next
                
def step_format(step):
        if step == 'day':
            return 86400
        elif step == 'month':
            return 2592000
        elif step == 'year':
            return 31536000
        raise Exception('step参数错误')