from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from dragonfly import Text
from dragonfly.actions.action_key import Key

class CustomNavigationBar(MergeRule):
    pronunciation = "custom navigation bar"
    mapping = {
        "fire chat":                                R(Key("w-1"), rdescript="Custom Navigation: Alpine Chat"), 
        "kanban":                                   R(Key("w-2"), rdescript="Custom Navigation: Kanban"), 
        "get help | git hub":                       R(Key("w-3"), rdescript="Custom Navigation: GitHub"), 
        "chromium":                                 R(Key("w-4"), rdescript="Custom Navigation: Chrome"), 
        "slime tech":                               R(Key("w-5"), rdescript="Custom Navigation: Sublime Text"), 
        "file system":                              R(Key("w-6"), rdescript="Custom Navigation: Open File Browser"), 
        "sequel server":                            R(Key("w-7"), rdescript="Custom Navigation: MSSQL Management Studio"), 
        "(get bash) | git bash":                    R(Key("w-8"), rdescript="Custom Navigation: ConEmu"), 
        }
    extras = []
    defaults = {}

control.nexus().merger.add_global_rule(CustomNavigationBar())
