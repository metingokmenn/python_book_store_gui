import glob


class I18N:
    def __init__(self, language, load_from_file=True):
        if load_from_file:
            if language in self.get_available_languages():
                self.load_data_from_file(language)
            else:
                raise NotImplementedError("Unsupported language. Add missing language file.")
        else:
            if language == "en":
                self.load_data_in_english()
            elif language == "tr":
                self.load_data_in_turkish()
            else:
                raise NotImplementedError("Unsupported language.")

    def load_data_in_english(self):
        self.logintitle = "Login"
        self.maintitle = "Main Screen"
        self.abptitle = "Add Book Page"
        self.ebptitle = "Edit Book Page"
        self.aaptitle = "Add Author Page"
        self.eaptitle = "Edit Author Page"
        self.sptitle = "Search Page"
        self.username = "User Name"
        self.password = "Password"
        self.login = "Login"
        self.ID = "ID"
        self.bookname = "Book Name"
        self.authorname = "Author Name"
        self.addbook = "Add Book"
        self.editbook = "Edit Book"
        self.deletebook = "Delete Book"
        self.addauthor = "Add Author"
        self.editauthor = "Edit Author"
        self.deleteauthor = "Delete Author"
        self.search = "Search"
        self.authorid = "Author ID"
        self.submitchanges = "Submit Changes"
        self.name = "Name"
        self.cleardatabase = "Clear Database"
        self.bookid = "Book ID"
        self.error = "Error"
        self.errmessage = "An error occured"
        

    def load_data_in_turkish(self):
        self.logintitle = "Giriş"
        self.maintitle = "Ana Ekran"
        self.abptitle = "Kitap Ekleme"
        self.ebptitle = "Kitap Düzenle"
        self.aaptitle = "Yazar Ekle"
        self.eaptitle = "Yazar Düzenle"
        self.sptitle = "Arama"
        self.username = "Kullanıcı Adı"
        self.password = "Şifre"
        self.login = "Giriş Yap"
        self.ID = "ID"
        self.bookname = "Kitap Adı"
        self.authorname = "Yazar Adı"
        self.addbook = "Kitap Ekle"
        self.editbook = "Kitap Düzenle"
        self.deletebook = "Kitap Sil"
        self.addauthor = "Yazar Ekle"
        self.editauthor = "Yazar Düzenle"
        self.deleteauthor = "Yazar Sil"
        self.search = "Ara"
        self.authorid = "Yazar ID"
        self.submitchanges = "Değişiklikleri Kaydet"
        self.name = "Ad"
        self.cleardatabase = "Tüm yazar ve kitapları sil"
        self.bookid = "Kitap ID"
        self.error = "Hata"
        self.errmessage = "Bir hata oluştu"

    def load_data_from_file(self, lang):
        lang_data = {}
        lang_file = f"data_{lang}.lng"
        with open(file=lang_file, encoding="utf-8") as f:
            for line in f:
                (key, val) = line.strip().split("=")
                lang_data[key] = val
                
        self.logintitle = lang_data["logintitle"]
        self.maintitle = lang_data["maintitle"]
        self.abptitle = lang_data["abptitle"]
        self.ebptitle = lang_data["ebptitle"]
        self.aaptitle = lang_data["aaptitle"]
        self.eaptitle = lang_data["eaptitle"]
        self.sptitle = lang_data["sptitle"]
        self.username = lang_data["username"]
        self.password = lang_data["password"]
        self.login = lang_data["login"]
        self.ID = lang_data["ID"]
        self.bookname = lang_data["bookname"]
        self.authorname = lang_data["authorname"]
        self.addbook = lang_data["addbook"]
        self.editbook = lang_data["editbook"]
        self.deletebook = lang_data["deletebook"]
        self.addauthor = lang_data["addauthor"]
        self.editauthor = lang_data["editauthor"]
        self.deleteauthor = lang_data["deleteauthor"]
        self.search = lang_data["search"]
        self.authorid = lang_data["authorid"]
        self.submitchanges = lang_data["submitchanges"]
        self.name = lang_data["name"]
        self.cleardatabase = lang_data["cleardatabase"]
        self.bookid = lang_data["bookid"]
        self.error = lang_data["error"]
        self.errmessage = lang_data["errmessage"]

    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")
        language_codes = []

        for f in language_files:
            language_code = f.replace("data_", "").replace(".lng", "")
            language_codes.append(language_code)

        return language_codes