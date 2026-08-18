# remove

## Modules to Import

```TypeScript
```

## remove

```TypeScript
function remove(id: string, callback: AsyncCallback<void>): void
```

Removes a specified task of the invoker. If the task is being executed, the task is forced to stop. This API uses an asynchronous callback to return the result. After this API is called, the **task** object and its callback function are released.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-agent-function remove(id: string, callback: AsyncCallback<void>): void--><!--Device-agent-function remove(id: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |


## remove

```TypeScript
function remove(id: string): Promise<void>
```

Removes a specified task of the invoker. If the task is being executed, the task is forced to stop. This API uses a promise to return the result. After this API is called, the **task** object and its callback function are released.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-agent-function remove(id: string): Promise<void>--><!--Device-agent-function remove(id: string): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
