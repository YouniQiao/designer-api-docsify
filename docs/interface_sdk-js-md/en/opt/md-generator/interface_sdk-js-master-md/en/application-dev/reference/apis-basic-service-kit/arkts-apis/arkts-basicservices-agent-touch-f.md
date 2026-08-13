# touch

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## touch

```TypeScript
function touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void
```

Queries the task details based on the task ID and token. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-agent-function touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void--><!--Device-agent-function touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| token | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |


## touch

```TypeScript
function touch(id: string, token: string): Promise<TaskInfo>
```

Queries the task details based on the task ID and token. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-agent-function touch(id: string, token: string): Promise<TaskInfo>--><!--Device-agent-function touch(id: string, token: string): Promise<TaskInfo>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| token | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;TaskInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
