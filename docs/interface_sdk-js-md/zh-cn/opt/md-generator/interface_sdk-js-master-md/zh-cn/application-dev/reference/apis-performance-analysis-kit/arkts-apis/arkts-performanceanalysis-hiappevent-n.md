# hiAppEvent

本模块提供应用打点和事件订阅能力，包括事件存储、事件订阅、事件清理、打点配置等功能。HiAppEvent将应用运行过程中触发的事件信息统一归纳到[AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md#appeventinfo) 中，并将事件分为系统事件和应用事件两类。 系统事件来源于系统服务，是系统预先定义的事件，这类事件信息中的事件参数对象params包含的字段已由各系统事件定义，具体字段含义在各系统事件指南的介绍中，例如 [崩溃事件介绍](../../../dfx/hiappevent-watcher-crash-events.md)。 应用事件来源于应用，是应用开发者自己定义的事件，这类事件信息支持自定义后通过[Write](arkts-performanceanalysis-hiappevent-write-f.md#write)打点接口进行配置设定，具体字段含义可结合开发者需求展开。

**起始版本：** 23

<!--Device-unnamed-declare namespace hiAppEvent--><!--Device-unnamed-declare namespace hiAppEvent-End-->

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

## 导入模块

```TypeScript
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [domain](arkts-performanceanalysis-hiappevent-domain-n.md) | 提供域名常量。 \|名称\|类型\|只读\|描述\| \| --- \| ------ \| ------ \| ---------- \| \| OS \| string \|是\|系统域\|
| [event](arkts-performanceanalysis-hiappevent-event-n.md) |
| [param](arkts-performanceanalysis-hiappevent-param-n.md) | 提供参数名常量。 \|名称\|类型\|只读\|描述\| \| ------------------------------- \| ------ \| ------ \| ------------------ \| \| USER_ID \| string \|是\|自定义用户ID\| \| DISTRIBUTED_SERVICE_NAME \| string \|是\|分布式服务名称\| \| DISTRIBUTED_SERVICE_INSTANCE_ID \| string \|是\|分布式服务实例ID\|

### 函数

| 名称 |
| --- |
| [configure](arkts-performanceanalysis-hiappevent-configure-f.md#configure) |
| [write](arkts-performanceanalysis-hiappevent-write-f.md#write) |
| [write](arkts-performanceanalysis-hiappevent-write-f.md#write) |
| [setEventParam](arkts-performanceanalysis-hiappevent-seteventparam-f.md#seteventparam) |
| [setEventConfig](arkts-performanceanalysis-hiappevent-seteventconfig-f.md#seteventconfig) |
| [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addwatcher) |
| [removeWatcher](arkts-performanceanalysis-hiappevent-removewatcher-f.md#removewatcher) |
| [clearData](arkts-performanceanalysis-hiappevent-cleardata-f.md#cleardata) |
| [setUserId](arkts-performanceanalysis-hiappevent-setuserid-f.md#setuserid) |
| [getUserId](arkts-performanceanalysis-hiappevent-getuserid-f.md#getuserid) |
| [setUserProperty](arkts-performanceanalysis-hiappevent-setuserproperty-f.md#setuserproperty) |
| [getUserProperty](arkts-performanceanalysis-hiappevent-getuserproperty-f.md#getuserproperty) |
| [addProcessor](arkts-performanceanalysis-hiappevent-addprocessor-f.md#addprocessor) |
| [addProcessorFromConfig](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md#addprocessorfromconfig) |
| [removeProcessor](arkts-performanceanalysis-hiappevent-removeprocessor-f.md#removeprocessor) |
| [configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md#configeventpolicy) |

### 类

| 名称 |
| --- |
| [AppEventPackageHolder](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) |

### 接口

| 名称 |
| --- |
| [ConfigOption](arkts-performanceanalysis-hiappevent-configoption-i.md) |
| [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) |
| [AppEventPackage](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) |
| [TriggerCondition](arkts-performanceanalysis-hiappevent-triggercondition-i.md) |
| [AppEventFilter](arkts-performanceanalysis-hiappevent-appeventfilter-i.md) |
| [AppEventGroup](arkts-performanceanalysis-hiappevent-appeventgroup-i.md) |
| [Watcher](arkts-performanceanalysis-hiappevent-watcher-i.md) |
| [AppEventReportConfig](arkts-performanceanalysis-hiappevent-appeventreportconfig-i.md) |
| [Processor](arkts-performanceanalysis-hiappevent-processor-i.md) |
| [MainThreadJankPolicy](arkts-performanceanalysis-hiappevent-mainthreadjankpolicy-i.md) |
| [CpuUsageHighPolicy](arkts-performanceanalysis-hiappevent-cpuusagehighpolicy-i.md) |
| [AppCrashPolicy](arkts-performanceanalysis-hiappevent-appcrashpolicy-i.md) |
| [AppFreezePolicy](arkts-performanceanalysis-hiappevent-appfreezepolicy-i.md) |
| [ResourceOverlimitPolicy](arkts-performanceanalysis-hiappevent-resourceoverlimitpolicy-i.md) |
| [AddressSanitizerPolicy](arkts-performanceanalysis-hiappevent-addresssanitizerpolicy-i.md) |
| [EventPolicy](arkts-performanceanalysis-hiappevent-eventpolicy-i.md) |

### 枚举

| 名称 |
| --- |
| [EventType](arkts-performanceanalysis-hiappevent-eventtype-e.md) |

### 类型

| 名称 |
| --- |
| [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md) |
