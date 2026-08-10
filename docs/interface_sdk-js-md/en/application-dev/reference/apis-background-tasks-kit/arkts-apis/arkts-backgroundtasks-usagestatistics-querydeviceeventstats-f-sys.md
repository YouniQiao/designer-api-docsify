# queryDeviceEventStats (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryDeviceEventStats

```TypeScript
function queryDeviceEventStats(begin: long, end: long, callback: AsyncCallback<Array<DeviceEventStats>>): void
```

通过指定起始和结束时间，查询系统事件（休眠、唤醒、解锁、锁屏）的统计信息，使用Callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryDeviceEventStats(begin: long, end: long, callback: AsyncCallback<Array<DeviceEventStats>>): void--><!--Device-usageStatistics-function queryDeviceEventStats(begin: long, end: long, callback: AsyncCallback<Array<DeviceEventStats>>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 起始时间，单位：ms。 |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 结束时间，单位：ms。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;DeviceEventStats&gt;&gt; | Yes | 回调函数。 当查询成功，err为undefined，data为起始和结束时间段内，系统事件（休眠、唤醒、解锁、锁屏）的统计信息；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 10000001 | Memory operation failed. |
| 202 | Not System App. |
| 10000002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |
| 10000003 | Failed to get system ability manager. |
| 10000004 | Failed to access the device usage service. |
| 10000006 | Failed to get the application information. |
| 10000007 | Failed to get the system time. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryDeviceEventStats(0, 20000000000000, (err: BusinessError, res: Array<usageStatistics.DeviceEventStats>) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryDeviceEventStats callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryDeviceEventStats callback success.');
    console.info('BUNDLE_ACTIVE queryDeviceEventStats callback result ' + JSON.stringify(res));
  }
});
```


## queryDeviceEventStats

```TypeScript
function queryDeviceEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>
```

通过指定起始和结束时间，查询系统事件（休眠、唤醒、解锁、锁屏）的统计信息，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryDeviceEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>--><!--Device-usageStatistics-function queryDeviceEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 起始时间，单位：ms。 |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 结束时间，单位：ms。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;DeviceEventStats&gt;&gt; | Promise对象。返回起始和结束时间段内，系统事件（休眠、唤醒、解锁、锁屏）的统计信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 10000001 | Memory operation failed. |
| 202 | Not System App. |
| 10000002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |
| 10000003 | Failed to get system ability manager. |
| 10000004 | Failed to access the device usage service. |
| 10000006 | Failed to get the application information. |
| 10000007 | Failed to get the system time. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryDeviceEventStats(0, 20000000000000).then((res: Array<usageStatistics.DeviceEventStats>) => {
  console.info('BUNDLE_ACTIVE queryDeviceEventStates promise success.');
  console.info('BUNDLE_ACTIVE queryDeviceEventStates promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryDeviceEventStats promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

