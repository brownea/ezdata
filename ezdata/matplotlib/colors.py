try: 
    basestring
except:
    basestring = str
        
from matplotlib import colors
from matplotlib.colors import LinearSegmentedColormap


# Lookup of web color names to their hex codes.
COLOR_LOOKUP = {'aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7',
                'aqua': '#00FFFF', 'aquamarine': '#7FFFD4',
                'azure': '#F0FFFF', 'beige': '#F5F5DC',
                'bisque': '#FFE4C4', 'black': '#000000',
                'blanchedalmond': '#FFEBCD', 'blue': '#0000FF',
                'blueviolet': '#8A2BE2', 'brown': '#A52A2A',
                'burlywood': '#DEB887', 'cadetblue': '#5F9EA0',
                'chartreuse': '#7FFF00', 'chocolate': '#D2691E',
                'coral': '#FF7F50', 'cornflowerblue': '#6495ED',
                'cornsilk': '#FFF8DC', 'crimson': '#DC143C',
                'cyan': '#00FFFF', 'darkblue': '#00008B',
                'darkcyan': '#008B8B', 'darkgoldenrod': '#B8860B',
                'darkgray': '#A9A9A9', 'darkgreen': '#006400',
                'darkgrey': '#A9A9A9', 'darkkhaki': '#BDB76B',
                'darkmagenta': '#8B008B', 'darkolivegreen': '#556B2F',
                'darkorange': '#FF8C00', 'darkorchid': '#9932CC',
                'darkred': '#8B0000', 'darksage': '#598556',
                'darksalmon': '#E9967A', 'darkseagreen': '#8FBC8F',
                'darkslateblue': '#483D8B', 'darkslategray': '#2F4F4F',
                'darkslategrey': '#2F4F4F', 'darkturquoise': '#00CED1',
                'darkviolet': '#9400D3', 'deeppink': '#FF1493',
                'deepskyblue': '#00BFFF', 'dimgray': '#696969',
                'dimgrey': '#696969', 'dodgerblue': '#1E90FF',
                'firebrick': '#B22222', 'floralwhite': '#FFFAF0',
                'forestgreen': '#228B22', 'fuchsia': '#FF00FF',
                'gainsboro': '#DCDCDC', 'ghostwhite': '#F8F8FF',
                'gold': '#FFD700', 'goldenrod': '#DAA520',
                'gray': '#808080', 'green': '#008000',
                'greenyellow': '#ADFF2F', 'grey': '#808080',
                'honeydew': '#F0FFF0', 'hotpink': '#FF69B4',
                'indianred': '#CD5C5C', 'indigo': '#4B0082',
                'ivory': '#FFFFF0', 'khaki': '#F0E68C',
                'lavender': '#E6E6FA', 'lavenderblush': '#FFF0F5',
                'lawngreen': '#7CFC00', 'lemonchiffon': '#FFFACD',
                'lightblue': '#ADD8E6', 'lightcoral': '#F08080',
                'lightcyan': '#E0FFFF', 'lightgoldenrodyellow': '#FAFAD2',
                'lightgray': '#D3D3D3', 'lightgreen': '#90EE90',
                'lightgrey': '#D3D3D3', 'lightpink': '#FFB6C1',
                'lightsage': '#BCECAC', 'lightsalmon': '#FFA07A',
                'lightseagreen': '#20B2AA', 'lightskyblue': '#87CEFA',
                'lightslategray': '#778899', 'lightslategrey': '#778899',
                'lightsteelblue': '#B0C4DE', 'lightyellow': '#FFFFE0',
                'lime': '#00FF00', 'limegreen': '#32CD32',
                'linen': '#FAF0E6', 'magenta': '#FF00FF',
                'maroon': '#800000', 'mediumaquamarine': '#66CDAA',
                'mediumblue': '#0000CD', 'mediumorchid': '#BA55D3',
                'mediumpurple': '#9370DB', 'mediumseagreen': '#3CB371',
                'mediumslateblue': '#7B68EE', 'mediumspringgreen': '#00FA9A',
                'mediumturquoise': '#48D1CC', 'mediumvioletred': '#C71585',
                'midnightblue': '#191970', 'mintcream': '#F5FFFA',
                'mistyrose': '#FFE4E1', 'moccasin': '#FFE4B5',
                'navajowhite': '#FFDEAD', 'navy': '#000080',
                'oldlace': '#FDF5E6', 'olive': '#808000',
                'olivedrab': '#6B8E23', 'orange': '#FFA500',
                'orangered': '#FF4500', 'orchid': '#DA70D6',
                'palegoldenrod': '#EEE8AA', 'palegreen': '#98FB98',
                'paleturquoise': '#AFEEEE', 'palevioletred': '#DB7093',
                'papayawhip': '#FFEFD5', 'peachpuff': '#FFDAB9',
                'peru': '#CD853F', 'pink': '#FFC0CB',
                'plum': '#DDA0DD', 'powderblue': '#B0E0E6',
                'purple': '#800080', 'red': '#FF0000',
                'rosybrown': '#BC8F8F', 'royalblue': '#4169E1',
                'saddlebrown': '#8B4513', 'sage': '#87AE73',
                'salmon': '#FA8072', 'sandybrown': '#FAA460',
                'seagreen': '#2E8B57', 'seashell': '#FFF5EE',
                'sienna': '#A0522D', 'silver': '#C0C0C0',
                'skyblue': '#87CEEB', 'slateblue': '#6A5ACD',
                'slategray': '#708090', 'slategrey': '#708090',
                'snow': '#FFFAFA', 'springgreen': '#00FF7F',
                'steelblue': '#4682B4', 'tan': '#D2B48C',
                'teal': '#008080', 'thistle': '#D8BFD8',
                'tomato': '#FF6347', 'turquoise': '#40E0D0',
                'violet': '#EE82EE', 'wheat': '#F5DEB3',
                'white': '#FFFFFF', 'whitesmoke': '#F5F5F5',
                'yellow': '#FFFF00', 'yellowgreen': '#9ACD32'}

