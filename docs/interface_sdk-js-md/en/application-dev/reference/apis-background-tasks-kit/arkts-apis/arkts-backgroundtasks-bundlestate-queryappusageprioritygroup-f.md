# queryAppUsagePriorityGroup

## Modules to Import

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryAppUsagePriorityGroup

```TypeScript
function queryAppUsagePriorityGroup(callback: AsyncCallback<number>): void
```

Queries the usage priority group of the calling application.The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## queryAppUsagePriorityGroup

```TypeScript
function queryAppUsagePriorityGroup(): Promise<number>
```

Queries the usage priority group of the calling application.The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |
