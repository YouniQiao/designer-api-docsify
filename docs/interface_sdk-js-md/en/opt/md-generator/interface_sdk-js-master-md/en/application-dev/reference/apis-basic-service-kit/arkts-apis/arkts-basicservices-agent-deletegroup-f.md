# deleteGroup

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## deleteGroup

```TypeScript
function deleteGroup(gid: string): Promise<void>
```

Deletes a specified group. No task ID can be added to the group. This API uses a promise to return the result.

When all tasks in a group are succeeded, failed, or removed and the group is deleted, the completion and failure notifications of this group are displayed.

**Since:** 15

<!--Device-agent-function deleteGroup(gid: string): Promise<void>--><!--Device-agent-function deleteGroup(gid: string): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21900008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900008-task-group-not-found-or-deleted) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
