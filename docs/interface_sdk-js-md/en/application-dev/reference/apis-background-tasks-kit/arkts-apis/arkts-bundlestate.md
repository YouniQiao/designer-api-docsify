# @ohos.bundleState(Device Usage Statistics)

This module provides APIs for collecting statistics on device usage.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

## Modules to Import

```TypeScript
import bundleState from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [isIdleState(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-isidlestate-f.md) | Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only check the idle state of itself. A system application can check the idle state of other applications only when it is granted with the ohos.permission.BUNDLE_ACTIVE_INFO permission. This API uses an asynchronous callback to return the result. |
| [isIdleState(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-isidlestate-f.md) | Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only check the idle state of itself. A system application can check the idle state of other applications only when it is granted with the ohos.permission.BUNDLE_ACTIVE_INFO permission. This API uses a promise to return the result. |
| [queryAppUsagePriorityGroup(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-queryappusageprioritygroup-f.md) | Queries the usage priority group of the calling application.The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppUsagePriorityGroup(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-queryappusageprioritygroup-f.md) | Queries the usage priority group of the calling application.The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryCurrentBundleActiveStates(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querycurrentbundleactivestates-f.md) | Queries state data of the current bundle within a specified period. |
| [queryCurrentBundleActiveStates(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querycurrentbundleactivestates-f.md) | Queries state data of the current bundle within a specified period. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [queryBundleActiveStates(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querybundleactivestates-f-sys.md) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleActiveStates(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querybundleactivestates-f-sys.md) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleStateInfoByInterval(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querybundlestateinfobyinterval-f-sys.md) | Queries usage information about each bundle within a specified period at a specified interval. |
| [queryBundleStateInfoByInterval(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querybundlestateinfobyinterval-f-sys.md) | Queries usage information about each bundle within a specified period at a specified interval. |
| [queryBundleStateInfos(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querybundlestateinfos-f-sys.md) | Queries usage information about each bundle within a specified period.This method queries usage information at the BY_OPTIMIZED interval by default. |
| [queryBundleStateInfos(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-querybundlestateinfos-f-sys.md) | Queries usage information about each bundle within a specified period.This method queries usage information at the BY_OPTIMIZED interval by default. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BundleActiveInfoResponse(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md) |  |
| [BundleActiveState(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) |  |
| [BundleStateInfo(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-bundlestateinfo-i.md) |  |

### Enums

| Name | Description |
| --- | --- |
| [IntervalType(Device Usage Statistics)](arkts-backgroundtasks-bundlestate-intervaltype-e.md) | Declares interval type. |
