# @ohos.resourceschedule.usageStatistics

Provides methods for managing bundle usage statistics, including the methods for querying bundle usage information and state data. You can use the methods defined in this class to query the usage history and states of bundles in a specified period. The system stores the query result in a [BundleStatsInfo](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md#BundleStatsInfo-(System-API)) instance and then returns it to you.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace usageStatistics--><!--Device-unnamed-declare namespace usageStatistics-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

## Modules to Import

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isIdleState-(System-API)) |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isIdleState-(System-API)) |
| [isIdleStateSync](arkts-backgroundtasks-usagestatistics-isidlestatesync-f-sys.md#isIdleStateSync-(System-API)) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup-(System-API)) |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryAppGroupSync-(System-API)) |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryAppGroupSync-(System-API)) |
| [queryAppStatsInfos](arkts-backgroundtasks-usagestatistics-queryappstatsinfos-f-sys.md#queryAppStatsInfos-(System-API)) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents-(System-API)) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents-(System-API)) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents-(System-API)) |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#queryBundleStatsInfoByInterval-(System-API)) |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#queryBundleStatsInfoByInterval-(System-API)) |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#queryBundleStatsInfos-(System-API)) |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#queryBundleStatsInfos-(System-API)) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents-(System-API)) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents-(System-API)) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents-(System-API)) |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#queryDeviceEventStats-(System-API)) |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#queryDeviceEventStats-(System-API)) |
| [queryLastUseTime](arkts-backgroundtasks-usagestatistics-querylastusetime-f-sys.md#queryLastUseTime-(System-API)) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords-(System-API)) |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#queryNotificationEventStats-(System-API)) |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#queryNotificationEventStats-(System-API)) |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerAppGroupCallBack-(System-API)) |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerAppGroupCallBack-(System-API)) |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setAppGroup-(System-API)) |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setAppGroup-(System-API)) |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterAppGroupCallBack-(System-API)) |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterAppGroupCallBack-(System-API)) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppGroupCallbackInfo](arkts-backgroundtasks-usagestatistics-appgroupcallbackinfo-i-sys.md) |
| [BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md) |
| [BundleStatsInfo](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md) |
| [DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md) |
| [HapFormInfo](arkts-backgroundtasks-usagestatistics-hapforminfo-i-sys.md) |
| [HapModuleInfo](arkts-backgroundtasks-usagestatistics-hapmoduleinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GroupType](arkts-backgroundtasks-usagestatistics-grouptype-e-sys.md) |
| [IntervalType](arkts-backgroundtasks-usagestatistics-intervaltype-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppStatsMap](arkts-backgroundtasks-usagestatistics-appstatsmap-t-sys.md) |
| [BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md) |
<!--DelEnd-->
