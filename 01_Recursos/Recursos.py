
#TODO INPUT de tipo categoría que desempacamos para poder usar con la API de revit
categoria = UnwrapElement(IN[0])

#TODO Selección de todos los ejemplares por el id de la categoría
muros = FilteredElementCollector(doc).OfCategoryId(categoria.Id).WhereElementIsNotElementType().ToElements()

#TODO Selección por BuiltIn parameters

#* Selección de ejemplares y tipos
collectorMuros = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElements()

#* Selección de los tipos
collector_TiposMuros = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().ToElements()

#* Selección de los ejemplares
collector_EjemplaresMuros = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

#TODO Selección con filtro inverso
#* 1. Se crea un filtro inverso para posteriormente seleccionar todos los elementos que no pertenezcan a la categoria especificada. 
filtroInverso = ElementCategoryFilter(categoria.Id, True)

#* 2. FilteredElementCollector siempre seleccionará por defecto tanto a los ejemplares como a los tipos de la categoria.
collector_ElementosNoMuros = FilteredElementCollector(doc).WherePasses(filtroInverso).ToElements()


#TODO Seleccionar elementos a través de un filtro multicategoría.

#* 1. Crear lista fuertemente tipada
builtInCat = List[BuiltInCategory]()

#* 2. Se añaden varias categorias con BuiltIn Parameters
builtInCat.Add(BuiltInCategory.OST_Doors)
builtInCat.Add(BuiltInCategory.OST_Windows)

#* 3. Se crea filtro multicategoría
filtroBuiltIn = ElementMulticategoryFilter(builtInCat)

#* 4. Se seleccionan los ejemplares de las categorias especificadas
collector_Elements = FilteredElementCollector(doc).WherePasses(filtroBuiltIn).WhereElementIsNotElementType().ToElements()

#* 5. Se seleccionan los ejemplares obteniendo los ids
collector_ElementsIds = FilteredElementCollector(doc).WherePasses(filtroBuiltIn).WhereElementIsNotElementType().ToElementIds()


# TODO Selección por multicategoria a través de una ICollection

#* 1. Desempacar las categorias y obtener sus ids
listaCategorias = UnwrapElement(IN[1])

#* 2. Obtiene ids de cada categoria
listaCategoriasId = [c.Id for c in listaCategorias]

#* 3. Construir una ICollection de ElementIds
catId = List[ElementId](listaCategoriasId)

#* 4. Crear el filtro
filtroCat = ElementMulticategoryFilter(catId)

#* 5. Selección usando el filtro multicategorias. Esta vez seleccionamos ejemplares y tipos
collector_Elements2 = FilteredElementCollector(doc).WherePasses(filtroCat).ToElements()





OUT = muros, collectorMuros, collector_TiposMuros, collector_EjemplaresMuros, collector_ElementosNoMuros, collector_Elements, collector_ElementsIds, collector_Elements2