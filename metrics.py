font_title=("Helvetica","14","bold")
font_label=("Helvetica","12")
font_combo=("Helvetica","10")

label_xy=[
    [77,2],
    [171,26],
    [239,26],
    [370,26],
    [615,2]
]

sizes=[
    [4,13],
    [4,10],
    [4,10],
    [4,10],
    [4,13]
]

colors_list=('black','brown','red','orange','yellow','green','blue','purple','gray','white')
colors_tolerance=('golden','silver')

e_category={
    'silver':{
        'serie':12,
        'values':[1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2] 
    },
    'golden':{
        'serie':24,
        'values':[1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.2, 8.2, 9.1]
    }
}

tolerance_porcent={
    24:0.05,
    12:0.1
}

scales={
    3:'K',
    6:'M',
    9:'G'
}

hex_color={
    'black':'#000',
    'brown':'#964B00',
    'red':'#f00',
    'orange':'#ffa500',
    'yellow':'#ff0',
    'green':'#008000',
    'blue':'#00f',
    'purple':'#800080',
    'gray':'#808080',
    'white':'#fff',
    'golden':'#ffd700',
    'silver':'#c0c0c0'
}

colors_values={
    'black':0,
    'brown':1,
    'red':2,
    'orange':3,
    'yellow':4,
    'green':5,
    'blue':6,
    'purple':7,
    'gray':8,
    'white':9,
}

test_torelance_values={
    'brown':'±1%',
    'red':'±2%',
    'green':'±0.5%',
    'blue':'±0.25',
    'purple':'±0.1%',
    'gray':'±0.05%',
    'golden':'±5',
    'silver':'±10'
}

torelance_values={
    'golden':'±5',
    'silver':'±10'
}

E12_serie=[1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]#silver

E24_serie=[1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
            3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.2, 8.2, 9.1]#golden
paths={
    '4':'./resourses/4_stripes.png',
    '5':'./resourses/5_stripes.png'
}

label_text=[
    'Color stripe\n1',
    'Color stripe\n2',
    'Color stripe\n3',
    'Color stripe\nmultiplicator',
    'Color strip\ntolerence',
]