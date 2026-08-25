# queryBundleActiveStates (System API)

## Modules to Import

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryBundleActiveStates

```TypeScript
function queryBundleActiveStates(begin: number, end: number, callback: AsyncCallback<Array<BundleActiveState>>): void
```

Queries state data of all bundles within a specified period identified by the start and end time.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; | Yes |


## queryBundleActiveStates

```TypeScript
function queryBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>
```

Queries state data of all bundles within a specified period identified by the start and end time.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.BUNDLE_ACTIVE_INFO

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
| Promise&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; |
