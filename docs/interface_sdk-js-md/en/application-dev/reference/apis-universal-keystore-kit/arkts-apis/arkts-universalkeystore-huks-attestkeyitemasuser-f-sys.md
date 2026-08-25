# attestKeyItemAsUser (System API)

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## attestKeyItemAsUser

```TypeScript
function attestKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<HuksReturnResult>
```

Attests a key for the specified user. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.ATTEST_KEY and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Security.Huks.Extension

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| keyAlias | string | Yes |
| huksOptions | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
