# registerProvider

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## registerProvider

```TypeScript
function registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>
```

Registers a specified external Provider. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.CRYPTO_EXTENSION_REGISTER

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| providerName | string | Yes |
| params | Array&lt;[HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000019](../errorcode-huks.md#12000019-provider-name-already-registered) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000025](../errorcode-huks.md#12000025-resource-limit-exceeded) |
