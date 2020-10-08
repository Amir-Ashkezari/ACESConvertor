import nuke
import os


def to_ACEScg():
    """ Write out selected read nodes to ACEScg colorspace """
    selNodes = nuke.selectedNodes()
    for node in selNodes:
        if node.Class() == 'Read':
            inputDataType = {
                '8-bit fixed': 169, '16-bit fixed': 169,
                '16-bit half float': 163, '32-bit float': 163
            }
            bitDepth = node.metadata('input/bitsperchannel')
            node['colorspace'].setValue(inputDataType[bitDepth])
            fileParm = node['file'].value()
            fileName = str(fileParm.split('/')[-1])
            newName = str(fileName.split('.')[0] + '_ACEScg')
            fileName = fileName.replace(str(fileName.split('.')[0]), newName)
            filename, fileExt = os.path.splitext(fileName)
            newFileName = filename + '.exr'
            newPath = fileParm.replace(
                str(fileParm.split('/')[-1]), newFileName)

            # Create write node and save out as ACEScg
            wNode = nuke.nodes.Write()
            wNode.setInput(0, node)
            wNode['file'].setValue(newPath)
            wNode['file_type'].setValue(3)
            wNode['colorspace'].setValue(16)
            nuke.execute(wNode, start=1, end=1, incr=1)


to_ACEScg()
