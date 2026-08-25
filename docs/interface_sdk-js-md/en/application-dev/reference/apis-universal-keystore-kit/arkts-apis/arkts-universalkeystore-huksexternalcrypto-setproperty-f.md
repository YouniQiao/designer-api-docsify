# setProperty

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## setProperty

```TypeScript
function setProperty(resourceId: string, propertyId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

The set-type operations of the external crypto extension support calling custom interfaces. However, the custom interface must be registered with the provider.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceId | string | Yes |
| propertyId | string | Yes |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |
