import ACESConvertor

toolbar = nuke.menu('Nodes')
aaMenu = toolbar.addMenu('ACES', 'A_logo.png')

aaMenu.addCommand('ACEScg', 'ACESConvertor.to_ACEScg()', 'a')
