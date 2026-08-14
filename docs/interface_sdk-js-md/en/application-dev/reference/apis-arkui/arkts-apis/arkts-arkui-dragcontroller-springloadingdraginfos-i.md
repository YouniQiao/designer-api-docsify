# SpringLoadingDragInfos

Defines drag-related information when triggering spring loading callbacks. This interface provides drag data summaries and additional drag information, useful for applications needing to dynamically determine whether to respond to spring loading callbacks based on drag data.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-dragController-export interface SpringLoadingDragInfos--><!--Device-dragController-export interface SpringLoadingDragInfos-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { dragController } from 'dragController';
```

## dataSummary

```TypeScript
dataSummary?: unifiedDataChannel.Summary
```

Summary of the dragged data. This field is absent if the source application did not configure data.

**Type:** unifiedDataChannel.Summary

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingDragInfos-dataSummary?: unifiedDataChannel.Summary--><!--Device-SpringLoadingDragInfos-dataSummary?: unifiedDataChannel.Summary-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraInfos

```TypeScript
extraInfos?: string
```

Additional information provided by the source application when initiating the drag operation. This field is absent if the source application did not configure it.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingDragInfos-extraInfos?: string--><!--Device-SpringLoadingDragInfos-extraInfos?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

