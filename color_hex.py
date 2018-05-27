#Hex color format
#Add hex color field
vLayer = iface.activeLayer()

fields = []
fields.append(QgsField('color_hex', QVariant.String)) #Name and data type of field to add for storing hex color value
vLayer.dataProvider().addAttributes(fields)
vLayer.updateFields()


#Add color value to color field

prefix = "'"
layer = iface.activeLayer()
attr = layer.renderer().classAttribute()
attrColor = 'color_hex' # Name of the field to store hex color value
fieldIndex = layer.dataProvider().fieldNameIndex(attrColor)
attrFeatMap = {}

for cat in layer.renderer().categories(): 
  expr = "\""+attr+"\"="+prefix+unicode(cat.value())+prefix
  for f in layer.getFeatures(QgsFeatureRequest(QgsExpression(expr))):
    attrMap = { fieldIndex : cat.symbol().color().name()}
    attrFeatMap[ f.id() ] = attrMap

layer.dataProvider().changeAttributeValues( attrFeatMap )