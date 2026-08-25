# authUkeyPin (System API)

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## authUkeyPin

```TypeScript
function authUkeyPin(resourceId: string, params: Array<HuksExternalCryptoParam>): Promise<void>
```

Authenticates a UKey PIN. This API uses a promise to return the result.

**Since:** 22

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceId | string | Yes |
| params | Array&lt;[HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000022](../errorcode-huks.md#12000022-incorrect-ukey-pin) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
