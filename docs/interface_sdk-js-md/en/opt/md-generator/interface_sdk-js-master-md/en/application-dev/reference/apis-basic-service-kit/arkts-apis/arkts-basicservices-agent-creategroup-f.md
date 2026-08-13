# createGroup

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## createGroup

```TypeScript
function createGroup(config: GroupConfig): Promise<string>
```

Creates a group based on [GroupConfig](arkts-basicservices-agent-groupconfig-i.md#GroupConfig). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-agent-function createGroup(config: GroupConfig): Promise<string>--><!--Device-agent-function createGroup(config: GroupConfig): Promise<string>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [GroupConfig](arkts-basicservices-agent-groupconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
