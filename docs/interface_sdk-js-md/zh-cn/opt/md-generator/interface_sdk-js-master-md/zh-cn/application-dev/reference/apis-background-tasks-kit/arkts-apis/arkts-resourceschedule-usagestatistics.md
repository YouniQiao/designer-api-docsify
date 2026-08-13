# @ohos.resourceschedule.usageStatistics

本模块提供设备使用信息统计能力，包括查询应用是否为常用应用、优先级分组、使用时长、系统事件（休眠、唤醒、解锁、锁屏）信息、应用事件（前台、后台、长时任务开始和结束）信息、通知次数等不同类型信息。 > **说明：** > > 本模块接口为系统接口。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace usageStatistics--><!--Device-unnamed-declare namespace usageStatistics-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isIdleState（系统接口）) |
| [isIdleState](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md#isIdleState（系统接口）) |
| [isIdleStateSync](arkts-backgroundtasks-usagestatistics-isidlestatesync-f-sys.md#isIdleStateSync（系统接口）) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup（系统接口）) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup（系统接口）) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup（系统接口）) |
| [queryAppGroup](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md#queryAppGroup（系统接口）) |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryAppGroupSync（系统接口）) |
| [queryAppGroupSync](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md#queryAppGroupSync（系统接口）) |
| [queryAppStatsInfos](arkts-backgroundtasks-usagestatistics-queryappstatsinfos-f-sys.md#queryAppStatsInfos（系统接口）) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents（系统接口）) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents（系统接口）) |
| [queryBundleEvents](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md#queryBundleEvents（系统接口）) |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#queryBundleStatsInfoByInterval（系统接口）) |
| [queryBundleStatsInfoByInterval](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md#queryBundleStatsInfoByInterval（系统接口）) |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#queryBundleStatsInfos（系统接口）) |
| [queryBundleStatsInfos](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md#queryBundleStatsInfos（系统接口）) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents（系统接口）) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents（系统接口）) |
| [queryCurrentBundleEvents](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md#queryCurrentBundleEvents（系统接口）) |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#queryDeviceEventStats（系统接口）) |
| [queryDeviceEventStats](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md#queryDeviceEventStats（系统接口）) |
| [queryLastUseTime](arkts-backgroundtasks-usagestatistics-querylastusetime-f-sys.md#queryLastUseTime（系统接口）) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords（系统接口）) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords（系统接口）) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords（系统接口）) |
| [queryModuleUsageRecords](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md#queryModuleUsageRecords（系统接口）) |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#queryNotificationEventStats（系统接口）) |
| [queryNotificationEventStats](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md#queryNotificationEventStats（系统接口）) |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerAppGroupCallBack（系统接口）) |
| [registerAppGroupCallBack](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md#registerAppGroupCallBack（系统接口）) |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setAppGroup（系统接口）) |
| [setAppGroup](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md#setAppGroup（系统接口）) |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterAppGroupCallBack（系统接口）) |
| [unregisterAppGroupCallBack](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md#unregisterAppGroupCallBack（系统接口）) |
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
