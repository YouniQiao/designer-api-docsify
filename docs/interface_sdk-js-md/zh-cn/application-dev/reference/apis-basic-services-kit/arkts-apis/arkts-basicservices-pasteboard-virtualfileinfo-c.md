# VirtualFileInfo

```TypeScript
class VirtualFileInfo
```

虚拟文件信息。

**起始版本：** 26.1.0

<!--Device-pasteboard-class VirtualFileInfo--><!--Device-pasteboard-class VirtualFileInfo-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## onCancel

```TypeScript
onCancel: VirtualFileOnCancel
```

取消指定虚拟文件操作的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileInfo-onCancel: VirtualFileOnCancel--><!--Device-VirtualFileInfo-onCancel: VirtualFileOnCancel-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## onRead

```TypeScript
onRead: VirtualFileOnRead
```

查询指定虚拟文件的文件内容的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileInfo-onRead: VirtualFileOnRead--><!--Device-VirtualFileInfo-onRead: VirtualFileOnRead-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## onStat

```TypeScript
onStat?: VirtualFileOnStat
```

查询指定虚拟文件的元数据的回调，可选参数。未填写时，若[itemInfo](#iteminfo)中存在[VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md)，需要通过[size](arkts-basicservices-pasteboard-virtualfileitem-c.md#size)在复制时指定文件大小信息。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileInfo-onStat?: VirtualFileOnStat--><!--Device-VirtualFileInfo-onStat?: VirtualFileOnStat-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## itemInfo

```TypeScript
itemInfo: VirtualFileItem | VirtualDirItem
```

文件或文件夹的元数据。

**类型：** [VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md) &#124; [VirtualDirItem](arkts-basicservices-pasteboard-virtualdiritem-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-VirtualFileInfo-itemInfo: VirtualFileItem | VirtualDirItem--><!--Device-VirtualFileInfo-itemInfo: VirtualFileItem | VirtualDirItem-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard
