# @ohos.arkui.dragController

本模块提供发起主动拖拽的能力，当应用接收到触摸或长按等事件时可以主动发起拖拽的动作，并在其中携带拖拽信息。 > **说明：** > > - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见 > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext)说明。 > > - 示例效果请以真机运行为准，当前 DevEco Studio预览器不支持。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace dragController--><!--Device-unnamed-declare namespace dragController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 函数

| 名称 |
| --- |
| [createDragAction](arkts-arkui-dragcontroller-createdragaction-f.md#createDragAction) |
| [executeDrag](arkts-arkui-dragcontroller-executedrag-f.md#executeDrag) |
| [executeDrag](arkts-arkui-dragcontroller-executedrag-f.md#executeDrag) |
| [getDragPreview](arkts-arkui-dragcontroller-getdragpreview-f.md#getDragPreview) |

### 类

| 名称 |
| --- |
| [DragPreview](arkts-arkui-dragcontroller-dragpreview-c.md) |
| [SpringLoadingContext](arkts-arkui-dragcontroller-springloadingcontext-c.md) |

### 接口

| 名称 |
| --- |
| [AnimationOptions](arkts-arkui-dragcontroller-animationoptions-i.md) |
| [DragAction](arkts-arkui-dragcontroller-dragaction-i.md) |
| [DragAndDropInfo](arkts-arkui-dragcontroller-draganddropinfo-i.md) |
| [DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md) |
| [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) |
| [DragSpringLoadingConfiguration](arkts-arkui-dragcontroller-dragspringloadingconfiguration-i.md) |
| [SpringLoadingDragInfos](arkts-arkui-dragcontroller-springloadingdraginfos-i.md) |

### 枚举

| 名称 |
| --- |
| [DragSpringLoadingState](arkts-arkui-dragcontroller-dragspringloadingstate-e.md) |
| [DragStartRequestStatus](arkts-arkui-dragcontroller-dragstartrequeststatus-e.md) |
| [DragStatus](arkts-arkui-dragcontroller-dragstatus-e.md) |
