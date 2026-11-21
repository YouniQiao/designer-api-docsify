# ToolBarConfigs

```TypeScript
export class ToolBarConfigs
```

工具栏的可观察配置存储，与[ToolBarParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarparams-i.md)对应。

**起始版本：** 26.1.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export class ToolBarConfigs--><!--Device-unnamed-export class ToolBarConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(params: ToolBarParams)
```

工具栏配置ToolBarConfigs的构造函数。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-constructor(params: ToolBarParams)--><!--Device-ToolBarConfigs-constructor(params: ToolBarParams)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ToolBarParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarparams-i.md) | 是 | 工具栏构造参数。 |

## advancedToolBarModifier

```TypeScript
advancedToolBarModifier: AdvancedToolBarV2Modifier
```

高级工具栏的修改器。

**类型：** [AdvancedToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2modifier-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-advancedToolBarModifier: AdvancedToolBarV2Modifier--><!--Device-ToolBarConfigs-advancedToolBarModifier: AdvancedToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## callbacks

```TypeScript
callbacks?: ToolBarCallbacks
```

工具栏回调合集。

**类型：** [ToolBarCallbacks](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcallbacks-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-callbacks?: ToolBarCallbacks--><!--Device-ToolBarConfigs-callbacks?: ToolBarCallbacks-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: ToolBarController
```

工具栏控制器。

**类型：** [ToolBarController](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontroller-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-controller?: ToolBarController--><!--Device-ToolBarConfigs-controller?: ToolBarController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## floatingConfigs

```TypeScript
floatingConfigs?: ToolBarFloatingConfigs
```

高级工具栏的浮动配置。

**类型：** [ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-floatingConfigs?: ToolBarFloatingConfigs--><!--Device-ToolBarConfigs-floatingConfigs?: ToolBarFloatingConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialParams

```TypeScript
initialParams: ToolBarInitialParams
```

高级工具栏的初始位置。

**类型：** [ToolBarInitialParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarinitialparams-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-initialParams: ToolBarInitialParams--><!--Device-ToolBarConfigs-initialParams: ToolBarInitialParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
toolBarList: AdvancedToolBarV2Item[]
```

要显示的高级工具栏项列表。

**类型：** [AdvancedToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2item-c.md)[]

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarConfigs-toolBarList: AdvancedToolBarV2Item[]--><!--Device-ToolBarConfigs-toolBarList: AdvancedToolBarV2Item[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
