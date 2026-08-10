# queryCurrentBundleEvents (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryCurrentBundleEvents

```TypeScript
function queryCurrentBundleEvents(begin: long, end: long, callback: AsyncCallback<Array<BundleEvents>>): void
```

通过指定起始和结束时间，查询当前应用的事件集合，使用Callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, callback: AsyncCallback<Array<BundleEvents>>): void--><!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, callback: AsyncCallback<Array<BundleEvents>>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 起始时间，单位：ms。 |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 结束时间，单位：ms。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BundleEvents&gt;&gt; | Yes | 回调方法。 当查询成功，err为undefined，data为指定起始和结束时间段内，当前应用的事件集合；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
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

usageStatistics.queryCurrentBundleEvents(0, 20000000000000, (err: BusinessError, res: Array<usageStatistics.BundleEvents>) => {
  if (err) {
    console.error('BUNDLE_ACTIVE queryCurrentBundleEvents callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryCurrentBundleEvents callback success.');
    for (let i = 0; i < res.length; i++) {
      console.info('BUNDLE_ACTIVE queryCurrentBundleEvents callback number : ' + (i + 1));
      console.info('BUNDLE_ACTIVE queryCurrentBundleEvents callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## queryCurrentBundleEvents

```TypeScript
function queryCurrentBundleEvents(begin: long, end: long): Promise<Array<BundleEvents>>
```

通过指定起始和结束时间段内，查询当前应用的事件集合，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long): Promise<Array<BundleEvents>>--><!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long): Promise<Array<BundleEvents>>-End-->

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
| Promise&lt;Array&lt;BundleEvents&gt;&gt; | Promise对象。返回指定起始和结束时间段内，当前应用的事件集合。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
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

usageStatistics.queryCurrentBundleEvents(0, 20000000000000).then((res: Array<usageStatistics.BundleEvents>) => {
  console.info('BUNDLE_ACTIVE queryCurrentBundleEvents promise success.');
  for (let i = 0; i < res.length; i++) {
    console.info('BUNDLE_ACTIVE queryCurrentBundleEvents promise number : ' + (i + 1));
    console.info('BUNDLE_ACTIVE queryCurrentBundleEvents promise result ' + JSON.stringify(res[i]));
  }
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryCurrentBundleEvents promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```


## queryCurrentBundleEvents

```TypeScript
function queryCurrentBundleEvents(begin: long, end: long, maxNum: int): Promise<Array<BundleEvents>>
```

通过指定起始时间、结束时间及最大返回条数，查询指定时间段内当前应用的事件集合。若条数大于maxNum，则按事件发生时间降序排列，返回前maxNum条，否则返回所有数据。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, maxNum: int): Promise<Array<BundleEvents>>--><!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, maxNum: int): Promise<Array<BundleEvents>>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 起始时间。&lt;br/&gt;单位：ms |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 结束时间。&lt;br/&gt;单位：ms |
| maxNum | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 返回的事件的条数。&lt;br/&gt;取值范围：[1, 1000] |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleEvents&gt;&gt; | Promise对象，返回指定起始和结束时间段内，当前应用的事件集合。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10000008 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types; 3. Parameter verification failed. |
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

usageStatistics.queryCurrentBundleEvents(0, 20000000000000, 100).then((res: Array<usageStatistics.BundleEvents>) => {
  console.info('BUNDLE_ACTIVE queryCurrentBundleEvents promise success.');
  for (let i = 0; i < res.length; i++) {
    console.info('BUNDLE_ACTIVE queryCurrentBundleEvents promise number : ' + (i + 1));
    console.info('BUNDLE_ACTIVE queryCurrentBundleEvents promise result ' + JSON.stringify(res[i]));
  }
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryCurrentBundleEvents promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

