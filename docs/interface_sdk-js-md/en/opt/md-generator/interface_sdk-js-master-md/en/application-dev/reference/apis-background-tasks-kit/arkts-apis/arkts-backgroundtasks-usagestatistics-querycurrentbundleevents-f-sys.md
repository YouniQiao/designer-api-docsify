# queryCurrentBundleEvents (System API)

## Modules to Import

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## queryCurrentBundleEvents

```TypeScript
function queryCurrentBundleEvents(begin: number, end: number, callback: AsyncCallback<Array<BundleEvents>>): void
```

Queries state data of the current bundle within a specified period.

**Since:** 23

**Deprecated since:** -1

<!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, callback: AsyncCallback<Array<BundleEvents>>): void--><!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, callback: AsyncCallback<Array<BundleEvents>>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) |

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
function queryCurrentBundleEvents(begin: number, end: number): Promise<Array<BundleEvents>>
```

Queries state data of the current bundle within a specified period.

**Since:** 23

**Deprecated since:** -1

<!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long): Promise<Array<BundleEvents>>--><!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long): Promise<Array<BundleEvents>>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) |

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
function queryCurrentBundleEvents(begin: number, end: number, maxNum: number): Promise<Array<BundleEvents>>
```

Queries state data of the current bundle within a specified period.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, maxNum: int): Promise<Array<BundleEvents>>--><!--Device-usageStatistics-function queryCurrentBundleEvents(begin: long, end: long, maxNum: int): Promise<Array<BundleEvents>>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |
| maxNum | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10000008](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000008-parameter-check-failed) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-memory-operation-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failure) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-system-service-operation-failure) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-ipc-failure) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-failed-to-obtain-application-information) |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-time-operation-failure) |

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
