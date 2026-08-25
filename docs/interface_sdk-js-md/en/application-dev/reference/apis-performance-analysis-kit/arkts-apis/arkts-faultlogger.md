# @ohos.faultLogger(FaultLogger)

The **faultLogger** APIs can be used to query fault logs of an application cached on the system. The APIs use the application bundle name and the UID allocated by the system as the unique key value.The number of application fault logs stored in the system is limited by the system log pressure. You are advised to use [@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md) to subscribe to fault events such as **APP_CRASH** and **APP_FREEZE**. For details, see:  
- [Migrating Crash Events from the FaultLogger API](../../../dfx/hiappevent-watcher-crash-events-arkts.md#migrating-crash-events-from-the-faultlogger-api)  
- [Migrating Application Freeze Events from the Faultlogger API](../../../dfx/hiappevent-watcher-freeze-events-arkts.md#migrating-application-freeze-events-from-the-faultlogger-api)

**Since:** 8

**Deprecated since:** 18

**Substitutes:** hiAppEvent

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Modules to Import

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [query(FaultLogger)](arkts-performanceanalysis-faultlogger-query-f.md) |
| [query(FaultLogger)](arkts-performanceanalysis-faultlogger-query-f.md) |
| [querySelfFaultLog(FaultLogger)](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md) |
| [querySelfFaultLog(FaultLogger)](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FaultLogInfo(FaultLogger)](arkts-performanceanalysis-faultlogger-faultloginfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FaultType(FaultLogger)](arkts-performanceanalysis-faultlogger-faulttype-e.md) |
