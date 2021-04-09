from modulefinder import ModuleFinder
finder = ModuleFinder()
finder.run_script("index.py")
for name, mod in finder.modules.items():
    print(name)