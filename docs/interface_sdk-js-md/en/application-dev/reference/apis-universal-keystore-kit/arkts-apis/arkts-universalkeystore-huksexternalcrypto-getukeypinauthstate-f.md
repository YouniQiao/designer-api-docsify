# getUkeyPinAuthState

## getUkeyPinAuthState

```TypeScript
function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>
```

Obtains the PIN authentication state. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>--><!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceId | string | Yes | Resource ID, which can be obtained using [certificateManagerDialog.openAuthorizeDialog22+]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . The result contains **resourceId**. |
| params | Array&lt;HuksExternalCryptoParam&gt; | No | Operation parameters. If a non-system application passes [HUKS\_\_\_ESCAPED\_UNDERSCORE\_\_\_EXT\_\_\_ESCAPED\_UNDERSCORE\_\_\_CRYPTO\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_UID]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, the parameter is invalid. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksExternalPinAuthState&gt; | Promise used to return the authentication result. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**HUKS\_\_\_ESCAPED\_UNDERSCORE\_\_\_EXT\_\_\_ESCAPED\_UNDERSCORE\_\_\_CRYPTO\_\_\_ESCAPED\_UNDERSCORE\_\_\_PIN\_\_\_ESCAPED\_UNDERSCORE\_\_\_NO\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUTH**: The PIN authentication fails. **HUKS\_\_\_ESCAPED\_UNDERSCORE\_\_\_EXT\_\_\_ESCAPED\_UNDERSCORE\_\_\_CRYPTO\_\_\_ESCAPED\_UNDERSCORE\_\_\_PIN\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUTH\_\_\_ESCAPED\_UNDERSCORE\_\_\_SUCCEEDED**: The PIN authentication is successful. **HUKS\_\_\_ESCAPED\_UNDERSCORE\_\_\_EXT\_\_\_ESCAPED\_UNDERSCORE\_\_\_CRYPTO\_\_\_ESCAPED\_UNDERSCORE\_\_\_PIN\_\_\_ESCAPED\_UNDERSCORE\_\_\_LOCKED**: The PIN is locked. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | api is not supported. |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed. |
| [12000006](../errorcode-huks.md#12000006-algorithm-library-operation-failed) | the UKey driver operation failed. |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | queried entity does not exist. This may happen because the resource ID has not been opened. |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameter is abnormal. This error may occur if the process function is not found, or due to other issues. |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | memory is insufficient. |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | the input parameter is invalid. |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) | the provider operation failed. |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) | the provider or UKey is busy. |

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

const testResourceId = "{\"providerName\":\"testProviderName\", \"bundleName\":\"com.example.cryptoapplication\", \"abilityName\":\"CryptoExtension\",\"index\":{\"key\":\"testKey\"}}";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
    .then((data) => {
      console.info(`promise: getUkeyPinAuthState success, data: ${data}`);
    });
```

