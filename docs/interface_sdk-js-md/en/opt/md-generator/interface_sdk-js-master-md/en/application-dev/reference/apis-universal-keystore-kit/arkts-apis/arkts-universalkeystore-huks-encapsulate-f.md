# encapsulate

## Modules to Import

```TypeScript
```

## encapsulate

```TypeScript
function encapsulate(keyAlias: string, params: HuksParam[],
      sharedKeyAlias?: string, sharedKeyParams?: HuksParam[]): Promise<HuksReturnResult>
```

Post-Quantum Cryptography key encapsulation operation, supporting key management by HUKS or by the application itself. If the application chooses to manage the key, the symmetric key is carried in the outData field of HuksReturnResult.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-huks-function encapsulate(keyAlias: string, params: HuksParam[],      sharedKeyAlias?: string, sharedKeyParams?: HuksParam[]): Promise<HuksReturnResult>--><!--Device-huks-function encapsulate(keyAlias: string, params: HuksParam[],      sharedKeyAlias?: string, sharedKeyParams?: HuksParam[]): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | Yes |
| sharedKeyAlias | string | No |
| sharedKeyParams | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) |
| 12000016 |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000003](../errorcode-huks.md#12000003-invalid-key-algorithm-parameter) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000001](../errorcode-huks.md#12000001-feature-not-supported) |
| [12000015](../errorcode-huks.md#12000015-failed-to-invoke-other-system-services) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000013](../errorcode-huks.md#12000013-the-credential-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
