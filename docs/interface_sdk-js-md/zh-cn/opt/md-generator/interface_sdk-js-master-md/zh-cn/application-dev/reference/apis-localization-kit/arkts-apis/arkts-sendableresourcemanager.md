# @ohos.sendableResourceManager

本模块提供[Resource](arkts-localization-sendableresourcemanager-resource-t.md#Resource)对象与  
[SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md#SendableResource)对象之间的相互转换功能。SendableResource实现了  
[ISendable](../../../arkts-utils/arkts-sendable.md#isendable)接口，支持跨线程传输。跨线程传输后，SendableResource对象可以再转换为Resource对象，作为参数传递给[资源管理](arkts-resourcemanager.md#resourceManager)接口以获取资源。

**起始版本：** 12

<!--Device-unnamed-declare namespace sendableResourceManager--><!--Device-unnamed-declare namespace sendableResourceManager-End-->

**系统能力：** SystemCapability.Global.ResourceManager

## 汇总

### 函数

| 名称 |
| --- |
| [resourceToSendableResource](arkts-localization-sendableresourcemanager-resourcetosendableresource-f.md#resourcetosendableresource) |
| [sendableResourceToResource](arkts-localization-sendableresourcemanager-sendableresourcetoresource-f.md#sendableresourcetoresource) |

### 类型

| 名称 |
| --- |
| [Resource](arkts-localization-sendableresourcemanager-resource-t.md) |
| [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) |
