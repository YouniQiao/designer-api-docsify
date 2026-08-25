# @ohos.sendableResourceManager(资源管理)

本模块提供[Resource](arkts-localization-sendableresourcemanager-resource-t.md)对象与 [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md)对象之间的相互转换功能。SendableResource实现了 [ISendable](../../../arkts-utils/arkts-sendable.md#isendable)接口，支持跨线程传输。跨线程传输后，SendableResource对象可以再转换为Resource对象，作为 参数传递给[资源管理](arkts-resourcemanager.md)接口以获取资源。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Global.ResourceManager

## 导入模块

```TypeScript
import { sendableResourceManager } from '@kit.LocalizationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [resourceToSendableResource(资源管理)](arkts-localization-sendableresourcemanager-resourcetosendableresource-f.md) |
| [sendableResourceToResource(资源管理)](arkts-localization-sendableresourcemanager-sendableresourcetoresource-f.md) |

### 类型

| 名称 |
| --- |
| [Resource(资源管理)](arkts-localization-sendableresourcemanager-resource-t.md) |
| [SendableResource(资源管理)](arkts-localization-sendableresourcemanager-sendableresource-t.md) |