OTHER_COLORS = (colors.BASE_COLORS, colors.CSS4_COLORS, 
                colors.TABLEAU_COLORS, colors.XKCD_COLORS)


def hex_to_rgb(x):
    """Convert a color hexcode to an rgb tuple.
    Example
    -------
    >>> rgb('#FFFFFF')
    (255, 255, 255)
    """
    if not (x.startswith('#') and len(x) == 7):
        raise ValueError("Invalid hex color")
    x = x.strip('#')
    try:
        return (int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16))
    except ValueError:
        raise ValueError("Invalid hex color")


def rgb(x):
    """Return a triple representing rgb color.
    Can convert colors by name or hexcode. Passing in a valid rgb tuple is
    idempotent.
    Example
    -------
    >>> rgb('plum')
    (221, 160, 221)
    >>> rgb('#FFFFFF')
    (255, 255, 255)
    >>> rgb((255, 255, 255))
    (255, 255, 255)
    """
    if isinstance(x, basestring):
        if x.startswith('#'):
            return hex_to_rgb(x)
        elif x in COLOR_LOOKUP:
            return hex_to_rgb(COLOR_LOOKUP[x])
        else:
            for registered in OTHER_COLORS:
                try:
                    return tuple(int(k * 256) for k in registered[x])
                except KeyError:
                    pass
            raise ValueError("Unknown color: '{0}'".format(x))
    elif isinstance(x, tuple) and len(x) == 3:
        if min(x) < 0 or max(x) > 255:
            raise ValueError("Invalid RGB tuple")
    else:
        raise TypeError("Don't know how to convert {0} to RGB".format(x))
    return x

def normed_rgb(x):
    return tuple(k / 256. for k in rgb(x))

#   Example palettes

# Copied from from bokeh.palettes.Greys9
Greys9 = ["#000000", "#252525", "#525252", "#737373", "#969696", 
          "#bdbdbd", "#d9d9d9", "#f0f0f0", "#ffffff"]

# Adapted from matplotlib.cm.hot to be more uniform at the high end
Hot = ["black", "maroon", "darkred", "red", "orangered", "darkorange", 
       "orange", "gold", "yellow", "white"]

# pseudo terrestial elevation ramp
Elevation = ["aqua", "sandybrown", "limegreen", "green", "green", "darkgreen",
             "saddlebrown", "gray", "white"]


def generate_cmap_from_colors(seq, N=256, name='user'):
    """ Make a color map from registered colors or rgb or hex values"""
    if isinstance(seq, basestring):
        values = ('w', normed_rgb(seq))
    else:
        values = [normed_rgb(k) for k in seq]
        return LinearSegmentedColormap.from_list(name, seq, N=256)
