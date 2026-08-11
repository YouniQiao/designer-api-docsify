# getProperty

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## getProperty

```TypeScript
function getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>
```

Obtains a property value. This API uses a promise to return the result.

The **propertyId** indicates the ID of the property to be queried. Currently, only the SKF API names defined in GMT0016-2023 can be used as property IDs. The supported IDs are as follows:

- SKF_EnumDev  
- SKF_GetDevInfo  
- SKF_EnumApplication  
- SKF_EnumContainer

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

<!--Device-huksExternalCrypto-function getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>--><!--Device-huksExternalCrypto-function getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceId | string | Yes |
| propertyId | string | Yes |
| params | Array&lt;HuksExternalCryptoParam&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;HuksExternalCryptoParam&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-unauthenticated-ukey-pin) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin-locked) |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
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

let propertyId = "SKF_EnumDev";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

console.info('promise: await huksExternalCrypto getProperty.');
async function testFunction() : Promise<void>
{
  try {
    await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
      .then((data) => {
        console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
      });
  } catch (error) {
    console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
  }
}
```
