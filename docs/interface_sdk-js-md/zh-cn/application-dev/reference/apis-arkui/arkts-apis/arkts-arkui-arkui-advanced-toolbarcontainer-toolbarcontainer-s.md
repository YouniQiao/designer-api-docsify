# ToolBarContainer

```TypeScript
export struct ToolBarContainer
```

ToolBarContainer组件，用于承载一个或多个浮动工具栏，支持停靠、安全区避让和握姿适配。

**起始版本：** 26.1.0

**装饰器类型：** @ComponentV2

<!--Device-unnamed-export struct ToolBarContainer--><!--Device-unnamed-export struct ToolBarContainer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## containerConfigs

```TypeScript
containerConfigs?: ToolBarContainerConfigs
```

容器级配置，包括停靠偏移量、安全区避让和握姿适配。

**类型：** [ToolBarContainerConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontainerconfigs-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainer-containerConfigs?: ToolBarContainerConfigs--><!--Device-ToolBarContainer-containerConfigs?: ToolBarContainerConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: Callback<void>
```

组件中显示的内容。

**类型：** Callback&lt;void&gt;

**起始版本：** 26.1.0

**装饰器类型：** @BuilderParam

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainer-content: Callback<void>--><!--Device-ToolBarContainer-content: Callback<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolbars

```TypeScript
toolbars: ToolBarConfigs[]
```

工具栏配置列表。最多支持4个工具栏，超出部分不生效。

**类型：** [ToolBarConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarconfigs-c.md)[]

**起始版本：** 26.1.0

**装饰器类型：** @Require

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainer-toolbars: ToolBarConfigs[]--><!--Device-ToolBarContainer-toolbars: ToolBarConfigs[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
