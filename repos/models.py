from django.db import models
from git import Repo
from base.settings import LOCAL_REPO_BASE_DIR


class GitRepo(models.Model):
    name = models.CharField(max_length=64)
    clone_url = models.URLField()

    def __str__(self):
        return self.name[:50]

    @property
    def local_path(self):
        return LOCAL_REPO_BASE_DIR + self.name

    def clone(self):
        try:
            Repo.clone_from(self.clone_url, self.local_path)
            print('Repo {} cloned!'.format(self.name))
            return True
        except (Exception,) as e:
            print('Repo {} clone failed with: {}'.format(self.name, e))
            return False

    def pull(self):
        try:
            repo = Repo(self.local_path)
            repo.git.pull()
            print('Repo {} updated!'.format(self.name))
            return True
        except (Exception,) as e:
            print('Repo {} pull failed with: {}'.format(self.name, e))
            return False

    def save(self, *args, **kwargs):
        self.clone()
        super().save(*args, **kwargs)
    
    
    
