# authUkeyPin (System API)

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## authUkeyPin

```TypeScript
function authUkeyPin(resourceId: string, params: Array<HuksExternalCryptoParam>): Promise<void>
```

PIN码认证。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-huksExternalCrypto-function authUkeyPin(resourceId: string, params: Array<HuksExternalCryptoParam>): Promise<void>--><!--Device-huksExternalCrypto-function authUkeyPin(resourceId: string, params: Array<HuksExternalCryptoParam>): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceId | string | Yes | Ukey中某容器的资源ID，可通过 [导出证书的接口](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md/arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md#openauthorizedialog) 获取，其结果中附带resourceId。 |
| params | Array&lt;HuksExternalCryptoParam&gt; | Yes | 操作时需传入的参数，必选TAG： [HUKS_EXT_CRYPTO_TAG_UKEY_PIN](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotagtype-e.md) 。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | api is not supported. |
| 12000006 | the UKey driver operation failed. |
| 12000022 | the UKey PIN is incorrect. |
| 12000005 | IPC communication failed. |
| 12000021 | the UKey PIN is locked. |
| 12000020 | the provider operation failed. |
| 12000018 | the input parameter is invalid. |
| 12000014 | memory is insufficient. |
| 202 | The caller is not a system application and is not allowed to use system applications. |
| 12000012 | Device environment or input parameter abnormal. This error may occur if the process function is not found, or due to other issues. |
| 12000011 | queried entity does not exist. |
| 12000024 | the provider or UKey is busy. |

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

let uid: number = 3511;
const testResourceId = "{\"providerName\":\"testProviderName\", \"bundleName\":\"com.example.cryptoapplication\", \"abilityName\":\"CryptoExtension\",\"index\":{\"key\":\"testKey\"}}";
const pin = "123456";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UID,
    value: uid
  }, {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UKEY_PIN,
    value: StringToUint8Array(pin)
  }
];
huksExternalCrypto.authUkeyPin(testResourceId, extProperties)
    .then((data) => {
        console.info(`promise: authUkeyPin success`);
    });
```

