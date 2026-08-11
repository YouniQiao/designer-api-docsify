# openResource

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## openResource

```TypeScript
function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

Open resource by specific resource ID.NOTE: The opened resource must be closed using closeResource.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-huksExternalCrypto-function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>--><!--Device-huksExternalCrypto-function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceId | string | Yes |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000017](../errorcode-huks.md#12000017-duplicate-key-alias) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000025](../errorcode-huks.md#12000025-resource-limit-exceeded) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |

## Examples

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

const testResourceId = JSON.stringify({
  providerName: "testProviderName",
  bundleName: "com.example.cryptoapplication",
  abilityName: "CryptoExtension",
  index: {
    key: "testKey"
  } as ESObject
});

huksExternalCrypto.openResource(testResourceId)
    .then(() => {
      console.info('promise: openResource success.');
    });
```
