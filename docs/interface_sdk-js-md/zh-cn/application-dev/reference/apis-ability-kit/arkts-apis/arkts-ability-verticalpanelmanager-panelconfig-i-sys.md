# PanelConfig（系统接口）

Indicates the panel config

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-verticalPanelManager-interface PanelConfig--><!--Device-verticalPanelManager-interface PanelConfig-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { verticalPanelManager } from 'kits/@kit.AbilityKit';
```

## sourceAppInfo

```TypeScript
sourceAppInfo: Record<string, string>
```

Indicates the info about source app

&lt;p&gt;**NOTE：**&lt;br&gt;1. The values of the following keys are assigned by the system. Manual settings do not take effect,since the system automatically changes the values to the actual values during data transfer.
-SOURCE_APP_BUNDLE_NAME: bundle name of the caller. The value is a string.
-SOURCE_APP_MODULE_NAME: module name of the caller. The value is a string.
-SOURCE_APP_ABILITY_NAME: ability name of the caller. The value is a string.
-SOURCE_APP_WINDOW_ID: the window ID of the caller. The value is a string.
-SOURCE_APP_SCREEN_MODE: the screen mode of the split screen. The value is a string. The value is "1".

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanelConfig-sourceAppInfo: Record<string, string>--><!--Device-PanelConfig-sourceAppInfo: Record<string, string>-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: VerticalType
```

The type of vertical domain

**类型：** [VerticalType](arkts-ability-verticalpanelmanager-verticaltype-e-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanelConfig-type: VerticalType--><!--Device-PanelConfig-type: VerticalType-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

