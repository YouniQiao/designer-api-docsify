# ToolBarParams

```TypeScript
export interface ToolBarParams
```

构造工具栏的参数，包括项列表、修改器、浮动配置和回调。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarParams--><!--Device-unnamed-export interface ToolBarParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## advancedToolBarModifier

```TypeScript
advancedToolBarModifier?: AdvancedToolBarV2Modifier
```

高级工具栏的修改器。

**类型：** [AdvancedToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2modifier-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarParams-advancedToolBarModifier?: AdvancedToolBarV2Modifier--><!--Device-ToolBarParams-advancedToolBarModifier?: AdvancedToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## callbacks

```TypeScript
callbacks?: ToolBarCallbacks
```

工具栏回调合集。

**类型：** [ToolBarCallbacks](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcallbacks-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarParams-callbacks?: ToolBarCallbacks--><!--Device-ToolBarParams-callbacks?: ToolBarCallbacks-End-->

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

<!--Device-ToolBarParams-controller?: ToolBarController--><!--Device-ToolBarParams-controller?: ToolBarController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## floatingConfigs

```TypeScript
floatingConfigs?: ToolBarFloatingConfigs
```

工具栏浮动行为配置。默认值：按[ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md)各字段默认值。

**类型：** [ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarParams-floatingConfigs?: ToolBarFloatingConfigs--><!--Device-ToolBarParams-floatingConfigs?: ToolBarFloatingConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialParams

```TypeScript
initialParams: ToolBarInitialParams
```

初始位置。

**类型：** [ToolBarInitialParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarinitialparams-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarParams-initialParams: ToolBarInitialParams--><!--Device-ToolBarParams-initialParams: ToolBarInitialParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
toolBarList: AdvancedToolBarV2Item[]
```

要显示的高级工具栏项的列表。

**类型：** [AdvancedToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2item-c.md)[]

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarParams-toolBarList: AdvancedToolBarV2Item[]--><!--Device-ToolBarParams-toolBarList: AdvancedToolBarV2Item[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
