import re
import socket
import zipfile
import os
import six


def is_object_id(value):
    if not isinstance(value, six.string_types):
        return False

    objectid_re = "^[0-9a-fA-F]{24}$"
    m = re.match(objectid_re, value)
    return True if m else False


def resolve_host(host="localhost", port=None):
    """resolve host url
    """
    ip = None
    _host = None
    if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d{2,5})?$", host):
        ip = host
    elif re.match("^https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d{2,5})?$", host):
        _host = host
    else:
        ip = socket.gethostbyname(host)
    if ip:
        # 'http://1.2.3.4:3000'
        _host = 'http://'+ip
    if port and port != 80:
        _host += ":" + str(port)
    return _host


def archive_files(files, zip_filename, files_path=""):
    zf = zipfile.ZipFile(zip_filename, "w")
    for filename in files:
        zf.write(os.path.join(files_path, filename), filename)
    zf.close()
    return zip_filename
