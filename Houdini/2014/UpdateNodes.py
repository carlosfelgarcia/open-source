'''
Created on Apr 26, 2014

@author: User
'''
import hou


obj_node = hou.node("/obj").children()
counter = 0
for n in obj_node:
    if len(n.children()) > 1:
        for _n in n.children():
            if len(_n.children()) > 1:
                if isinstance(_n, hou.ShopNode):
                    for final_node in _n.allNodes():
                        try:
                            if not final_node.matchesCurrentDefinition():
                                print 'updating node {0}'.format(final_node.name)
                                final_node.matchCurrentDefinition()
                                counter += 1
                        except:
                            print ':('
if counter == 0:
    print 'All nodes are up to date :)'
                

if __name__ == '__main__':
    pass