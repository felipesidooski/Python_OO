class ConstruturElemento:
    # Inicializador
    def __init__(self, hostname, vendor, loopback):
        self._hostname = hostname
        self._vendor = vendor
        self._loopback = loopback

    @property
    def hostname(self):
        return self._hostname

    @property
    def loopback(self):
        return self._loopback

    @property
    def vendor(self):
        return self._vendor

    @hostname.setter
    def hostname(self, novo_hostname):
        self._hostname = novo_hostname

    @vendor.setter
    def vendor(self, novo_vendor):
        self._vendor = novo_vendor

    @loopback.setter
    def loopback(self, novo_loopback):
        self._loopback = novo_loopback



class ConstrutorOLT(ConstruturElemento):
    #Inicializador
    def __init__(self, hostname, vendor, loopback, ardHostname):
        super().__init__(hostname, vendor, loopback)
        self._ardHostname = ardHostname

    @property
    def ardHostname(self):
        return self._ardHostname

    @ardHostname.setter
    def ardHostname(self, novo_hostname):
        self._ardHostname = novo_hostname

    #Como reescrever o setter default da classe pai
    #@loopback.setter
    #def loopback(self, novo_loopback):
    #    super(ConstrutorOLT, self.__class__).loopback.__set__(self, novo_loopback)



class ConstrutorHL(ConstruturElemento):
    def __init__(self, hostname, loopback, vendor):
        super().__init__(hostname, loopback, vendor)

