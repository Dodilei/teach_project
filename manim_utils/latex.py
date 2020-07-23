import os
from manimlib.imports import *

def make_new_tex_temp(TEMPLATE, *packages):
  new_packs = ""

  for p in packages:
    new_packs += "\n\\usepackage{%s}" % p

  return (TEMPLATE[:35] + new_packs + TEMPLATE[36:])


class CustomTMobject(TextMobject):
    CONFIG = {}

    def __init__(self, *packages):
        
        self.template = make_new_tex_temp(TEMPLATE_TEX_FILE_BODY, *packages)

        self.CONFIG["template_tex_file_body"] = self.template
        

    def generate(self, *args, **kwargs):

        digest_config(self,
            {**kwargs, "template_tex_file_body": self.template}
        )

        TextMobject.__init__(self,
            *args,
            template_tex_file_body = self.template,
            **kwargs)

        return self



