# getUkeyPinAuthState

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## getUkeyPinAuthState

```TypeScript
function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>
```

Obtains the PIN authentication state. This API uses a promise to return the result.

**Since:** 22

<!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>--><!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceId | string | Yes |
| params | Array&lt;HuksExternalCryptoParam&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;HuksExternalPinAuthState&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) |

## Examples

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

const testResourceId = "{\"providerName\":\"testProviderName\", \"bundleName\":\"com.example.cryptoapplication\", \"abilityName\":\"CryptoExtension\",\"index\":{\"key\":\"testKey\"}}";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
    .then((data) => {
      console.info(`promise: getUkeyPinAuthState success, data: ${data}`);
    });
```
