# DragEvent

DragEvent object description

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## executeDropAnimation

```TypeScript
executeDropAnimation(customDropAnimation: VoidCallback): void
```

Setup one drop animation execution callback, which will be triggered by system when user drops. Use this way to implement the custom drop animation instead of doing it in onDrop, as the system will decide when to trigger the callback during the drop handling. [Note]:
1. Please set useCustomDropAnimation to true as well when using this method.
2. Do not implement the animation no-related logics in the callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customDropAnimation | [VoidCallback](arkts-arkui-voidcallback-t.md) | 是 |

## getData

```TypeScript
getData(): UnifiedData | undefined
```

Get dragData from DragEvent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UnifiedData](arkts-arkui-unifieddata-t.md) \| undefined |

**错误码：**

| 错误码ID |
| --- |
| [190001](../errorcode-drag-event.md#190001-数据未找到) |
| [190002](../errorcode-drag-event.md#190002-获取数据错误) |

## getDisplayId

```TypeScript
getDisplayId(): int
```

Get the id of display which the drag event is occuring on.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| int |

## getDisplayX

```TypeScript
getDisplayX(): double
```

X coordinate of the touch point relative to the left edge of the device screen.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getDisplayY

```TypeScript
getDisplayY(): double
```

Y coordinate of the touch point relative to the upper edge of the device screen.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getDragSource

```TypeScript
getDragSource(): string
```

Retrieve the bundle information of the drag source application.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getGlobalDisplayX

```TypeScript
getGlobalDisplayX(): double
```

X coordinate of the point relative to the global display.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getGlobalDisplayY

```TypeScript
getGlobalDisplayY(): double
```

Y coordinate of the point relative to the global display.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getModifierKeyState

```TypeScript
getModifierKeyState?: ModifierKeyStateGetter
```

Query the modifier key press state, support 'ctrl'|'alt'|'shift'

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getPreviewRect

```TypeScript
getPreviewRect(): Rectangle
```

Get the rectangle of drag window.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Rectangle](arkts-arkui-common-rectangle-i.md) |

## getResult

```TypeScript
getResult(): DragResult
```

Get dragEvent result from DragEvent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DragResult](arkts-arkui-common-dragresult-e.md) |

## getSummary

```TypeScript
getSummary(): Summary | undefined
```

Get dragData summary from DragEvent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Summary](arkts-arkui-summary-t.md) \| undefined |

## getVelocity

```TypeScript
getVelocity(): double
```

Get the velocity of drag gesture.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getVelocityX

```TypeScript
getVelocityX(): double
```

Get the x axis velocity of drag gesture.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getVelocityY

```TypeScript
getVelocityY(): double
```

Get the y axis velocity of drag gesture.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getWindowX

```TypeScript
getWindowX(): double
```

X coordinate of the touch point relative to the left edge of the current window.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## getWindowY

```TypeScript
getWindowY(): double
```

Y coordinate of the touch point relative to the left edge of the current window.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double |

## isRemote

```TypeScript
isRemote(): boolean
```

Call this method to determine whether the current drag operation is a cross-device drag.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## setData

```TypeScript
setData(unifiedData: UnifiedData): void
```

Set dragData into DragEvent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| unifiedData | [UnifiedData](arkts-arkui-unifieddata-t.md) | 是 |

## setDataLoadParams

```TypeScript
setDataLoadParams(dataLoadParams: DataLoadParams): void
```

Use this method to provide a data representation to the system instead of directly providing a complete data object. When the user releases the drag over the target application, the system will use this data representation to request the actual data from drag source. This approach significantly improves the efficiency of initiating drag operations for large volumes of data and enhances the effectiveness of data reception. It is recommended to use this method instead of the setData method.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dataLoadParams](arkts-arkui-dragcontroller-draginfo-i.md) | [DataLoadParams](arkts-arkui-dataloadparams-t.md) | 是 |

## setResult

```TypeScript
setResult(dragResult: DragResult): void
```

Set dragEvent result to DragEvent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dragResult | [DragResult](arkts-arkui-common-dragresult-e.md) | 是 |

## startDataLoading

```TypeScript
startDataLoading(options: DataSyncOptions): string | undefined
```

Request the drag data to be synchronized to caller, can be notified with the synchronization progress. Only can be used in onDrop event processing.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DataSyncOptions](arkts-arkui-datasyncoptions-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string \| undefined |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [190003](../errorcode-drag-event.md#190003-当前阶段不允许操作) |

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: int | int[]
```

Set the uniqueId or uniqueId array of components that need to be automatically hidden during dragging. This property takes effect only in onDragStart. After the drag starts successfully, the system hides the target components before the drag preview window is shown. Developers need to restore component visibility in onDragEnd or onDrop based on service requirements.

**类型：** int \| int[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dragBehavior

```TypeScript
dragBehavior: DragBehavior
```

If copy is COPY, this DragEvent is a copy event.

**类型：** [DragBehavior](arkts-arkui-common-dragbehavior-e.md)

**默认值：** COPY

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## useCustomDropAnimation

```TypeScript
useCustomDropAnimation: boolean
```

If useCustomDropAnimation is true, System will not use drop animation.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
