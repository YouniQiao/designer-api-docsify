# unregisterProvider

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## unregisterProvider

```TypeScript
function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>
```

Unregisters a specified external Provider. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.CRYPTO_EXTENSION_REGISTER

<!--Device-huksExternalCrypto-function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>--><!--Device-huksExternalCrypto-function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| providerName | string | Yes |
| params | Array&lt;HuksExternalCryptoParam&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |

## Examples

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

const providerName = "testProviderName";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
    value: StringToUint8Array("CryptoExtension")
  }
];
huksExternalCrypto.unregisterProvider(providerName, extProperties)
    .then((data) => {
        console.info('promise: unregisterProvider success.');
    });
```
