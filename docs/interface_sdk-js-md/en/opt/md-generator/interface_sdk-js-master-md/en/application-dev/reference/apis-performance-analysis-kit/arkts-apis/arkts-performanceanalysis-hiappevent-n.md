# hiAppEvent

This module provides application logging and event subscription capabilities, including event storage, event subscription, event clearance, and logging configuration. HiAppEvent records the events triggered during application running in [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md#AppEventInfo), and classifies the events into system events and application events. System events are triggered in system services and are predefined in the system. The fields of the event parameter object **params** of such events are defined by each system event. For details, see overviews of user guides. For example, [Crash Event Overview](../../../dfx/hiappevent-watcher-crash-events.md). Application events are defined by application developers and can be customized using the [Write](arkts-performanceanalysis-hiappevent-write-f.md#write) API as required.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace hiAppEvent--><!--Device-unnamed-declare namespace hiAppEvent-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [domain](arkts-performanceanalysis-hiappevent-domain-n.md) | Provides domain name constants. \| Name\| Type \| Read Only \| Description \| \| --- \| ------ \| ------ \| ---------- \| \| OS \| string \| Yes\| System domain.\|
| [event](arkts-performanceanalysis-hiappevent-event-n.md) |
| [param](arkts-performanceanalysis-hiappevent-param-n.md) | Provides parameter name constants. \| Name \| Type \| Read Only \| Description \| \| ------------------------------- \| ------ \| ------ \| ------------------ \| \| USER_ID \| string \| Yes\| Custom user ID. \| \| DISTRIBUTED_SERVICE_NAME \| string \| Yes\| Distributed service name. \| \| DISTRIBUTED_SERVICE_INSTANCE_ID \| string \| Yes\| Distributed service instance ID.\|

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [configure](arkts-performanceanalysis-hiappevent-configure-f.md#configure) |
| [write](arkts-performanceanalysis-hiappevent-write-f.md#write) |
| [write](arkts-performanceanalysis-hiappevent-write-f.md#write) |
| [setEventParam](arkts-performanceanalysis-hiappevent-seteventparam-f.md#setEventParam) |
| [setEventConfig](arkts-performanceanalysis-hiappevent-seteventconfig-f.md#setEventConfig) |
| [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addWatcher) |
| [removeWatcher](arkts-performanceanalysis-hiappevent-removewatcher-f.md#removeWatcher) |
| [clearData](arkts-performanceanalysis-hiappevent-cleardata-f.md#clearData) |
| [setUserId](arkts-performanceanalysis-hiappevent-setuserid-f.md#setUserId) |
| [getUserId](arkts-performanceanalysis-hiappevent-getuserid-f.md#getUserId) |
| [setUserProperty](arkts-performanceanalysis-hiappevent-setuserproperty-f.md#setUserProperty) |
| [getUserProperty](arkts-performanceanalysis-hiappevent-getuserproperty-f.md#getUserProperty) |
| [addProcessor](arkts-performanceanalysis-hiappevent-addprocessor-f.md#addProcessor) |
| [addProcessorFromConfig](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md#addProcessorFromConfig) |
| [removeProcessor](arkts-performanceanalysis-hiappevent-removeprocessor-f.md#removeProcessor) |
| [configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md#configEventPolicy) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppEventPackageHolder](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EventType](arkts-performanceanalysis-hiappevent-eventtype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md) |
