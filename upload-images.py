# coding=utf-8
import os
import sys
import json
import subprocess


def display_notification(context, title, subtitle=None):
    if subtitle is None:
        subprocess.call('osascript -e \'display notification "%s" with title "%s"\' ' %
                        (context, title), shell=True)
    else:
        subprocess.call('osascript -e \'display notification "%s" with title "%s" subtitle "%s"\' ' %
                        (context, title, subtitle), shell=True)


result_file_path = os.environ['HOME'] + '/Library/Mobile Documents/com~apple~CloudDocs/sm.ms.txt'
result_image_path = os.environ['HOME'] + '/Library/Mobile Documents/com~apple~CloudDocs/SM.MS Images/'

try:
    with open(result_file_path, 'r') as the_file:
        content = the_file.read()
        if not content.startswith('code'):
            raise IOError('Unknown File Content')
except IOError:
    with open(result_file_path, 'w') as the_file:
        the_file.write('code, storename, width, height, size, url, filename, path, timestamp, ip, hash, delete\n')

clipboard = []

for f in sys.argv[1:]:
    print f
    i = str(f).strip('"')
    command = "curl https://sm.ms/api/upload -X POST -F smfile='@" + i + "'"
    try:
        s = subprocess.check_output(command, shell=True)
        j = json.loads(s)  # syntax error: A identifier can’t go after this “"”
        if j['code'] == 'success':
            print j
            d = j['data']
            content = '"{0}"'.format('", "'.join(str(x) for x in [[j['code'], d['storename'], d['width'], d['height'],
                                                                   d['size'], d['url'], d['filename'], d['path'],
                                                                   d['timestamp'], d['ip'], d['hash'], d['delete']]]))
            with open(result_file_path, 'a') as the_file:
                the_file.write(content + '\n')
            display_notification(d['filename'], 'Good! The Image is Uploaded', 'The image url has been copied!')
            clipboard.append(d['url'])
            subprocess.call('mkdir -p ' + result_image_path.replace(' ', '\\ '), shell=True)
            subprocess.call('mv ' + f.replace(' ', '\\ ') + ' ' +
                            result_image_path.replace(' ', '\\ ') + str(d['path'][1:]).replace('/', '-'), shell=True)
        elif j['code'] == 'error':
            print "The error message is %s" % j['msg']
            display_notification(j['msg'], 'Oops! Return Code is Error', 'Please choose the right image file...')
    except subprocess.CalledProcessError:
        print "The commnad %s returns a non-zero exit status" % command
        display_notification(command, 'Oops! Network (Curl) Error', 'The commnad returns a non-zero exit status...')
    except ValueError as e:
        print "The return data %s is not json format" % s
        print e  # use for debug
        display_notification(s, 'Oops! Return Data Error', 'The return data is not json format...')
        pass
    except Exception as e:
        print(e.message)
        display_notification(e.message, 'Oops! Unknown Exception', 'Please contact github@acbetter.com ...')

if len(clipboard) > 0:
    subprocess.call('echo "' + '\\n'.join(clipboard) + '" | pbcopy', shell=True)
