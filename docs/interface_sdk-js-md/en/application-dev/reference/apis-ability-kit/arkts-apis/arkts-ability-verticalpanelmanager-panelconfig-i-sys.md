# PanelConfig (System API)

Indicates the panel config

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-verticalPanelManager-interface PanelConfig--><!--Device-verticalPanelManager-interface PanelConfig-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

## sourceAppInfo

```TypeScript
sourceAppInfo: Record<string, string>
```

Indicates the info about source app

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE**  
\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_1. The values of the following keys are assigned by the system. Manual settings do not take effect,since the system automatically changes the values to the actual values during data transfer.  
-SOURCE\_APP\_BUNDLE\_NAME: bundle name of the caller. The value is a string.  
-SOURCE\_APP\_MODULE\_NAME: module name of the caller. The value is a string.  
-SOURCE\_APP\_ABILITY\_NAME: ability name of the caller. The value is a string.  
-SOURCE\_APP\_WINDOW\_ID: the window ID of the caller. The value is a string.  
-SOURCE\_APP\_SCREEN\_MODE: the screen mode of the split screen. The value is a string. The value is "1".

**Type:** Record&lt;string, string&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelConfig-sourceAppInfo: Record<string, string>--><!--Device-PanelConfig-sourceAppInfo: Record<string, string>-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

## type

```TypeScript
type: VerticalType
```

The type of vertical domain

**Type:** VerticalType

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelConfig-type: VerticalType--><!--Device-PanelConfig-type: VerticalType-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

