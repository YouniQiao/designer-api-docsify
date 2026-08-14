# wrapKeyItem

## Modules to Import

```TypeScript
import { huks } from 'huks';
```

## wrapKeyItem

```TypeScript
function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>
```

Wraps a key. This API uses a promise to return the result. > **NOTE：**> > Wrapping SE security level keys that defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel) > requires the ohos.permission.ACCESS_SE_KEY permission. &lt;!--Del--&gt;This feature is not supported currently.&lt;!--DelEnd--&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-huks-function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | Key alias, which must be the same as the alias used when the key was generated. |
| params | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Encryption type of the key to be exported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | Promise that returns the operation result. If the operation is successful, **outData** in **HuksReturnResult** is the exported key ciphertext. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | api is not supported |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000004](../errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the input parameter is invalid |
| [201](../../errorcode-universal.md#201-permission-denied) | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**Applicable version:** 26.0.0 and later |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available<br>**Applicable version:** 26.0.0 and later |

