# grantUriPermissionByKey (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## grantUriPermissionByKey

```TypeScript
function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: number): Promise<void>
```

Grants the URI access permission of the current application to the target application through the unique key of the Unified Data Management Framework (UDMF) data. The permission will be revoked after the target application exits. This API uses a promise to return the result. This API can be properly called only on phones, 2-in-1 devices, and tablets. If it is called on other device types, error code 801 is returned. **System API**: This is a system API.

**Since:** 20

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| flag | wantConstant.Flags | Yes |
| targetTokenId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000058](../errorcode-ability.md#16000058-specified-uri-flag-is-invalid) |
| [16000060](../errorcode-ability.md#16000060-sandbox-applications-cannot-grant-uri-permission) |
| [16000091](../errorcode-ability.md#16000091-failed-to-obtain-a-file-uri-by-key) |
| [16000092](../errorcode-ability.md#16000092-no-permission-to-authorize-uri) |
| [16000094](../errorcode-ability.md#16000094-invalid-target-token-id) |
