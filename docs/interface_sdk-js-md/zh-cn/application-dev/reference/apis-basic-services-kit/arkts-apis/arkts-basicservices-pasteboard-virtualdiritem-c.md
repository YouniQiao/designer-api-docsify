# VirtualDirItem

```TypeScript
class VirtualDirItem extends VirtualBaseItem
```

虚拟文件夹的元数据。

**继承/实现关系：** VirtualDirItem extends [VirtualBaseItem](arkts-basicservices-pasteboard-virtualbaseitem-c.md)

**起始版本：** 26.1.0

<!--Device-pasteboard-class VirtualDirItem extends VirtualBaseItem--><!--Device-pasteboard-class VirtualDirItem extends VirtualBaseItem-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## subItems

```TypeScript
subItems?: Array<VirtualFileItem | VirtualDirItem>
```

文件夹的子节点，可选参数。

**类型：** Array&lt;[VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md) &#124; [VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md)&gt;

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualDirItem-subItems?: Array<VirtualFileItem | VirtualDirItem>--><!--Device-VirtualDirItem-subItems?: Array<VirtualFileItem | VirtualDirItem>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## type

```TypeScript
readonly type: VirtualItemType = VirtualItemType.DIR
```

文件类型，值为[DIR](arkts-basicservices-pasteboard-virtualitemtype-e.md#dir)。

**类型：** [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualDirItem-readonly type: VirtualItemType = VirtualItemType.DIR--><!--Device-VirtualDirItem-readonly type: VirtualItemType = VirtualItemType.DIR-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard
