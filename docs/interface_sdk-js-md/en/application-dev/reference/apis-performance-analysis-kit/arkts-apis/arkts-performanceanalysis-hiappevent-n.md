# hiAppEvent(Application Event Logging)

This module provides application logging and event subscription capabilities, including event storage, event subscription, event clearance, and logging configuration. HiAppEvent records the events triggered during application running in [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md), and classifies the events into system events and application events.System events are triggered in system services and are predefined in the system. The fields of the event parameter object **params** of such events are defined by each system event. For details, see overviews of user guides. For example, [Crash Event Overview](../../../dfx/hiappevent-watcher-crash-events.md).Application events are defined by application developers and can be customized using the [Write](arkts-performanceanalysis-hiappevent-write-f.md) API as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [domain(Application Event Logging)](arkts-performanceanalysis-hiappevent-domain-n.md) | Provides domain name constants.  \| Name\| Type \| Read Only \| Description \| \| --- \| ------ \| ------ \| ---------- \| \| OS \| string \| Yes\| System domain.\|
| [event(Application Event Logging)](arkts-performanceanalysis-hiappevent-event-n.md) |
| [param(Application Event Logging)](arkts-performanceanalysis-hiappevent-param-n.md) | Provides parameter name constants.  \| Name \| Type \| Read Only \| Description \| \| ------------------------------- \| ------ \| ------ \| ------------------ \| \| USER_ID \| string \| Yes\| Custom user ID. \| \| DISTRIBUTED_SERVICE_NAME \| string \| Yes\| Distributed service name. \| \| DISTRIBUTED_SERVICE_INSTANCE_ID \| string \| Yes\| Distributed service instance ID.\|

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [configure(Application Event Logging)](arkts-performanceanalysis-hiappevent-configure-f.md) |
| [write(Application Event Logging)](arkts-performanceanalysis-hiappevent-write-f.md) |
| [write(Application Event Logging)](arkts-performanceanalysis-hiappevent-write-f.md) |
| [setEventParam(Application Event Logging)](arkts-performanceanalysis-hiappevent-seteventparam-f.md) |
| [setEventConfig(Application Event Logging)](arkts-performanceanalysis-hiappevent-seteventconfig-f.md) |
| [addWatcher(Application Event Logging)](arkts-performanceanalysis-hiappevent-addwatcher-f.md) |
| [removeWatcher(Application Event Logging)](arkts-performanceanalysis-hiappevent-removewatcher-f.md) |
| [clearData(Application Event Logging)](arkts-performanceanalysis-hiappevent-cleardata-f.md) |
| [setUserId(Application Event Logging)](arkts-performanceanalysis-hiappevent-setuserid-f.md) |
| [getUserId(Application Event Logging)](arkts-performanceanalysis-hiappevent-getuserid-f.md) |
| [setUserProperty(Application Event Logging)](arkts-performanceanalysis-hiappevent-setuserproperty-f.md) |
| [getUserProperty(Application Event Logging)](arkts-performanceanalysis-hiappevent-getuserproperty-f.md) |
| [addProcessor(Application Event Logging)](arkts-performanceanalysis-hiappevent-addprocessor-f.md) |
| [addProcessorFromConfig(Application Event Logging)](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md) |
| [removeProcessor(Application Event Logging)](arkts-performanceanalysis-hiappevent-removeprocessor-f.md) |
| [configEventPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md) |
| [registerExternalLogManager(Application Event Logging)](arkts-performanceanalysis-hiappevent-registerexternallogmanager-f.md) |
| [isExternalLogManagerRegistered(Application Event Logging)](arkts-performanceanalysis-hiappevent-isexternallogmanagerregistered-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppEventPackageHolder(Application Event Logging)](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) |
| [ExternalLogManager(Application Event Logging)](arkts-performanceanalysis-hiappevent-externallogmanager-c.md) |
| [ExternalLogContainer(Application Event Logging)](arkts-performanceanalysis-hiappevent-externallogcontainer-c.md) |
| [ExternalLogWrapper(Application Event Logging)](arkts-performanceanalysis-hiappevent-externallogwrapper-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConfigOption(Application Event Logging)](arkts-performanceanalysis-hiappevent-configoption-i.md) |
| [AppEventInfo(Application Event Logging)](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) |
| [AppEventPackage(Application Event Logging)](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) |
| [TriggerCondition(Application Event Logging)](arkts-performanceanalysis-hiappevent-triggercondition-i.md) |
| [AppEventFilter(Application Event Logging)](arkts-performanceanalysis-hiappevent-appeventfilter-i.md) |
| [AppEventGroup(Application Event Logging)](arkts-performanceanalysis-hiappevent-appeventgroup-i.md) |
| [Watcher(Application Event Logging)](arkts-performanceanalysis-hiappevent-watcher-i.md) |
| [AppEventReportConfig(Application Event Logging)](arkts-performanceanalysis-hiappevent-appeventreportconfig-i.md) |
| [Processor(Application Event Logging)](arkts-performanceanalysis-hiappevent-processor-i.md) |
| [MainThreadJankPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-mainthreadjankpolicy-i.md) |
| [CpuUsageHighPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-cpuusagehighpolicy-i.md) |
| [AppCrashPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-appcrashpolicy-i.md) |
| [AppFreezePolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-appfreezepolicy-i.md) |
| [ResourceOverlimitPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-resourceoverlimitpolicy-i.md) |
| [AddressSanitizerPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-addresssanitizerpolicy-i.md) |
| [EventPolicy(Application Event Logging)](arkts-performanceanalysis-hiappevent-eventpolicy-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EventType(Application Event Logging)](arkts-performanceanalysis-hiappevent-eventtype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ParamType(Application Event Logging)](arkts-performanceanalysis-hiappevent-paramtype-t.md) |
