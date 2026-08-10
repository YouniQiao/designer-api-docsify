# DragInfo

DragInfo object description

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-dragController-interface DragInfo--><!--Device-dragController-interface DragInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: int | int[]
```

Components to be automatically hidden during drag by uniqueId.You can pass a single uniqueId or an array. If the drag source itself also needs to be hidden,pass its uniqueId as well.

**类型：** int \| int[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-autoHideComponentUniqueIds?: int | int[]--><!--Device-DragInfo-autoHideComponentUniqueIds?: int | int[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## data

```TypeScript
data?: unifiedDataChannel.UnifiedData
```

Drag data.

**类型：** unifiedDataChannel.UnifiedData

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-data?: unifiedDataChannel.UnifiedData--><!--Device-DragInfo-data?: unifiedDataChannel.UnifiedData-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dataLoadParams

```TypeScript
dataLoadParams?: unifiedDataChannel.DataLoadParams
```

Provide a data representation to the system instead of providing a complete data object directly. When the user releases the drag over the target application, the system will use this data representation to request the actual data from drag source. This approach significantly improves the efficiency of initiating drag operations for large volumes of data and enhances the effectiveness of data reception. It is recommended to use this instead of the data field.

**类型：** unifiedDataChannel.DataLoadParams

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-dataLoadParams?: unifiedDataChannel.DataLoadParams--><!--Device-DragInfo-dataLoadParams?: unifiedDataChannel.DataLoadParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## extraParams

```TypeScript
extraParams?: string
```

Additional information about the drag info.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-extraParams?: string--><!--Device-DragInfo-extraParams?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pointerId

```TypeScript
pointerId: int
```

A unique identifier to identify which touch point.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-pointerId: int--><!--Device-DragInfo-pointerId: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## previewOptions

```TypeScript
previewOptions?: DragPreviewOptions
```

Drag preview options.

**类型：** [DragPreviewOptions](../arkts-components/arkts-arkui-dragpreviewoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-previewOptions?: DragPreviewOptions--><!--Device-DragInfo-previewOptions?: DragPreviewOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## touchPoint

```TypeScript
touchPoint?: TouchPoint
```

Touch point coordinates.

**类型：** [TouchPoint](arkts-arkui-touchpoint-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragInfo-touchPoint?: TouchPoint--><!--Device-DragInfo-touchPoint?: TouchPoint-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

