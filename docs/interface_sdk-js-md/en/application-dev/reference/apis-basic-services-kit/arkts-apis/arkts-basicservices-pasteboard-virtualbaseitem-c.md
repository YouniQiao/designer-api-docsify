# VirtualBaseItem

```TypeScript
class VirtualBaseItem
```

Base type for virtual file and directory items.

**Since:** 26.1.0

<!--Device-pasteboard-class VirtualBaseItem--><!--Device-pasteboard-class VirtualBaseItem-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## modifyTime

```TypeScript
modifyTime: Date
```

Last modification time.

**Type:** Date

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualBaseItem-modifyTime: Date--><!--Device-VirtualBaseItem-modifyTime: Date-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## name

```TypeScript
name: string
```

File or directory name.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualBaseItem-name: string--><!--Device-VirtualBaseItem-name: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## type

```TypeScript
readonly type: VirtualItemType
```

File type. The value of [type](arkts-basicservices-pasteboard-virtualfileitem-c.md#type) for [VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md) is [FILE](arkts-basicservices-pasteboard-virtualitemtype-e.md#file); the value of [type](arkts-basicservices-pasteboard-virtualdiritem-c.md#type) for [VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md) is [DIR](arkts-basicservices-pasteboard-virtualitemtype-e.md#dir).

**Type:** [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualBaseItem-readonly type: VirtualItemType--><!--Device-VirtualBaseItem-readonly type: VirtualItemType-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
