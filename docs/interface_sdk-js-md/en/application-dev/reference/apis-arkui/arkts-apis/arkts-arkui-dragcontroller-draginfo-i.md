# DragInfo

DragInfo object description@interface DragInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-dragController-interface DragInfo--><!--Device-dragController-interface DragInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { dragController } from '@kit.ArkUI';
```

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: int | int[]
```

Components to be automatically hidden during drag by uniqueId. You can pass a single uniqueId or an array. If the drag source itself also needs to be hidden, pass its uniqueId as well.

**Type:** int \| int[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-autoHideComponentUniqueIds?: int | int[]--><!--Device-DragInfo-autoHideComponentUniqueIds?: int | int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## data

```TypeScript
data?: unifiedDataChannel.UnifiedData
```

Drag data.

**Type:** unifiedDataChannel.UnifiedData

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-data?: unifiedDataChannel.UnifiedData--><!--Device-DragInfo-data?: unifiedDataChannel.UnifiedData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dataLoadParams

```TypeScript
dataLoadParams?: unifiedDataChannel.DataLoadParams
```

Provide a data representation to the system instead of providing a complete data object directly. When the user releases the drag over the target application, the system will use this data representation to request the actual data from drag source. This approach significantly improves the efficiency of initiating drag operations for large volumes of data and enhances the effectiveness of data reception. It is recommended to use this instead of the data field.

**Type:** unifiedDataChannel.DataLoadParams

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-dataLoadParams?: unifiedDataChannel.DataLoadParams--><!--Device-DragInfo-dataLoadParams?: unifiedDataChannel.DataLoadParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraParams

```TypeScript
extraParams?: string
```

Additional information about the drag info.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-extraParams?: string--><!--Device-DragInfo-extraParams?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pointerId

```TypeScript
pointerId: int
```

A unique identifier to identify which touch point.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-pointerId: int--><!--Device-DragInfo-pointerId: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewOptions

```TypeScript
previewOptions?: DragPreviewOptions
```

Drag preview options.

**Type:** DragPreviewOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-previewOptions?: DragPreviewOptions--><!--Device-DragInfo-previewOptions?: DragPreviewOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## touchPoint

```TypeScript
touchPoint?: TouchPoint
```

Touch point coordinates.

**Type:** TouchPoint

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragInfo-touchPoint?: TouchPoint--><!--Device-DragInfo-touchPoint?: TouchPoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

