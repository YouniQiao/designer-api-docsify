# queryBundleStateInfos (System API)

## Modules to Import

```TypeScript
import { bundleState } from 'bundleState';
```

## queryBundleStateInfos

```TypeScript
function queryBundleStateInfos(begin: number, end: number, callback: AsyncCallback<BundleActiveInfoResponse>): void
```

Queries usage information about each bundle within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-bundleState-function queryBundleStateInfos(begin: number, end: number, callback: AsyncCallback<BundleActiveInfoResponse>): void--><!--Device-bundleState-function queryBundleStateInfos(begin: number, end: number, callback: AsyncCallback<BundleActiveInfoResponse>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | number | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleActiveInfoResponse](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md)&gt; | Yes | the callback of queryBundleStateInfos. the [BundleActiveInfoResponse](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md#bundleactiveinforesponse) objects containing the usage information about each bundle. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';

bundleState.queryBundleStateInfos(0, 20000000000000, (err: BusinessError ,
  res: bundleState.BundleActiveInfoResponse ) => {
  if (err) {
    console.error('BUNDLE_ACTIVE queryBundleStateInfos callback failed, because: ' + err.code);
  } else {
    console.info('BUNDLE_ACTIVE queryBundleStateInfos callback success.');
    console.info('BUNDLE_ACTIVE queryBundleStateInfos callback result ' + JSON.stringify(res));
  }
});
```


## queryBundleStateInfos

```TypeScript
function queryBundleStateInfos(begin: number, end: number): Promise<BundleActiveInfoResponse>
```

Queries usage information about each bundle within a specified period. This method queries usage information at the BY_OPTIMIZED interval by default.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-bundleState-function queryBundleStateInfos(begin: number, end: number): Promise<BundleActiveInfoResponse>--><!--Device-bundleState-function queryBundleStateInfos(begin: number, end: number): Promise<BundleActiveInfoResponse>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | Yes | Indicates the start time of the query period, in milliseconds. <br> Unit:ms |
| end | number | Yes | Indicates the end time of the query period, in milliseconds. <br> Unit:ms |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[BundleActiveInfoResponse](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md)&gt; | the promise returned by queryBundleStatsInfos. the { |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';

bundleState.queryBundleStateInfos(0, 20000000000000).then((res: bundleState.BundleActiveInfoResponse) => {
  console.info('BUNDLE_ACTIVE queryBundleStateInfos promise success.');
  console.info('BUNDLE_ACTIVE queryBundleStateInfos promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryBundleStateInfos promise failed, because: ' + err.code);
});
```

