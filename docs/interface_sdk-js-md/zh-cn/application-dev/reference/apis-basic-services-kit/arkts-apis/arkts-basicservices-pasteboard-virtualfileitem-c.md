# VirtualFileItem

```TypeScript
class VirtualFileItem extends VirtualBaseItem
```

虚拟文件的元数据。

**继承/实现关系：** VirtualFileItem extends [VirtualBaseItem](arkts-basicservices-pasteboard-virtualbaseitem-c.md)

**起始版本：** 26.1.0

<!--Device-pasteboard-class VirtualFileItem extends VirtualBaseItem--><!--Device-pasteboard-class VirtualFileItem extends VirtualBaseItem-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## id

```TypeScript
id: string
```

文件唯一标识，用于在[onStat](arkts-basicservices-pasteboard-virtualfileinfo-c.md#onstat)、[onRead](arkts-basicservices-pasteboard-virtualfileinfo-c.md#onread)和[onCancel](arkts-basicservices-pasteboard-virtualfileinfo-c.md#oncancel)中标识需要处理的虚拟文件。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileItem-id: string--><!--Device-VirtualFileItem-id: string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## size

```TypeScript
size?: number
```

文件大小（单位：字节数），可选参数。未填写时，需要通过[onStat](arkts-basicservices-pasteboard-virtualfileinfo-c.md#onstat)在运行时返回文件大小信息。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileItem-size?: long--><!--Device-VirtualFileItem-size?: long-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## type

```TypeScript
readonly type: VirtualItemType = VirtualItemType.FILE
```

文件类型，值为[FILE](arkts-basicservices-pasteboard-virtualitemtype-e.md#file)。

**类型：** [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileItem-readonly type: VirtualItemType = VirtualItemType.FILE--><!--Device-VirtualFileItem-readonly type: VirtualItemType = VirtualItemType.FILE-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard
