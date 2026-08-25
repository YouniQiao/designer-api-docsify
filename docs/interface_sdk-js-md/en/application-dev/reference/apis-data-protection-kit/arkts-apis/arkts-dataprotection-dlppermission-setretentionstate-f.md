# setRetentionState

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setRetentionState

```TypeScript
function setRetentionState(docUris: Array<string>): Promise<void>
```

Sets the retention state for sandbox applications. By default, when a DLP file is opened, the system automatically creates a sandbox environment. After the file is closed, the sandbox is automatically destroyed. After the retention state is set, the sandbox environment is retained even if the DLP file is closed, allowing the system to quickly reopen the same DLP file. This is applicable to scenarios where the same DLP file needs to be frequently operated, improving the file opening efficiency. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [docUris](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100006](../errorcode-dlp.md#19100006-access-denied-for-a-non-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |


## setRetentionState

```TypeScript
function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void
```

Sets the retention state for sandbox applications. By default, when a DLP file is opened, the system automatically creates a sandbox environment. After the file is closed, the sandbox is automatically destroyed. After the retention state is set, the sandbox environment is retained even if the DLP file is closed, allowing the system to quickly reopen the same DLP file. This is applicable to scenarios where the same DLP file needs to be frequently operated, improving the file opening efficiency.

**Since:** 10

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [docUris](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100006](../errorcode-dlp.md#19100006-access-denied-for-a-non-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
