# @ohos.resourceschedule.usageStatistics(设备使用信息统计)

本模块提供设备使用信息统计能力，包括查询应用是否为常用应用、优先级分组、使用时长、系统事件（休眠、唤醒、解锁、锁屏）信息、应用事件（前台、后台、长时任务开始和结束）信息、通知次数等不同类型信息。

> **说明：**&gt;
> 本模块接口为系统接口。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

## 导入模块

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isIdleState(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md) |
| [isIdleState(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-isidlestate-f-sys.md) |
| [isIdleStateSync(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-isidlestatesync-f-sys.md) |
| [queryAppGroup(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md) |
| [queryAppGroup(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md) |
| [queryAppGroup(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md) |
| [queryAppGroup(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappgroup-f-sys.md) |
| [queryAppGroupSync(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md) |
| [queryAppGroupSync(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappgroupsync-f-sys.md) |
| [queryAppStatsInfos(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-queryappstatsinfos-f-sys.md) |
| [queryBundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md) |
| [queryBundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md) |
| [queryBundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundleevents-f-sys.md) |
| [queryBundleStatsInfoByInterval(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md) |
| [queryBundleStatsInfoByInterval(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundlestatsinfobyinterval-f-sys.md) |
| [queryBundleStatsInfos(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md) |
| [queryBundleStatsInfos(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querybundlestatsinfos-f-sys.md) |
| [queryCurrentBundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md) |
| [queryCurrentBundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md) |
| [queryCurrentBundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querycurrentbundleevents-f-sys.md) |
| [queryDeviceEventStats(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md) |
| [queryDeviceEventStats(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querydeviceeventstats-f-sys.md) |
| [queryLastUseTime(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querylastusetime-f-sys.md) |
| [queryModuleUsageRecords(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md) |
| [queryModuleUsageRecords(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md) |
| [queryModuleUsageRecords(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md) |
| [queryModuleUsageRecords(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querymoduleusagerecords-f-sys.md) |
| [queryNotificationEventStats(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md) |
| [queryNotificationEventStats(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-querynotificationeventstats-f-sys.md) |
| [registerAppGroupCallBack(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md) |
| [registerAppGroupCallBack(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-registerappgroupcallback-f-sys.md) |
| [setAppGroup(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md) |
| [setAppGroup(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-setappgroup-f-sys.md) |
| [unregisterAppGroupCallBack(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md) |
| [unregisterAppGroupCallBack(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-unregisterappgroupcallback-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AppGroupCallbackInfo(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-appgroupcallbackinfo-i-sys.md) |
| [BundleEvents(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md) |
| [BundleStatsInfo(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-bundlestatsinfo-i-sys.md) |
| [DeviceEventStats(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md) |
| [HapFormInfo(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-hapforminfo-i-sys.md) |
| [HapModuleInfo(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-hapmoduleinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [GroupType(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-grouptype-e-sys.md) |
| [IntervalType(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-intervaltype-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AppStatsMap(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-appstatsmap-t-sys.md) |
| [BundleStatsMap(设备使用信息统计)](arkts-backgroundtasks-usagestatistics-bundlestatsmap-t-sys.md) |
<!--DelEnd-->
