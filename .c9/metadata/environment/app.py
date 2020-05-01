{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":60,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":418}],[{"start":{"row":61,"column":0},"end":{"row":68,"column":16},"action":"insert","lines":["#route and function to display the recipe name and title, and apply filters","@app.route('/browse_recipes', methods=[\"GET\", \"POST\"])","def browse_recipes():","    courses = mongo.db.course.find()","    cuisine = mongo.db.cuisine.find()","    recipes = mongo.db.recipes.find()","    allergens = mongo.db.allergens.find()","    filters = {}"],"id":419}],[{"start":{"row":68,"column":16},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":420},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":61,"column":1},"end":{"row":61,"column":19},"action":"remove","lines":["route and function"],"id":421},{"start":{"row":61,"column":1},"end":{"row":61,"column":2},"action":"insert","lines":["F"]},{"start":{"row":61,"column":2},"end":{"row":61,"column":3},"action":"insert","lines":["u"]},{"start":{"row":61,"column":3},"end":{"row":61,"column":4},"action":"insert","lines":["n"]},{"start":{"row":61,"column":4},"end":{"row":61,"column":5},"action":"insert","lines":["c"]},{"start":{"row":61,"column":5},"end":{"row":61,"column":6},"action":"insert","lines":["t"]},{"start":{"row":61,"column":6},"end":{"row":61,"column":7},"action":"insert","lines":["i"]},{"start":{"row":61,"column":7},"end":{"row":61,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["n"],"id":422}],[{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":[" "],"id":423},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["t"]},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["o"]}],[{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":[" "],"id":424}],[{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["a"],"id":425},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["n"]},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"insert","lines":[" "],"id":426},{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["r"]},{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["o"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["u"]},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":["t"]},{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"insert","lines":[" "],"id":427}],[{"start":{"row":61,"column":25},"end":{"row":61,"column":26},"action":"remove","lines":["o"],"id":428},{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"remove","lines":["t"]},{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"remove","lines":[" "]},{"start":{"row":61,"column":22},"end":{"row":61,"column":23},"action":"remove","lines":[" "]}],[{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"remove","lines":["e"],"id":429},{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"remove","lines":["h"]},{"start":{"row":61,"column":31},"end":{"row":61,"column":32},"action":"remove","lines":["t"]}],[{"start":{"row":61,"column":31},"end":{"row":61,"column":32},"action":"insert","lines":["a"],"id":430},{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"insert","lines":["l"]},{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"insert","lines":["l"]}],[{"start":{"row":61,"column":34},"end":{"row":61,"column":35},"action":"insert","lines":[" "],"id":431},{"start":{"row":61,"column":35},"end":{"row":61,"column":36},"action":"insert","lines":["p"]},{"start":{"row":61,"column":36},"end":{"row":61,"column":37},"action":"insert","lines":["l"]},{"start":{"row":61,"column":37},"end":{"row":61,"column":38},"action":"insert","lines":["a"]},{"start":{"row":61,"column":38},"end":{"row":61,"column":39},"action":"insert","lines":["y"]}],[{"start":{"row":61,"column":39},"end":{"row":61,"column":40},"action":"insert","lines":["g"],"id":432},{"start":{"row":61,"column":40},"end":{"row":61,"column":41},"action":"insert","lines":["r"]},{"start":{"row":61,"column":41},"end":{"row":61,"column":42},"action":"insert","lines":["o"]},{"start":{"row":61,"column":42},"end":{"row":61,"column":43},"action":"insert","lines":["u"]},{"start":{"row":61,"column":43},"end":{"row":61,"column":44},"action":"insert","lines":["n"]},{"start":{"row":61,"column":44},"end":{"row":61,"column":45},"action":"insert","lines":["d"]},{"start":{"row":61,"column":45},"end":{"row":61,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":62,"column":0},"end":{"row":68,"column":16},"action":"remove","lines":["@app.route('/browse_recipes', methods=[\"GET\", \"POST\"])","def browse_recipes():","    courses = mongo.db.course.find()","    cuisine = mongo.db.cuisine.find()","    recipes = mongo.db.recipes.find()","    allergens = mongo.db.allergens.find()","    filters = {}"],"id":433},{"start":{"row":62,"column":0},"end":{"row":69,"column":72},"action":"insert","lines":["# browse playground function","# @app.route('/')","# @app.route('/browse_playground', methods=[\"GET\", \"POST\"])","# def browse_playground():","#  borough_name = mongo.db.playgrounds.find(), playground_name = mongo.db.playgrounds.find()","# if request.method == \"POST\":","#     return render_template('browseplayground.html',","#                             playgrounds = mongo.db.playgrounds.find())"]}],[{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"remove","lines":["# "],"id":434},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"remove","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"remove","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"remove","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"remove","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"remove","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"remove","lines":["# "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":61,"column":30},"end":{"row":61,"column":31},"action":"insert","lines":["/"],"id":435},{"start":{"row":61,"column":31},"end":{"row":61,"column":32},"action":"insert","lines":["b"]},{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"insert","lines":["r"]},{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"insert","lines":["o"]}],[{"start":{"row":61,"column":34},"end":{"row":61,"column":35},"action":"insert","lines":["w"],"id":436},{"start":{"row":61,"column":35},"end":{"row":61,"column":36},"action":"insert","lines":["s"]},{"start":{"row":61,"column":36},"end":{"row":61,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":61,"column":54},"end":{"row":61,"column":94},"action":"remove","lines":["recipe name and title, and apply filters"],"id":437}],[{"start":{"row":62,"column":0},"end":{"row":62,"column":26},"action":"remove","lines":["browse playground function"],"id":438}],[{"start":{"row":61,"column":54},"end":{"row":62,"column":0},"action":"remove","lines":["",""],"id":439}],[{"start":{"row":65,"column":45},"end":{"row":66,"column":0},"action":"insert","lines":["",""],"id":440},{"start":{"row":66,"column":0},"end":{"row":66,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":60,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":441}],[{"start":{"row":67,"column":1},"end":{"row":67,"column":4},"action":"insert","lines":["   "],"id":442},{"start":{"row":66,"column":1},"end":{"row":66,"column":4},"action":"insert","lines":["   "]}],[{"start":{"row":34,"column":2},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":443},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":67,"column":38},"end":{"row":67,"column":39},"action":"remove","lines":["s"],"id":444},{"start":{"row":67,"column":37},"end":{"row":67,"column":38},"action":"remove","lines":["d"]},{"start":{"row":67,"column":36},"end":{"row":67,"column":37},"action":"remove","lines":["n"]},{"start":{"row":67,"column":35},"end":{"row":67,"column":36},"action":"remove","lines":["u"]},{"start":{"row":67,"column":34},"end":{"row":67,"column":35},"action":"remove","lines":["o"]},{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"remove","lines":["r"]},{"start":{"row":67,"column":32},"end":{"row":67,"column":33},"action":"remove","lines":["g"]},{"start":{"row":67,"column":31},"end":{"row":67,"column":32},"action":"remove","lines":["y"]},{"start":{"row":67,"column":30},"end":{"row":67,"column":31},"action":"remove","lines":["a"]},{"start":{"row":67,"column":29},"end":{"row":67,"column":30},"action":"remove","lines":["l"]},{"start":{"row":67,"column":28},"end":{"row":67,"column":29},"action":"remove","lines":["p"]}],[{"start":{"row":67,"column":28},"end":{"row":67,"column":29},"action":"insert","lines":["b"],"id":445},{"start":{"row":67,"column":29},"end":{"row":67,"column":30},"action":"insert","lines":["o"]},{"start":{"row":67,"column":30},"end":{"row":67,"column":31},"action":"insert","lines":["r"]},{"start":{"row":67,"column":31},"end":{"row":67,"column":32},"action":"insert","lines":["o"]}],[{"start":{"row":67,"column":28},"end":{"row":67,"column":32},"action":"remove","lines":["boro"],"id":446},{"start":{"row":67,"column":28},"end":{"row":67,"column":36},"action":"insert","lines":["boroughs"]}],[{"start":{"row":68,"column":49},"end":{"row":68,"column":51},"action":"insert","lines":["''"],"id":447}],[{"start":{"row":68,"column":49},"end":{"row":68,"column":51},"action":"remove","lines":["''"],"id":448}],[{"start":{"row":68,"column":49},"end":{"row":68,"column":50},"action":"insert","lines":[","],"id":449}],[{"start":{"row":68,"column":50},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":450},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":69,"column":4},"end":{"row":69,"column":5},"action":"insert","lines":["p"],"id":451},{"start":{"row":69,"column":5},"end":{"row":69,"column":6},"action":"insert","lines":["l"]},{"start":{"row":69,"column":6},"end":{"row":69,"column":7},"action":"insert","lines":["a"]},{"start":{"row":69,"column":7},"end":{"row":69,"column":8},"action":"insert","lines":["y"]}],[{"start":{"row":69,"column":8},"end":{"row":69,"column":9},"action":"insert","lines":["g"],"id":452},{"start":{"row":69,"column":9},"end":{"row":69,"column":10},"action":"insert","lines":["r"]},{"start":{"row":69,"column":10},"end":{"row":69,"column":11},"action":"insert","lines":["o"]},{"start":{"row":69,"column":11},"end":{"row":69,"column":12},"action":"insert","lines":["u"]},{"start":{"row":69,"column":12},"end":{"row":69,"column":13},"action":"insert","lines":["n"]},{"start":{"row":69,"column":13},"end":{"row":69,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":69,"column":14},"end":{"row":69,"column":15},"action":"insert","lines":["-"],"id":453}],[{"start":{"row":69,"column":14},"end":{"row":69,"column":15},"action":"remove","lines":["-"],"id":454}],[{"start":{"row":69,"column":14},"end":{"row":69,"column":15},"action":"insert","lines":["_"],"id":455},{"start":{"row":69,"column":15},"end":{"row":69,"column":16},"action":"insert","lines":["d"]}],[{"start":{"row":69,"column":16},"end":{"row":69,"column":17},"action":"insert","lines":["e"],"id":456},{"start":{"row":69,"column":17},"end":{"row":69,"column":18},"action":"insert","lines":["s"]},{"start":{"row":69,"column":18},"end":{"row":69,"column":19},"action":"insert","lines":["c"]},{"start":{"row":69,"column":19},"end":{"row":69,"column":20},"action":"insert","lines":["r"]},{"start":{"row":69,"column":20},"end":{"row":69,"column":21},"action":"insert","lines":["i"]},{"start":{"row":69,"column":21},"end":{"row":69,"column":22},"action":"insert","lines":["p"]}],[{"start":{"row":69,"column":22},"end":{"row":69,"column":23},"action":"insert","lines":["t"],"id":457},{"start":{"row":69,"column":23},"end":{"row":69,"column":24},"action":"insert","lines":["i"]},{"start":{"row":69,"column":24},"end":{"row":69,"column":25},"action":"insert","lines":["o"]},{"start":{"row":69,"column":25},"end":{"row":69,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":69,"column":26},"end":{"row":69,"column":27},"action":"insert","lines":[" "],"id":458},{"start":{"row":69,"column":27},"end":{"row":69,"column":28},"action":"insert","lines":["="]}],[{"start":{"row":69,"column":28},"end":{"row":69,"column":29},"action":"insert","lines":[" "],"id":459},{"start":{"row":69,"column":29},"end":{"row":69,"column":30},"action":"insert","lines":["m"]},{"start":{"row":69,"column":30},"end":{"row":69,"column":31},"action":"insert","lines":["o"]}],[{"start":{"row":69,"column":31},"end":{"row":69,"column":32},"action":"insert","lines":["n"],"id":460},{"start":{"row":69,"column":32},"end":{"row":69,"column":33},"action":"insert","lines":["g"]},{"start":{"row":69,"column":33},"end":{"row":69,"column":34},"action":"insert","lines":["o"]}],[{"start":{"row":69,"column":34},"end":{"row":69,"column":35},"action":"insert","lines":["."],"id":461},{"start":{"row":69,"column":35},"end":{"row":69,"column":36},"action":"insert","lines":["d"]},{"start":{"row":69,"column":36},"end":{"row":69,"column":37},"action":"insert","lines":["b"]}],[{"start":{"row":69,"column":37},"end":{"row":69,"column":38},"action":"insert","lines":["."],"id":462},{"start":{"row":69,"column":38},"end":{"row":69,"column":39},"action":"insert","lines":["p"]},{"start":{"row":69,"column":39},"end":{"row":69,"column":40},"action":"insert","lines":["l"]},{"start":{"row":69,"column":40},"end":{"row":69,"column":41},"action":"insert","lines":["a"]},{"start":{"row":69,"column":41},"end":{"row":69,"column":42},"action":"insert","lines":["y"]}],[{"start":{"row":69,"column":42},"end":{"row":69,"column":43},"action":"insert","lines":["g"],"id":463},{"start":{"row":69,"column":43},"end":{"row":69,"column":44},"action":"insert","lines":["r"]},{"start":{"row":69,"column":44},"end":{"row":69,"column":45},"action":"insert","lines":["o"]},{"start":{"row":69,"column":45},"end":{"row":69,"column":46},"action":"insert","lines":["u"]},{"start":{"row":69,"column":46},"end":{"row":69,"column":47},"action":"insert","lines":["n"]},{"start":{"row":69,"column":47},"end":{"row":69,"column":48},"action":"insert","lines":["d"]}],[{"start":{"row":69,"column":48},"end":{"row":69,"column":49},"action":"insert","lines":["s"],"id":464}],[{"start":{"row":69,"column":49},"end":{"row":69,"column":50},"action":"insert","lines":["."],"id":465},{"start":{"row":69,"column":50},"end":{"row":69,"column":51},"action":"insert","lines":["f"]},{"start":{"row":69,"column":51},"end":{"row":69,"column":52},"action":"insert","lines":["i"]},{"start":{"row":69,"column":52},"end":{"row":69,"column":53},"action":"insert","lines":["n"]}],[{"start":{"row":69,"column":53},"end":{"row":69,"column":54},"action":"insert","lines":["d"],"id":466}],[{"start":{"row":69,"column":54},"end":{"row":69,"column":56},"action":"insert","lines":["()"],"id":467}],[{"start":{"row":69,"column":56},"end":{"row":69,"column":57},"action":"insert","lines":[","],"id":468}],[{"start":{"row":69,"column":57},"end":{"row":70,"column":0},"action":"insert","lines":["",""],"id":469},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":70,"column":4},"end":{"row":70,"column":5},"action":"insert","lines":["s"],"id":470},{"start":{"row":70,"column":5},"end":{"row":70,"column":6},"action":"insert","lines":["t"]},{"start":{"row":70,"column":6},"end":{"row":70,"column":7},"action":"insert","lines":["a"]},{"start":{"row":70,"column":7},"end":{"row":70,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":70,"column":4},"end":{"row":70,"column":8},"action":"remove","lines":["star"],"id":471},{"start":{"row":70,"column":4},"end":{"row":70,"column":15},"action":"insert","lines":["star_rating"]}],[{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"insert","lines":[" "],"id":472},{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":70,"column":17},"end":{"row":70,"column":18},"action":"insert","lines":[" "],"id":473},{"start":{"row":70,"column":18},"end":{"row":70,"column":19},"action":"insert","lines":["m"]}],[{"start":{"row":70,"column":19},"end":{"row":70,"column":20},"action":"insert","lines":["o"],"id":474},{"start":{"row":70,"column":20},"end":{"row":70,"column":21},"action":"insert","lines":["n"]},{"start":{"row":70,"column":21},"end":{"row":70,"column":22},"action":"insert","lines":["g"]}],[{"start":{"row":70,"column":18},"end":{"row":70,"column":22},"action":"remove","lines":["mong"],"id":475},{"start":{"row":70,"column":18},"end":{"row":70,"column":23},"action":"insert","lines":["mongo"]}],[{"start":{"row":70,"column":23},"end":{"row":70,"column":24},"action":"insert","lines":["."],"id":476},{"start":{"row":70,"column":24},"end":{"row":70,"column":25},"action":"insert","lines":["d"]},{"start":{"row":70,"column":25},"end":{"row":70,"column":26},"action":"insert","lines":["b"]}],[{"start":{"row":70,"column":26},"end":{"row":70,"column":27},"action":"insert","lines":["."],"id":477},{"start":{"row":70,"column":27},"end":{"row":70,"column":28},"action":"insert","lines":["p"]},{"start":{"row":70,"column":28},"end":{"row":70,"column":29},"action":"insert","lines":["l"]}],[{"start":{"row":70,"column":27},"end":{"row":70,"column":29},"action":"remove","lines":["pl"],"id":478},{"start":{"row":70,"column":27},"end":{"row":70,"column":38},"action":"insert","lines":["playgrounds"]}],[{"start":{"row":70,"column":38},"end":{"row":70,"column":39},"action":"insert","lines":["."],"id":479},{"start":{"row":70,"column":39},"end":{"row":70,"column":40},"action":"insert","lines":["f"]}],[{"start":{"row":70,"column":39},"end":{"row":70,"column":40},"action":"remove","lines":["f"],"id":480},{"start":{"row":70,"column":39},"end":{"row":70,"column":43},"action":"insert","lines":["find"]}],[{"start":{"row":70,"column":43},"end":{"row":70,"column":45},"action":"insert","lines":["()"],"id":481}],[{"start":{"row":70,"column":45},"end":{"row":70,"column":46},"action":"insert","lines":[","],"id":482}],[{"start":{"row":70,"column":46},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":483},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":70,"column":46},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":484},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":71,"column":4},"end":{"row":71,"column":13},"action":"insert","lines":["image_url"],"id":485}],[{"start":{"row":71,"column":13},"end":{"row":71,"column":14},"action":"insert","lines":[" "],"id":486},{"start":{"row":71,"column":14},"end":{"row":71,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":71,"column":15},"end":{"row":71,"column":16},"action":"insert","lines":[" "],"id":487},{"start":{"row":71,"column":16},"end":{"row":71,"column":17},"action":"insert","lines":["m"]},{"start":{"row":71,"column":17},"end":{"row":71,"column":18},"action":"insert","lines":["o"]}],[{"start":{"row":71,"column":17},"end":{"row":71,"column":18},"action":"remove","lines":["o"],"id":488},{"start":{"row":71,"column":16},"end":{"row":71,"column":17},"action":"remove","lines":["m"]}],[{"start":{"row":71,"column":16},"end":{"row":71,"column":44},"action":"insert","lines":["mongo.db.playgrounds.find(),"],"id":489}],[{"start":{"row":71,"column":43},"end":{"row":71,"column":44},"action":"remove","lines":[","],"id":490}],[{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["# "],"id":491},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["# "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"insert","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["# "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":2},"action":"insert","lines":["# "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"insert","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["s"],"id":492},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["k"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["s"]},{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["a"]},{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":["t"]}],[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"insert","lines":["p"],"id":493},{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"insert","lines":["l"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["a"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["y"]}],[{"start":{"row":26,"column":27},"end":{"row":26,"column":31},"action":"remove","lines":["play"],"id":494},{"start":{"row":26,"column":27},"end":{"row":26,"column":38},"action":"insert","lines":["playgrounds"]}],[{"start":{"row":63,"column":0},"end":{"row":63,"column":1},"action":"remove","lines":["#"],"id":495},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"remove","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"remove","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"remove","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"remove","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"remove","lines":["# "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"remove","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"remove","lines":["# "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":2},"action":"remove","lines":["# "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"remove","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"remove","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":75,"column":28},"end":{"row":75,"column":32},"action":"insert","lines":["    "],"id":496},{"start":{"row":74,"column":4},"end":{"row":74,"column":8},"action":"insert","lines":["    "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":75,"column":32},"end":{"row":75,"column":36},"action":"insert","lines":["    "],"id":497},{"start":{"row":74,"column":8},"end":{"row":74,"column":12},"action":"insert","lines":["    "]},{"start":{"row":73,"column":4},"end":{"row":73,"column":8},"action":"insert","lines":["    "]}],[{"start":{"row":75,"column":32},"end":{"row":75,"column":36},"action":"remove","lines":["    "],"id":498},{"start":{"row":75,"column":28},"end":{"row":75,"column":32},"action":"remove","lines":["    "]},{"start":{"row":75,"column":24},"end":{"row":75,"column":28},"action":"remove","lines":["    "]},{"start":{"row":75,"column":20},"end":{"row":75,"column":24},"action":"remove","lines":["    "]}],[{"start":{"row":73,"column":4},"end":{"row":73,"column":8},"action":"remove","lines":["    "],"id":499}],[{"start":{"row":74,"column":8},"end":{"row":74,"column":12},"action":"remove","lines":["    "],"id":500},{"start":{"row":74,"column":4},"end":{"row":74,"column":8},"action":"remove","lines":["    "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "],"id":501}],[{"start":{"row":74,"column":4},"end":{"row":74,"column":8},"action":"insert","lines":["    "],"id":502}],[{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["# "],"id":503}],[{"start":{"row":75,"column":62},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":504},{"start":{"row":76,"column":0},"end":{"row":76,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":76,"column":16},"end":{"row":76,"column":20},"action":"remove","lines":["    "],"id":505},{"start":{"row":76,"column":12},"end":{"row":76,"column":16},"action":"remove","lines":["    "]},{"start":{"row":76,"column":8},"end":{"row":76,"column":12},"action":"remove","lines":["    "]},{"start":{"row":76,"column":4},"end":{"row":76,"column":8},"action":"remove","lines":["    "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"remove","lines":["    "]},{"start":{"row":75,"column":62},"end":{"row":76,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"remove","lines":["r"],"id":506},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"remove","lines":[" "]},{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"remove","lines":["d"]},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"remove","lines":["n"]},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"remove","lines":["a"]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"remove","lines":[" "]},{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"remove","lines":["s"]},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"remove","lines":["t"]},{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"remove","lines":["c"]},{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"remove","lines":["e"]},{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"remove","lines":["l"]},{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"remove","lines":["e"]},{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"remove","lines":["S"]}],[{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"insert","lines":["R"],"id":507}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":["#"],"id":508}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["\""],"id":509},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["\""]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["\""]}],[{"start":{"row":39,"column":73},"end":{"row":39,"column":74},"action":"insert","lines":["\""],"id":510},{"start":{"row":39,"column":74},"end":{"row":39,"column":75},"action":"insert","lines":["\""]},{"start":{"row":39,"column":75},"end":{"row":39,"column":76},"action":"insert","lines":["\""]}],[{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"remove","lines":["e"],"id":511},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["h"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"remove","lines":["t"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"remove","lines":[" "]}],[{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["s"],"id":512}],[{"start":{"row":49,"column":4},"end":{"row":49,"column":5},"action":"remove","lines":["#"],"id":513}],[{"start":{"row":49,"column":4},"end":{"row":49,"column":5},"action":"insert","lines":["\""],"id":514},{"start":{"row":49,"column":5},"end":{"row":49,"column":6},"action":"insert","lines":["\""]},{"start":{"row":49,"column":6},"end":{"row":49,"column":7},"action":"insert","lines":["\""]}],[{"start":{"row":49,"column":65},"end":{"row":49,"column":66},"action":"insert","lines":["\""],"id":515},{"start":{"row":49,"column":66},"end":{"row":49,"column":67},"action":"insert","lines":["\""]},{"start":{"row":49,"column":67},"end":{"row":49,"column":68},"action":"insert","lines":["\""]}],[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":["g"],"id":516}],[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["G"],"id":529}],[{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":530}]]},"ace":{"folds":[],"scrolltop":1003,"scrollleft":0,"selection":{"start":{"row":45,"column":0},"end":{"row":45,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1588308810782,"hash":"3684b5f63027145d3a5fee8c964d3116f4725228"}