"""
Generic tools function
"""
import re
import zipfile
import os
import six

from opentmi_client.utils.exceptions import OpentmiException


def is_object_id(value):
    """
    Check if value is mongodb ObjectId
    :param value:
    :return: Boolean
    """
    if not isinstance(value, six.string_types):
        return False

    objectid_re = r"^[0-9a-fA-F]{24}$"
    match = re.match(objectid_re, value)
    return True if match else False


def resolve_host(host, port=None):
    """
    Resolve host from given arguments
    :param host: string
    :param port: number
    :return:
    """
    if port and port != 80:
        host += ":" + str(port)
    if not host.startswith("http"):
        host = "http://" + host
    return host

def archive_files(files, zip_filename, base_path=""):
    """
    Archive given files
    :param files: list of file names
    :param zip_filename: target zip filename
    :param base_path: base path for files
    :return:
    """
    zip_file = zipfile.ZipFile(zip_filename, "w")
    for filename in files:
        zip_file.write(os.path.join(base_path, filename), filename)
    zip_file.close()
    return zip_filename

def requires_logged_in(fn):
    """
    Decorator which verify that client are logged in
    if not but env variables are available
    it tries to loggin using them
    :param fn: function to decorated
    :return: wrapper function
    """
    def ret_fn(*args):
        self = args[0]
        self._try_login()
        return fn(*args)
    return ret_fn
