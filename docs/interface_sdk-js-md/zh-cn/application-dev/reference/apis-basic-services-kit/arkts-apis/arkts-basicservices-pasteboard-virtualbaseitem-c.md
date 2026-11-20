# VirtualBaseItem

```TypeScript
class VirtualBaseItem
```

虚拟文件和文件夹的基础类型。

**起始版本：** 26.1.0

<!--Device-pasteboard-class VirtualBaseItem--><!--Device-pasteboard-class VirtualBaseItem-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## modifyTime

```TypeScript
modifyTime: Date
```

最后修改时间。

**类型：** Date

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualBaseItem-modifyTime: Date--><!--Device-VirtualBaseItem-modifyTime: Date-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## name

```TypeScript
name: string
```

文件名或文件夹名。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualBaseItem-name: string--><!--Device-VirtualBaseItem-name: string-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## type

```TypeScript
readonly type: VirtualItemType
```

文件类型。[VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md)的type值为[FILE](arkts-basicservices-pasteboard-virtualitemtype-e.md#file)；[VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md)的type值为[DIR](arkts-basicservices-pasteboard-virtualitemtype-e.md#dir)。

**类型：** [VirtualItemType](arkts-basicservices-pasteboard-virtualitemtype-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualBaseItem-readonly type: VirtualItemType--><!--Device-VirtualBaseItem-readonly type: VirtualItemType-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard
