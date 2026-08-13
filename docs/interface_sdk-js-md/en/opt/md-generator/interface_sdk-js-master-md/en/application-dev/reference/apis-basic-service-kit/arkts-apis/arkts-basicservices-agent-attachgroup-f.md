# attachGroup

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## attachGroup

```TypeScript
function attachGroup(gid: string, tids: string[]): Promise<void>
```

Attaches multiple download task IDs to a specified group ID. This API uses a promise to return the result. If any task ID does not meet the attachment conditions, all tasks in the list will not be added to the group.

**Since:** 23

**Deprecated since:** -1

<!--Device-agent-function attachGroup(gid: string, tids: string[]): Promise<void>--><!--Device-agent-function attachGroup(gid: string, tids: string[]): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gid | string | Yes |
| tids | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900008](../../apis-basic-services-kit/errorcode-request.md#21900008-task-group-not-found-or-deleted) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-task-not-found) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
