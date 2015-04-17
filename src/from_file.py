
SHORT_VERSION_PY = """
# This file was generated by 'versioneer.py' (@VERSIONEER-VERSION@) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

version_version = '%(version)s'
version_full = '%(full)s'
def get_versions(verbose=False):
    return {'version': version_version, 'full': version_full}

"""


def versions_from_file(filename):
    versions = {}
    try:
        with open(filename) as f:
            for line in f.readlines():
                mo = re.match("version_version = '([^']+)'", line)
                if mo:
                    versions["version"] = mo.group(1)
                mo = re.match("version_full = '([^']+)'", line)
                if mo:
                    versions["full"] = mo.group(1)
    except EnvironmentError:
        return {}

    return versions


def write_to_version_file(filename, versions):
    with open(filename, "w") as f:
        f.write(SHORT_VERSION_PY % versions)

    print("set %s to '%s'" % (filename, versions["version"]))

