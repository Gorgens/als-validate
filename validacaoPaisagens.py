import subprocess
import os

FUSION_FOLDER = 'C:/FUSION'
LASTOOLS_FOLDER = 'C:/LAStools/bin'

NP_FOLDER = "C:/Paisagens/recebimentoPaisagem/NP"
NP_DTM_FOLDER = "C:/Paisagens/recebimentoPaisagem/NP"
DTM_FOLDER = "C:/Paisagens/recebimentoPaisagem/NP"
DTM_PREVIOUS = "C:/Paisagens/recebimentoPaisagem/MDT_ANTERIOR"

VALIDA_FOLDER = 'C:/Paisagens/recebimentoPaisagem'
PROJETO = 'TAN_A01'

### Cria pasta para projeto 
#try:
#    os.mkdir(VALIDA_FOLDER + '/' + PROJETO)
#except OSError:
#    print ("Creation of the directory failed.")
#else:
#    print ("Successfully created the directory.")
#
### Gera o modelo digital de terreno
#try:
#    subprocess.call(FUSION_FOLDER + '/GridSurfaceCreate ' +
#                    VALIDA_FOLDER + '/' + PROJETO + '/' + 'mdtCriado.dtm ' +
#                    '1 m m 0 0 0 0 ' + NP_DTM_FOLDER + '/' + PROJETO + '*.las')
#except OSError:
#    print('DTM for %s was not created.' % PROJETO)
#else:
#    print('DTM for %s created successfully!' % PROJETO)
#
### Converte modelo digital de terreno para asc
#try:
#    subprocess.call(FUSION_FOLDER + '/DTM2ASCII ' +
#                    VALIDA_FOLDER + '/' + PROJETO + '/' + 'mdtCriado.dtm ' +
#                    VALIDA_FOLDER + '/' + PROJETO + '/' + 'mdtCriado.asc')
#except OSError:
#    print('DTM from %s was not converted to ASC.' % PROJETO)
#else:
#    print('DTM from %s was successfully converted to ASC!' % PROJETO)
#
### Unir tiles groud antigo
#try:
#    mdts = []
#    for filename in os.listdir(DTM_PREVIOUS):
#        mdts.append(os.path.join(DTM_PREVIOUS+'/'+filename))
#    mdtAnteriorPath = VALIDA_FOLDER + '/' + PROJETO + '/' + 'mdtAnterior.tif'
#    processing.run("gdal:merge", {'INPUT':mdts,
#                                  'PCT':False,
#                                  'SEPARATE':False,
#                                  'NODATA_INPUT':None,
#                                  'NODATA_OUTPUT':-9999, #Prevous None
#                                  'OPTIONS':'',
#                                  'EXTRA':'',
#                                  'DATA_TYPE':5,
#                                  'OUTPUT':VALIDA_FOLDER + '/' + PROJETO + '/' + 'mdtAnterior.tif'})
#except OSError:
#    print('Previous DTM from %s was not merged.' % PROJETO)
#else:
#    print('Previous DTM from %s was successfully merged!' % PROJETO)
#
#mdtAnterior = QgsRasterLayer(mdtAnteriorPath, "mdtAnterior")
#mdtCriado = QgsRasterLayer(VALIDA_FOLDER + '/' + PROJETO + '/' + 'mdtCriado.asc', "mdtCriado")
#crs = QgsCoordinateReferenceSystem("EPSG:31982")
#mdtAnterior.setCrs(crs)
#mdtCriado.setCrs(crs)
#QgsProject.instance().addMapLayer(mdtAnterior)
#QgsProject.instance().addMapLayer(mdtCriado)

### Calcula diferença entre MDTs
#try:
#    processing.run("saga:rastercalculator", {'GRIDS':mdtCriado, #'C:/Paisagens/recebimentoPaisagem/TAN_A01/mdtCriado.asc',
#                                             'XGRIDS': mdtAnterior, #['C:/Paisagens/recebimentoPaisagem/TAN_A01/mdtAnterior.tif'],
#                                             'FORMULA':'a-b',
#                                             'RESAMPLING':3,
#                                             'USE_NODATA':False,
#                                             'TYPE':7,
#                                             'RESULT': VALIDA_FOLDER + '/' + PROJETO + '/' + 'diffCriadoAnterior.tif'}) #'TEMPORARY_OUTPUT'})
#except OSError:
#    print('Diff between DTMs for %s was not computed.' % PROJETO)
#else:
#    print('Diff between DTMs for %s successfully computed' % PROJETO)
    
diffAntCriado = QgsRasterLayer(VALIDA_FOLDER + '/' + PROJETO + '/' + 'diffCriadoAnterior.sdat', 'diffCriadoAnt')
diffAntCriado.setCrs(crs)
QgsProject.instance().addMapLayer(diffAntCriado)