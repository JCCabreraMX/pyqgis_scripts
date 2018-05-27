#Add rgb color field
vLayer = iface.activeLayer()

fields = []
fields.append(QgsField('color_rgb', QVariant.String)) #Name and data type of field to add for storing rgb color value
vLayer.dataProvider().addAttributes(fields)
vLayer.updateFields()

#Add color value to color rgb field
prefix = "'"
layer = iface.activeLayer()
attr = layer.renderer().classAttribute()
attrColor = 'color_rgb' # Name of the field to store rgb color value
fieldIndex = layer.dataProvider().fieldNameIndex(attrColor)
attrFeatMap = {}

for cat in layer.renderer().categories(): 
  expr = "\""+attr+"\"="+prefix+unicode(cat.value())+prefix
  for f in layer.getFeatures(QgsFeatureRequest(QgsExpression(expr))):
    attrMap = { fieldIndex :str(cat.symbol().color().red()) +','+ str(cat.symbol().color().green()) +','+ str(cat.symbol().color().blue())}
    attrFeatMap[ f.id() ] = attrMap

layer.dataProvider().changeAttributeValues( attrFeatMap )