# obtainAllWorks

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## obtainAllWorks

```TypeScript
function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>
```

Obtains all the deferred tasks. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [obtainAllWorks](#obtainallworks)(callback: AsyncCallback&lt;Array&lt;WorkInfo&gt;&gt;)

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9700001](../errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../errorcode-workScheduler.md#9700003-system-service-failure) |


## obtainAllWorks

```TypeScript
function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void
```

Obtains all the deferred tasks. This API uses an asynchronous callback to return the result.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9700001](../errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../errorcode-workScheduler.md#9700003-system-service-failure) |


## obtainAllWorks

```TypeScript
function obtainAllWorks(): Promise<Array<WorkInfo>>
```

Obtains all the deferred tasks. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9700001](../errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../errorcode-workScheduler.md#9700003-system-service-failure) |
