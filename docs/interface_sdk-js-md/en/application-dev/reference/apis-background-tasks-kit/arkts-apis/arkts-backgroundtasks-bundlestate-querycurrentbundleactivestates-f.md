# queryCurrentBundleActiveStates

## Modules to Import

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryCurrentBundleActiveStates

```TypeScript
function queryCurrentBundleActiveStates(
    begin: number,
    end: number,
    callback: AsyncCallback<Array<BundleActiveState>>
  ): void
```

Queries state data of the current bundle within a specified period.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; | Yes |


## queryCurrentBundleActiveStates

```TypeScript
function queryCurrentBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>
```

Queries state data of the current bundle within a specified period.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; |
