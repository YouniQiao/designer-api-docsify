# unregisterProvider

## unregisterProvider

```TypeScript
function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>
```

Unregisters a specified external Provider. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Required permissions:** ohos.permission.CRYPTO_EXTENSION_REGISTER

<!--Device-huksExternalCrypto-function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>--><!--Device-huksExternalCrypto-function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| providerName | string | Yes | Provider name, which contains a maximum of 128 characters. It is recommended that the value contain the vendor information, be globally unique, and not contain sensitive data such as personal contact information. If a provider has registered multiple extension capabilities, all the extension capabilities of the provider will be unregistered. |
| params | Array&lt;HuksExternalCryptoParam&gt; | No | Parameters to be passed during the operation.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_You can specify [HUKS\_\_\_ESCAPED\_UNDERSCORE\_\_\_EXT\_\_\_ESCAPED\_UNDERSCORE\_\_\_CRYPTO\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_ABILITY\_\_\_ESCAPED\_UNDERSCORE\_\_\_NAME]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ in the **params** parameter to unregister the corresponding **cryptoExtensionAbility** based on the bundle name,**providerName**, and **abilityName**.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_3\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If [HUKS\_\_\_ESCAPED\_UNDERSCORE\_\_\_EXT\_\_\_ESCAPED\_UNDERSCORE\_\_\_CRYPTO\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_ABILITY\_\_\_ESCAPED\_UNDERSCORE\_\_\_NAME]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is not specified in the **params** parameter or the **params** parameter is not passed, all providers under the corresponding **providerName** are unregistered. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | check permission failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported. |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed. |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | the provider is not found. |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter is abnormal.This may happen for several reasons, such as the model already being unloaded. |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient. |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the input parameter is invalid. |

**Example**

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
        console.info(`promise: unregisterProvider success`);
    });
```

