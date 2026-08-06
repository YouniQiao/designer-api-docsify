# wrapKeyItem

## wrapKeyItem

```TypeScript
function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>
```

Wraps a key. This API uses a promise to return the result.
    **NOTE**  
    
    Wrapping SE security level keys that defined in [HuksKeySecurityLevel]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_  
    requires the ohos.permission.ACCESS\_SE\_KEY permission.

\_\_\_MD\_COMMENT\_DESC\_USD\_1\_\_\_This feature is not supported currently.\_\_\_MD\_COMMENT\_DESC\_USD\_2\_\_\_

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-huks-function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | Key alias, which must be the same as the alias used when the key was generated. |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Encryption type of the key to be exported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksReturnResult&gt; | Promise that returns the operation result. If the operation is successful, **outData** in **HuksReturnResult** is the exported key ciphertext. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | The application permissions are insufficient, possibly because the ohos.permission.ACCESS\_\_\_ESCAPED\_UNDERSCORE\_\_\_SE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY permission is missing.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 26.0.0 and later |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported |
| [12000004](../errorcode-huks.md#12000004-file-error) | operating file failed |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter abnormal |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the input parameter is invalid |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) | the secure element is not available\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 26.0.0 and later |

