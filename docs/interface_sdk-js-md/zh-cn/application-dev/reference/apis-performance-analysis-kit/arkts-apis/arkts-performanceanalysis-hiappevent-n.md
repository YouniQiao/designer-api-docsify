# hiAppEvent(应用事件打点)

本模块提供应用打点和事件订阅能力，包括事件存储、事件订阅、事件清理、打点配置等功能。HiAppEvent将应用运行过程中触发的事件信息统一归纳到[AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) 中，并将事件分为系统事件和应用事件两类。系统事件来源于系统服务，是系统预先定义的事件，这类事件信息中的事件参数对象params包含的字段已由各系统事件定义，具体字段含义在各系统事件指南的介绍中，例如 [崩溃事件介绍](../../../dfx/hiappevent-watcher-crash-events.md)。应用事件来源于应用，是应用开发者自己定义的事件，这类事件信息支持自定义后通过[Write](arkts-performanceanalysis-hiappevent-write-f.md)打点接口进行配置设定，具体字段含义可结合开发者需求展开。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

## 导入模块

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [domain(应用事件打点)](arkts-performanceanalysis-hiappevent-domain-n.md) | 提供域名常量。  \|名称\|类型\|只读\|描述\| \| --- \| ------ \| ------ \| ---------- \| \| OS \| string \|是\|系统域\|
| [event(应用事件打点)](arkts-performanceanalysis-hiappevent-event-n.md) |
| [param(应用事件打点)](arkts-performanceanalysis-hiappevent-param-n.md) | 提供参数名常量。  \|名称\|类型\|只读\|描述\| \| ------------------------------- \| ------ \| ------ \| ------------------ \| \| USER_ID \| string \|是\|自定义用户ID\| \| DISTRIBUTED_SERVICE_NAME \| string \|是\|分布式服务名称\| \| DISTRIBUTED_SERVICE_INSTANCE_ID \| string \|是\|分布式服务实例ID\|

### 函数

| 名称 |
| --- |
| [configure(应用事件打点)](arkts-performanceanalysis-hiappevent-configure-f.md) |
| [write(应用事件打点)](arkts-performanceanalysis-hiappevent-write-f.md) |
| [write(应用事件打点)](arkts-performanceanalysis-hiappevent-write-f.md) |
| [setEventParam(应用事件打点)](arkts-performanceanalysis-hiappevent-seteventparam-f.md) |
| [setEventConfig(应用事件打点)](arkts-performanceanalysis-hiappevent-seteventconfig-f.md) |
| [addWatcher(应用事件打点)](arkts-performanceanalysis-hiappevent-addwatcher-f.md) |
| [removeWatcher(应用事件打点)](arkts-performanceanalysis-hiappevent-removewatcher-f.md) |
| [clearData(应用事件打点)](arkts-performanceanalysis-hiappevent-cleardata-f.md) |
| [setUserId(应用事件打点)](arkts-performanceanalysis-hiappevent-setuserid-f.md) |
| [getUserId(应用事件打点)](arkts-performanceanalysis-hiappevent-getuserid-f.md) |
| [setUserProperty(应用事件打点)](arkts-performanceanalysis-hiappevent-setuserproperty-f.md) |
| [getUserProperty(应用事件打点)](arkts-performanceanalysis-hiappevent-getuserproperty-f.md) |
| [addProcessor(应用事件打点)](arkts-performanceanalysis-hiappevent-addprocessor-f.md) |
| [addProcessorFromConfig(应用事件打点)](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md) |
| [removeProcessor(应用事件打点)](arkts-performanceanalysis-hiappevent-removeprocessor-f.md) |
| [configEventPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md) |

### 类

| 名称 |
| --- |
| [AppEventPackageHolder(应用事件打点)](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) |

### 接口

| 名称 |
| --- |
| [ConfigOption(应用事件打点)](arkts-performanceanalysis-hiappevent-configoption-i.md) |
| [AppEventInfo(应用事件打点)](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) |
| [AppEventPackage(应用事件打点)](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) |
| [TriggerCondition(应用事件打点)](arkts-performanceanalysis-hiappevent-triggercondition-i.md) |
| [AppEventFilter(应用事件打点)](arkts-performanceanalysis-hiappevent-appeventfilter-i.md) |
| [AppEventGroup(应用事件打点)](arkts-performanceanalysis-hiappevent-appeventgroup-i.md) |
| [Watcher(应用事件打点)](arkts-performanceanalysis-hiappevent-watcher-i.md) |
| [AppEventReportConfig(应用事件打点)](arkts-performanceanalysis-hiappevent-appeventreportconfig-i.md) |
| [Processor(应用事件打点)](arkts-performanceanalysis-hiappevent-processor-i.md) |
| [MainThreadJankPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-mainthreadjankpolicy-i.md) |
| [CpuUsageHighPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-cpuusagehighpolicy-i.md) |
| [AppCrashPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-appcrashpolicy-i.md) |
| [AppFreezePolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-appfreezepolicy-i.md) |
| [ResourceOverlimitPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-resourceoverlimitpolicy-i.md) |
| [AddressSanitizerPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-addresssanitizerpolicy-i.md) |
| [EventPolicy(应用事件打点)](arkts-performanceanalysis-hiappevent-eventpolicy-i.md) |

### 枚举

| 名称 |
| --- |
| [EventType(应用事件打点)](arkts-performanceanalysis-hiappevent-eventtype-e.md) |

### 类型

| 名称 |
| --- |
| [ParamType(应用事件打点)](arkts-performanceanalysis-hiappevent-paramtype-t.md) |
