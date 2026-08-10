# PanelStartCallback（系统接口）

The callback of start vertical panel.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-verticalPanelManager-interface PanelStartCallback--><!--Device-verticalPanelManager-interface PanelStartCallback-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { verticalPanelManager } from 'kits/@kit.AbilityKit';
```

## onError

```TypeScript
onError: OnErrorFn
```

Called when some error occurred except disconnected from UIAbility or UIExtensionAbility.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanelStartCallback-onError: OnErrorFn--><!--Device-PanelStartCallback-onError: OnErrorFn-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

## onResult

```TypeScript
onResult?: OnResultFn
```

Called when UIExtensionAbility terminate with result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PanelStartCallback-onResult?: OnResultFn--><!--Device-PanelStartCallback-onResult?: OnResultFn-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

