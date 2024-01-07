from IPython.display import Image, IFrame, display

class Photo(Image):
    
    def __init__(self, name):
        url = photo_links.get(name)
        super().__init__(url=url,width=200,height=200,)
        

        
photo_links = {
'de Broglie':'https://cdn.britannica.com/s:1500x700,q:85/09/21109-004-2172F5F5/Louis-Victor-Broglie-1958.jpg',
'Rutherford':'https://cdn.britannica.com/43/102243-050-15D49DEF/Ernest-Rutherford.jpg',
'Rosen':'https://upload.wikimedia.org/wikipedia/en/d/d7/NathanRosen.jpg', 
'Podolsky':'https://www.ias.edu/sites/default/files/styles/basic_scholar/public/images/scholars/Boris.jpg', 
'Bohr':'https://cdn.britannica.com/s:300x1000/14/21114-004-FA0334F4/Niels-Bohr.jpg', 
'Bell':'https://upload.wikimedia.org/wikipedia/en/a/a5/JohnStewartBell.jpg', 
'Einstein':'https://cdn.britannica.com/09/75509-050-86D8CBBF/Albert-Einstein.jpg', 
'Plank':'https://cdn.britannica.com/s:300x1000/73/20973-050-F6EEBFF1/Max-Planck.jpg', 
'Heisenberg':'https://cdn.britannica.com/67/43167-004-A4FAD96F/Werner-Heisenberg.jpg', 
'Jordan':'https://upload.wikimedia.org/wikipedia/commons/a/a6/Pascual_Jordan_1920s.jpg', 
'Born':'https://cdn.britannica.com/24/13124-004-E329BF69/Max-Born.jpg', 
'Dirac':'https://cdn.britannica.com/66/91766-004-CE5A2E61/PAM-Dirac.jpg', 
'Pauli':'https://cdn.britannica.com/80/20980-004-2BC7E745/Wolfgang-Pauli-1945.jpg', 
'Stern':'https://cdn.britannica.com/06/134706-050-755B4B38/Otto-Stern-presentation-Nobel-Prizes-New-York-1943.jpg',
'Gerlach':'https://upload.wikimedia.org/wikipedia/en/9/9e/Walther_Gerlach.jpg',
'Wien':'https://cdn.britannica.com/47/8747-004-A1104E40/Wien.jpg',
'Kramers':'https://upload.wikimedia.org/wikipedia/commons/b/b4/Kramers_1928.jpg',
'Sommerfeld':'https://upload.wikimedia.org/wikipedia/commons/7/74/Sommerfeld1897.gif',
'Wilson':'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/William_Wilson_Academic.jpg/517px-William_Wilson_Academic.jpg',
'Schrodinger':'https://cdn.britannica.com/16/198816-050-AF8B7B3C/Erwin-Schrodinger.jpg',
'von Neumann':'https://cdn.britannica.com/23/26823-050-E778F3DF/John-von-Neumann.jpg'
}

experiment_link = {'Stern-Gerlach':'https://plato.stanford.edu/entries/physics-experiment/figure13.jpg'}