# @ohos.resourceschedule.usageStatistics(设备使用信息统计)

本模块提供设备使用信息统计能力，包括查询应用是否为常用应用、优先级分组、使用时长、系统事件（休眠、唤醒、解锁、锁屏）信息、应用事件（前台、后台、长时任务开始和结束）信息、通知次数等不同类型信息。

> **说明：**
> 
> 本模块接口为系统接口。

**起始版本：** 9

<!--Device-unnamed-declare namespace usageStatistics--><!--Device-unnamed-declare namespace usageStatistics-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isidlestate) |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isidlestate-1) |
| [isIdleStateSync](arkts-backgroundtasks-usagestatistics-isidlestatesync-f-sys.md#isidlestatesync) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryappgroup) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryappgroup-1) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryappgroup-2) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryappgroup-3) |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryappgroupsync) |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryappgroupsync-1) |
| [queryAppStatsInfos](arkts-backgroundtasks-usagestatistics-queryappstatsinfos-f-sys.md#queryappstatsinfos) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#querybundleevents) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#querybundleevents-1) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#querybundleevents-2) |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#querybundlestatsinfobyinterval) |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#querybundlestatsinfobyinterval-1) |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#querybundlestatsinfos) |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#querybundlestatsinfos-1) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#querycurrentbundleevents) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#querycurrentbundleevents-1) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#querycurrentbundleevents-2) |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#querydeviceeventstats) |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#querydeviceeventstats-1) |
| [queryLastUseTime](arkts-backgroundtasks-usagestatistics-querylastusetime-f-sys.md#querylastusetime) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#querymoduleusagerecords) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#querymoduleusagerecords-1) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#querymoduleusagerecords-2) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#querymoduleusagerecords-3) |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#querynotificationeventstats) |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#querynotificationeventstats-1) |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerappgroupcallback) |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerappgroupcallback-1) |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setappgroup) |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setappgroup-1) |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterappgroupcallback) |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterappgroupcallback-1) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AppGroupCallbackInfo](arkts-backgroundtasks-usagestatistics-appgroupcallbackinfo-i-sys.md) |
| [BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md) |
| [BundleStatsInfo](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md) |
| [DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md) |
| [HapFormInfo](arkts-backgroundtasks-usagestatistics-hapforminfo-i-sys.md) |
| [HapModuleInfo](arkts-backgroundtasks-usagestatistics-hapmoduleinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [GroupType](arkts-backgroundtasks-usagestatistics-grouptype-e-sys.md) |
| [IntervalType](arkts-backgroundtasks-usagestatistics-intervaltype-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AppStatsMap](arkts-backgroundtasks-usagestatistics-appstatsmap-t-sys.md) |
| [BundleStatsMap](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md) |
<!--DelEnd-->
