# VirtualFileInfo

```TypeScript
class VirtualFileInfo
```

Virtual file information.

**Since:** 26.1.0

<!--Device-pasteboard-class VirtualFileInfo--><!--Device-pasteboard-class VirtualFileInfo-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## onCancel

```TypeScript
onCancel: VirtualFileOnCancel
```

Callback invoked to cancel the operation of specified virtual files.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileInfo-onCancel: VirtualFileOnCancel--><!--Device-VirtualFileInfo-onCancel: VirtualFileOnCancel-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## onRead

```TypeScript
onRead: VirtualFileOnRead
```

Callback invoked to read the content of a specified virtual file.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileInfo-onRead: VirtualFileOnRead--><!--Device-VirtualFileInfo-onRead: VirtualFileOnRead-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## onStat

```TypeScript
onStat?: VirtualFileOnStat
```

Callback invoked to obtain the metadata of a specified virtual file. This parameter is optional. If left unspecified, when [itemInfo](#iteminfo) contains a [VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md), the file size must be specified through [size](arkts-basicservices-pasteboard-virtualfileitem-c.md#size) at copy time.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileInfo-onStat?: VirtualFileOnStat--><!--Device-VirtualFileInfo-onStat?: VirtualFileOnStat-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## itemInfo

```TypeScript
itemInfo: VirtualFileItem | VirtualDirItem
```

Metadata of a file or directory.

**Type:** [VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md) &#124; [VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileInfo-itemInfo: VirtualFileItem | VirtualDirItem--><!--Device-VirtualFileInfo-itemInfo: VirtualFileItem | VirtualDirItem-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
