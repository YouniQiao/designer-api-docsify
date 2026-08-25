# scanFile

## Modules to Import

```TypeScript
import { identifySensitiveContent } from 'kits/@kit.DataProtectionKit';
```

## scanFile

```TypeScript
function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>
```

Identifies sensitive content in a specified file based on the configured policy and returns the identified result array, including the matched sensitivity labels, matched content, and number of matched items. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| identifyPolicies | Array & lt;Policy & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MatchResult](arkts-dataprotection-identifysensitivecontent-matchresult-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19110001](../errorcode-dlp.md#19110001-invalid-parameter) |
| [19110002](../errorcode-dlp.md#19110002-file-sensitive-content-identification-timed-out) |
| [19110003](../errorcode-dlp.md#19110003-file-not-supported) |
| [19110004](../errorcode-dlp.md#19110004-system-function-abnormal) |
