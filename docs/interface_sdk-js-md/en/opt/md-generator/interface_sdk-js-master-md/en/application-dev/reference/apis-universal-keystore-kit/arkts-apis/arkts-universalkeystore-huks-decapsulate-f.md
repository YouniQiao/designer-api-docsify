# decapsulate

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## decapsulate

```TypeScript
function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,
      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>
```

Decapsulates a post-quantum cryptography key. This operation can be managed by HUKS or the app itself. If the app chooses to manage the key,the symmetric key is contained in the outData field of HuksReturnResult.

**Since:** 26.0.0

<!--Device-huks-function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>--><!--Device-huks-function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | Yes |
| encapData | Uint8Array | Yes |
| sharedKeyAlias | string | No |
| sharedKeyParams | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;HuksReturnResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
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
