# getUkeyPinAuthState

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## getUkeyPinAuthState

```TypeScript
function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>
```

获取PIN码认证状态。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>--><!--Device-huksExternalCrypto-function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceId | string | Yes | 资源ID，可通过 [导出证书的接口](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md/arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md#openauthorizedialog) 获取，其结果中附带资源ID。 |
| params | Array&lt;HuksExternalCryptoParam&gt; | No | 操作的属性。非系统应用传入 [HUKS_EXT_CRYPTO_TAG_UID](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotagtype-e.md)是非法参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksExternalPinAuthState&gt; | Promise对象，返回认证结果。 &lt;br&gt;HUKS_EXT_CRYPTO_PIN_NO_AUTH 表示未认证；HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED 表示认证成功；HUKS_EXT_CRYPTO_PIN_LOCKED 表示PIN被锁定。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | api is not supported. |
| 12000006 | the UKey driver operation failed. |
| 12000005 | IPC communication failed. |
| 12000020 | the provider operation failed. |
| 12000018 | the input parameter is invalid. |
| 12000014 | memory is insufficient. |
| 12000012 | Device environment or input parameter is abnormal. This error may occur if the process function is not found, or due to other issues. |
| 12000011 | queried entity does not exist. This may happen because the resource ID has not been opened. |
| 12000024 | the provider or UKey is busy. |

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

