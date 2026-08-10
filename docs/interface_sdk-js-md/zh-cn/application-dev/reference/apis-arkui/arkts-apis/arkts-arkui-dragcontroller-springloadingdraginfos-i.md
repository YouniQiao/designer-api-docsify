# SpringLoadingDragInfos

Defines drag-related information when triggering spring loading callbacks.This interface provides drag data summaries and additional drag information, useful for applications needing to dynamically determine whether to respond to spring loading callbacks based on drag data.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-dragController-export interface SpringLoadingDragInfos--><!--Device-dragController-export interface SpringLoadingDragInfos-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## dataSummary

```TypeScript
dataSummary?: unifiedDataChannel.Summary
```

Summary of the dragged data. This field is absent if the source application did not configure data.

**类型：** unifiedDataChannel.Summary

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingDragInfos-dataSummary?: unifiedDataChannel.Summary--><!--Device-SpringLoadingDragInfos-dataSummary?: unifiedDataChannel.Summary-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## extraInfos

```TypeScript
extraInfos?: string
```

Additional information provided by the source application when initiating the drag operation.This field is absent if the source application did not configure it.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingDragInfos-extraInfos?: string--><!--Device-SpringLoadingDragInfos-extraInfos?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

