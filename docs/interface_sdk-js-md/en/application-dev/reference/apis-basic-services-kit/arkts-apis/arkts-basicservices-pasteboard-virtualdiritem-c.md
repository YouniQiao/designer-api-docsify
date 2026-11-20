# VirtualDirItem

```TypeScript
class VirtualDirItem extends VirtualBaseItem
```

Metadata of a virtual directory.

**Inheritance/Implementation:** VirtualDirItem extends [VirtualBaseItem](arkts-basicservices-pasteboard-virtualbaseitem-c.md)

**Since:** 26.1.0

<!--Device-pasteboard-class VirtualDirItem extends VirtualBaseItem--><!--Device-pasteboard-class VirtualDirItem extends VirtualBaseItem-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## subItems

```TypeScript
subItems?: Array<VirtualFileItem | VirtualDirItem>
```

Child items of the directory. This parameter is optional.

**Type:** Array&lt;[VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md) &#124; [VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md)&gt;

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualDirItem-subItems?: Array<VirtualFileItem | VirtualDirItem>--><!--Device-VirtualDirItem-subItems?: Array<VirtualFileItem | VirtualDirItem>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## type

```TypeScript
readonly type: VirtualItemType = VirtualItemType.DIR
```

File type, with the value [DIR](arkts-basicservices-pasteboard-virtualitemtype-e.md#dir).

**Type:** [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-VirtualDirItem-readonly type: VirtualItemType = VirtualItemType.DIR--><!--Device-VirtualDirItem-readonly type: VirtualItemType = VirtualItemType.DIR-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
