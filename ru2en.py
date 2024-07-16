import codecs
import argostranslate.package
import argostranslate.translate
import translatehtml

from_code = "ru"
to_code = "en"
ru_html = f"docs/{from_code}.html"
en_html = f"docs/{to_code}.html"

print('Downloading and installing Argos Translate package...')
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
download_path = available_package.download()
argostranslate.package.install_from_path(download_path)

installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(lambda x: x.code == from_code, installed_languages))[0]
to_lang = list(filter(lambda x: x.code == to_code, installed_languages))[0]
translation = from_lang.get_translation(to_lang)

with codecs.open(ru_html, mode="r", encoding="UTF-8") as ru_html_id:
    html_doc = ru_html_id.read()
    print(f"Translating '{ru_html}'...")
    translated_soup = translatehtml.translate_html(translation, html_doc)
    print(f"Saved to file '{en_html}'")
    with codecs.open(en_html, "w", encoding="UTF-8") as en_html_id:
        en_html_id.write(str(translated_soup))
