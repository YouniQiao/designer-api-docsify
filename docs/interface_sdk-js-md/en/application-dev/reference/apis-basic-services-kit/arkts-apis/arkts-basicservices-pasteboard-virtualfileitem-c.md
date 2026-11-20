# VirtualFileItem

```TypeScript
class VirtualFileItem extends VirtualBaseItem
```

Metadata of a virtual file.

**Inheritance/Implementation:** VirtualFileItem extends [VirtualBaseItem](arkts-basicservices-pasteboard-virtualbaseitem-c.md)

**Since:** 26.1.0

<!--Device-pasteboard-class VirtualFileItem extends VirtualBaseItem--><!--Device-pasteboard-class VirtualFileItem extends VirtualBaseItem-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## id

```TypeScript
id: string
```

Unique file identifier, used in [onStat](arkts-basicservices-pasteboard-virtualfileinfo-c.md#onstat), [onRead](arkts-basicservices-pasteboard-virtualfileinfo-c.md#onread), and [onCancel](arkts-basicservices-pasteboard-virtualfileinfo-c.md#oncancel) to identify the virtual file to be processed.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileItem-id: string--><!--Device-VirtualFileItem-id: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## size

```TypeScript
size?: number
```

File size (unit: bytes). This parameter is optional. If left unspecified, the file size information must be returned at runtime through [onStat](arkts-basicservices-pasteboard-virtualfileinfo-c.md#onstat).

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileItem-size?: long--><!--Device-VirtualFileItem-size?: long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## type

```TypeScript
readonly type: VirtualItemType = VirtualItemType.FILE
```

File type, with the value [FILE](arkts-basicservices-pasteboard-virtualitemtype-e.md#file).

**Type:** [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualFileItem-readonly type: VirtualItemType = VirtualItemType.FILE--><!--Device-VirtualFileItem-readonly type: VirtualItemType = VirtualItemType.FILE-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
