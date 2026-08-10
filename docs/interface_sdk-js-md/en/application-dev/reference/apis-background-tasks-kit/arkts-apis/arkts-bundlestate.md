# @ohos.bundleState(设备使用信息统计)

本模块提供设备使用信息统计能力。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-unnamed-declare namespace bundleState--><!--Device-unnamed-declare namespace bundleState-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

## Modules to Import

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [isIdleState](arkts-backgroundtasks-bundlestate-isidlestate-f.md#isidlestate) | 判断指定bundleName的应用当前是否是空闲状态，三方应用只能查询自身的空闲状态。系统应用支持查询其他应用的空闲状态，查询前需要申请权限ohos.permission.BUNDLE_ACTIVE_INFO。使用Callback异步回调。 |
| [isIdleState](arkts-backgroundtasks-bundlestate-isidlestate-f.md#isidlestate-1) | 判断指定bundleName的应用当前是否是空闲状态，三方应用只能查询自身的空闲状态。系统应用支持查询其他应用的空闲状态，查询前需要申请权限ohos.permission.BUNDLE_ACTIVE_INFO，使用Promise异步回调。 |
| [queryAppUsagePriorityGroup](arkts-backgroundtasks-bundlestate-queryappusageprioritygroup-f.md#queryappusageprioritygroup) | Queries the usage priority group of the calling application.  The priority defined in a priority group restricts the resource usage of an application,for example, restricting the running of background tasks. |
| [queryAppUsagePriorityGroup](arkts-backgroundtasks-bundlestate-queryappusageprioritygroup-f.md#queryappusageprioritygroup-1) | Queries the usage priority group of the calling application.  The priority defined in a priority group restricts the resource usage of an application,for example, restricting the running of background tasks. |
| [queryCurrentBundleActiveStates](arkts-backgroundtasks-bundlestate-querycurrentbundleactivestates-f.md#querycurrentbundleactivestates) | Queries state data of the current bundle within a specified period. |
| [queryCurrentBundleActiveStates](arkts-backgroundtasks-bundlestate-querycurrentbundleactivestates-f.md#querycurrentbundleactivestates-1) | Queries state data of the current bundle within a specified period. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [queryBundleActiveStates](arkts-backgroundtasks-bundlestate-querybundleactivestates-f-sys.md#querybundleactivestates) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleActiveStates](arkts-backgroundtasks-bundlestate-querybundleactivestates-f-sys.md#querybundleactivestates-1) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleStateInfoByInterval](arkts-backgroundtasks-bundlestate-querybundlestateinfobyinterval-f-sys.md#querybundlestateinfobyinterval) | Queries usage information about each bundle within a specified period at a specified interval. |
| [queryBundleStateInfoByInterval](arkts-backgroundtasks-bundlestate-querybundlestateinfobyinterval-f-sys.md#querybundlestateinfobyinterval-1) | Queries usage information about each bundle within a specified period at a specified interval. |
| [queryBundleStateInfos](arkts-backgroundtasks-bundlestate-querybundlestateinfos-f-sys.md#querybundlestateinfos) | Queries usage information about each bundle within a specified period.  This method queries usage information at the {@link #BY_OPTIMIZED} interval by default. |
| [queryBundleStateInfos](arkts-backgroundtasks-bundlestate-querybundlestateinfos-f-sys.md#querybundlestateinfos-1) | Queries usage information about each bundle within a specified period.  This method queries usage information at the {@link #BY_OPTIMIZED} interval by default. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BundleActiveInfoResponse](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md) |  |
| [BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) |  |
| [BundleStateInfo](arkts-backgroundtasks-bundlestate-bundlestateinfo-i.md) |  |

### Enums

| Name | Description |
| --- | --- |
| [IntervalType](arkts-backgroundtasks-bundlestate-intervaltype-e.md) | Declares interval type. |

