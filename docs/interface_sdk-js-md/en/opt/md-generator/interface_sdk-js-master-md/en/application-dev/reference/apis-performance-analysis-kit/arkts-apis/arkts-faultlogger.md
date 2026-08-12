# @ohos.faultLogger(FaultLogger)

The **faultLogger** APIs can be used to query fault logs of an application cached on the system. The APIs use the application bundle name and the UID allocated by the system as the unique key value.

The number of application fault logs stored in the system is limited by the system log pressure. You are advised to use [@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md#hiAppEvent) to subscribe to fault events such as  
**APP_CRASH** and **APP_FREEZE**.

> **NOTE：**
> 
> The APIs of this module are no longer maintained since API version 18. You are advised to use
> [@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md#hiAppEvent) to subscribe to the **APP_CRASH** and
> **APP_FREEZE** events in later versions.
> 
> For details about how to use HiAppEvent to subscribe to the **APP_CRASH** event, see
> [Migrating Crash Events from the FaultLogger API](../../../dfx/hiappevent-watcher-crash-events-arkts.md#migrating-crash-events-from-the-faultlogger-api)
> .
> 
> For details about how to use HiAppEvent to subscribe to the **APP_FREEZE** event, see
> [Migrating Application Freeze Events from the Faultlogger API](../../../dfx/hiappevent-watcher-freeze-events-arkts.md#migrating-application-freeze-events-from-the-faultlogger-api)
> .

**Since:** 8

**Deprecated since:** 18

**Substitutes:** [hiAppEvent](ohos.hiviewdfx.hiAppEvent)

<!--Device-unnamed-declare namespace FaultLogger--><!--Device-unnamed-declare namespace FaultLogger-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Modules to Import

```TypeScript
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [query](arkts-performanceanalysis-faultlogger-query-f.md#query) |
| [query](arkts-performanceanalysis-faultlogger-query-f.md#query-1) |
| [querySelfFaultLog](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md#queryselffaultlog) |
| [querySelfFaultLog](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md#queryselffaultlog-1) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) |
