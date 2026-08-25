# DragEvent

拖拽事件信息。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## executeDropAnimation

```TypeScript
executeDropAnimation(customDropAnimation: Callback<void>): void
```

设置自定义落位动效的执行函数，仅在 [useCustomDropAnimation](#usecustomdropanimation)为true时有效。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customDropAnimation | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | 是 |

## getData

```TypeScript
getData(): UnifiedData
```

获取拖拽相关数据。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UnifiedData](arkts-arkui-unifieddata-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [190001](../errorcode-drag-event.md#190001-数据未找到) |
| [190002](../errorcode-drag-event.md#190002-获取数据错误) |

## getDisplayId

```TypeScript
getDisplayId(): number
```

获取当前拖拽事件发生时所在的屏幕ID，不支持在[onDragEnd](arkts-arkui-commonmethod-c.md#ondragend)阶段使用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getDisplayX

```TypeScript
getDisplayX(): number
```

获取当前拖拽点相对于屏幕左上角的x轴坐标。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getDisplayY

```TypeScript
getDisplayY(): number
```

获取当前拖拽点相对于屏幕左上角的y轴坐标。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getDragSource

```TypeScript
getDragSource(): string
```

获取拖起方包名。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getGlobalDisplayX

```TypeScript
getGlobalDisplayX(): number
```

当前拖拽点相对于全局屏幕的左上角的X坐标。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getGlobalDisplayY

```TypeScript
getGlobalDisplayY(): number
```

当前拖拽点相对于全局屏幕的左上角的Y坐标。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getModifierKeyState

```TypeScript
getModifierKeyState?(keys: Array<string>): boolean
```

获取功能键按压状态。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | Array & lt;string & gt; | 是 | 获取功能键按压状态。报错信息请参考以下错误码。支持功能键 'Ctrl' \| 'Alt' \|

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getPreviewRect

```TypeScript
getPreviewRect(): Rectangle
```

获取拖拽预览图相对于当前窗口的位置，以及预览图尺寸信息。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Rectangle](arkts-arkui-rectangle-i.md) |

## getResult

```TypeScript
getResult(): DragResult
```

获取拖拽结果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DragResult](arkts-arkui-dragresult-e.md) |

## getSummary

```TypeScript
getSummary(): Summary
```

获取所拖拽数据的概要，包括数据类型及大小信息；在延迟拖拽场景下，只能获取到数据类型信息。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Summary](arkts-arkui-summary-t.md) |

## getVelocity

```TypeScript
getVelocity(): number
```

获取当前拖拽的主方向拖动速度。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getVelocityX

```TypeScript
getVelocityX(): number
```

获取当前拖拽的x轴方向拖动速度。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getVelocityY

```TypeScript
getVelocityY(): number
```

获取当前拖拽的y轴方向拖动速度。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getWindowX

```TypeScript
getWindowX(): number
```

获取拖拽点相对于窗口左上角的x轴坐标。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getWindowY

```TypeScript
getWindowY(): number
```

获取拖拽点相对于窗口左上角的y轴坐标。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getX

```TypeScript
getX(): number
```

当前拖拽点相对于窗口左上角的x轴坐标，单位为vp。

> **说明：**

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [getWindowX](#getwindowx)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getY

```TypeScript
getY(): number
```

当前拖拽点相对于窗口左上角的y轴坐标，单位为vp。

> **说明：**

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [getWindowY](#getwindowy)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## isRemote

```TypeScript
isRemote(): boolean
```

获取是否是跨设备拖拽，跨设备拖拽时为true。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## setData

```TypeScript
setData(unifiedData: UnifiedData): void
```

向DragEvent中设置用于拖拽的数据。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| unifiedData | [UnifiedData](arkts-arkui-unifieddata-t.md) | 是 |

## setDataLoadParams

```TypeScript
setDataLoadParams(dataLoadParams: DataLoadParams): void
```

设置起拖方延迟提供数据。使用此方法向系统提供数据加载参数，而不是直接提供完整的数据对象。当用户在目标应用程序上落入时，系统将使用此参数从起拖方请求实际数据。与[setData](#setdata)方法 同时使用，以最后调用的方法为准。该接口仅在[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart)回调中生效。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dataLoadParams](../arkts-apis/arkts-arkui-dragcontroller-draginfo-i.md) | [DataLoadParams](arkts-arkui-dataloadparams-t.md) | 是 |

## setResult

```TypeScript
setResult(dragResult: DragResult): void
```

在DragEvent中设置拖拽结果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dragResult | [DragResult](arkts-arkui-dragresult-e.md) | 是 |

## startDataLoading

```TypeScript
startDataLoading(options: DataSyncOptions): string
```

异步获取拖拽数据，并通知开发者当前数据同步进度，仅支持在onDrop阶段使用。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DataSyncOptions](arkts-arkui-datasyncoptions-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [190003](../errorcode-drag-event.md#190003-当前阶段不允许操作) |

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: number | number[]
```

设置拖拽过程中需要自动隐藏的组件uniqueId，支持传入单个uniqueId或数组。仅在[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart)回调中设置生效。拖拽成功发起后，系统会在显示拖拽预览窗口前隐藏目标组件。若拖拽源本身也需要隐藏，需要同时传入拖拽源组件的uniqueId。组件的uniqueId可通过[UIContext.getFrameNodeById()](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#getframenodebyid) 配合[FrameNode.getUniqueId()](../arkts-apis/arkts-arkui-framenode-c.md#getuniqueid)获取。开发者应在[onDragEnd](arkts-arkui-commonmethod-c.md#ondragend)或 onDrop中恢复组件显示状态。

**类型：** number \| number[]

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dragBehavior

```TypeScript
dragBehavior: DragBehavior
```

切换复制和剪贴模式的角标显示状态。默认值：DragBehavior.COPY。

**类型：** [DragBehavior](arkts-arkui-dragbehavior-e.md)

**默认值：** COPY

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## useCustomDropAnimation

```TypeScript
useCustomDropAnimation: boolean
```

当拖拽结束时，是否禁用系统默认落位动效。应用可将该值设定为true来禁用系统默认落位动效，并实现自己的自定义落位动效。当不配置或设置为false时，系统默认落位动效生效，当[setResult](#setresult)设置为DRAG_SUCCESSFUL时，落位为缩小消失动效，不为DRAG_SUCCESSFUL时，则 为放大消失动效。当未禁用系统默认落位动效时，应用不应再实现自定义动效，以避免动效上的冲突。默认值：false

**类型：** boolean

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
