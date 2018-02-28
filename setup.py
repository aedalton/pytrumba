from setuptools import setup, find_packages

setup(name="pytrumba",
      description="Trumba API client",
      license="MIT",
      install_requires=["datetime", "requests","json"], # reqs txt
      author="Alexandra Dalton",
      author_email="alexandra@localprojects.com",
      url="http://github.com/aedalton/pytrumba",
      packages = find_packages(),
      keywords= "trumba",
      zip_safe = True
)
