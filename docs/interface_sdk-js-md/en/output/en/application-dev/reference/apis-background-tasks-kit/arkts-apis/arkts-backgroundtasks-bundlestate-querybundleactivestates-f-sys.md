# queryBundleActiveStates (System API)

## queryBundleActiveStates

```TypeScript
function queryBundleActiveStates(begin: number, end: number, callback: AsyncCallback<Array<BundleActiveState>>): void
```

Queries state data of all bundles within a specified period identified by the start and end time.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-bundleState-function queryBundleActiveStates(begin: number, end: number, callback: AsyncCallback<Array<BundleActiveState>>): void--><!--Device-bundleState-function queryBundleActiveStates(begin: number, end: number, callback: AsyncCallback<Array<BundleActiveState>>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | Yes | Indicates the start time of the query period, in milliseconds. |
| end | number | Yes | Indicates the end time of the query period, in milliseconds. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;BundleActiveState&gt;&gt; | Yes | the state data of all bundles. |

**Example**

```TypeScript
import { BusinessError } from '@ohos.base';

bundleState.queryBundleActiveStates(0, 20000000000000, (err: BusinessError, res: Array<bundleState.BundleActiveState>) => {
  if (err) {
    console.error('BUNDLE_ACTIVE queryBundleActiveStates callback failed, because: ' + err.code);
  } else {
    console.info('BUNDLE_ACTIVE queryBundleActiveStates callback success.');
    for (let i = 0; i < res.length; i++) {
      console.info('BUNDLE_ACTIVE queryBundleActiveStates callback number : ' + (i + 1));
      console.info('BUNDLE_ACTIVE queryBundleActiveStates callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## queryBundleActiveStates

```TypeScript
function queryBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>
```

Queries state data of all bundles within a specified period identified by the start and end time.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-bundleState-function queryBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>--><!--Device-bundleState-function queryBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | number | Yes | Indicates the start time of the query period, in milliseconds. |
| end | number | Yes | Indicates the end time of the query period, in milliseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleActiveState&gt;&gt; | the state data of all bundles. |

**Example**

```TypeScript
import { BusinessError } from '@ohos.base';

bundleState.queryBundleActiveStates(0, 20000000000000).then((res: Array<bundleState.BundleActiveState>) => {
  console.info('BUNDLE_ACTIVE queryBundleActiveStates promise success.');
  for (let i = 0; i < res.length; i++) {
    console.info('BUNDLE_ACTIVE queryBundleActiveStates promise number : ' + (i + 1));
    console.info('BUNDLE_ACTIVE queryBundleActiveStates promise result ' + JSON.stringify(res[i]));
  }
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryBundleActiveStates promise failed, because: ' + err.code);
});
```

