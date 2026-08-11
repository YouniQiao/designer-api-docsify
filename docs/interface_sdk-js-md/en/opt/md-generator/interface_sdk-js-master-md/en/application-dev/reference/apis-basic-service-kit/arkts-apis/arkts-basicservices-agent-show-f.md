# show

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## show

```TypeScript
function show(id: string, callback: AsyncCallback<TaskInfo>): void
```

Queries the task details based on the task ID. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-agent-function show(id: string, callback: AsyncCallback<TaskInfo>): void--><!--Device-agent-function show(id: string, callback: AsyncCallback<TaskInfo>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |


## show

```TypeScript
function show(id: string): Promise<TaskInfo>
```

Queries the task details based on the task ID. This API uses a promise to return the result.

**Since:** 10

<!--Device-agent-function show(id: string): Promise<TaskInfo>--><!--Device-agent-function show(id: string): Promise<TaskInfo>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;TaskInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
