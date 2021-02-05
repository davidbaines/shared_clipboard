# Adding Linux Support will require supporting at least GNOME and KDE, the most popular Linux windows managers. 

# You can access Gnome's clipboard using pygtk and KDE's clipboard using pyqt. 

# Another option is to require that the target machines have xsel or xclip, which work very much like pbcopy/pbpaste and implement Linux clipboard support on top of those.

import pygtk
