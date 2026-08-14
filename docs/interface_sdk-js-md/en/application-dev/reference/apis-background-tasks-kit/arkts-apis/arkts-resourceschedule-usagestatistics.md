# @ohos.resourceschedule.usageStatistics

Provides methods for managing bundle usage statistics, including the methods for querying bundle usage information and state data. You can use the methods defined in this class to query the usage history and states of bundles in a specified period. The system stores the query result in a [BundleStatsInfo](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md#BundleStatsInfo-(System-API)) instance and then returns it to you.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace usageStatistics--><!--Device-unnamed-declare namespace usageStatistics-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

## Modules to Import

```TypeScript
import { usageStatistics } from 'usageStatistics';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isIdleState) | Checks whether the application with a specified bundle name is in the idle state. |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isIdleState-(System-API)) | Checks whether the application with a specified bundle name is in the idle state. |
| [isIdleStateSync](arkts-backgroundtasks-usagestatistics-isidlestatesync-f-sys.md#isIdleStateSync) | Checks whether the application with a specified bundle name is in the idle state. |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup) | Queries the app group of the calling application. The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) | Queries the app group of the calling application. The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) | Queries the usage priority group by bundleName. The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) | Queries the usage priority group by bundleName. The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryAppGroupSync) | Queries the app group of the calling application. The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryAppGroupSync-(System-API)) | Queries the usage priority group by bundleName. The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks. |
| [queryAppStatsInfos](arkts-backgroundtasks-usagestatistics-queryappstatsinfos-f-sys.md#queryAppStatsInfos) | Queries usage information about each application within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default. |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents-(System-API)) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents-(System-API)) | Queries state data of all bundles within a specified period identified by the start and end time. |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#queryBundleStatsInfoByInterval) | Queries usage information about each bundle within a specified period at a specified interval. |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#queryBundleStatsInfoByInterval-(System-API)) | Queries usage information about each bundle within a specified period at a specified interval. |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#queryBundleStatsInfos) | Queries usage information about each bundle within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default. |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#queryBundleStatsInfos-(System-API)) | Queries usage information about each bundle within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default. |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents) | Queries state data of the current bundle within a specified period. |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents-(System-API)) | Queries state data of the current bundle within a specified period. |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents-(System-API)) | Queries state data of the current bundle within a specified period. |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#queryDeviceEventStats) | Queries device event states data within a specified period identified by the start and end time. |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#queryDeviceEventStats-(System-API)) | Queries device event states data within a specified period identified by the start and end time. |
| [queryLastUseTime](arkts-backgroundtasks-usagestatistics-querylastusetime-f-sys.md#queryLastUseTime) | Queries the last usage timestamp by bundleName and app index. |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords) | Queries recently module usage records with maxNum. |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) | Queries recently module usage records with maxNum. |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) | Queries recently module usage records. |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) | Queries recently module usage records. |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#queryNotificationEventStats) | Queries app notification number within a specified period identified by the start and end time. |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#queryNotificationEventStats-(System-API)) | Queries app notification number within a specified period identified by the start and end time. |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerAppGroupCallBack) | Register appGroup change callback to service. |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerAppGroupCallBack-(System-API)) | Register appGroup change callback to service. |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setAppGroup) | Set app group by bundleName. |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setAppGroup-(System-API)) | Set app group by bundleName. |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterAppGroupCallBack) | Unregister appGroup change callback from service. |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterAppGroupCallBack-(System-API)) | Unregister appGroup change callback from service. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AppGroupCallbackInfo](arkts-backgroundtasks-usagestatistics-appgroupcallbackinfo-i-sys.md) |  |
| [BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md) |  |
| [BundleStatsInfo](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md) |  |
| [DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md) |  |
| [HapFormInfo](arkts-backgroundtasks-usagestatistics-hapforminfo-i-sys.md) |  |
| [HapModuleInfo](arkts-backgroundtasks-usagestatistics-hapmoduleinfo-i-sys.md) |  |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [GroupType](arkts-backgroundtasks-usagestatistics-grouptype-e-sys.md) | Declares group type. |
| [IntervalType](arkts-backgroundtasks-usagestatistics-intervaltype-e-sys.md) | Declares interval type. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [AppStatsMap](arkts-backgroundtasks-usagestatistics-appstatsmap-t-sys.md) |  |
| [BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md) |  |
<!--DelEnd-->

