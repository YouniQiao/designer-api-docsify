# closeResource

## Modules to Import

```TypeScript
import { huksExternalCrypto } from 'kits/@kit.UniversalKeystoreKit';
```

## closeResource

```TypeScript
function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

关闭指定资源ID的资源。使用Promise异步回调。

该接口会回调  
[onClearUkeyPinAuthState](../../../reference/apis-universal-keystore-kit/js-apis-CryptoExtensionAbility.md#cryptoextensionabilityonclearukeypinauthstate)清理该资源关联的PIN认证状态，以及会回调  
[onFinishSession](../../../reference/apis-universal-keystore-kit/js-apis-CryptoExtensionAbility.md#cryptoextensionabilityonfinishsession)清理该资源关联的会话handle。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-huksExternalCrypto-function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>--><!--Device-huksExternalCrypto-function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceId | string | Yes | 资源ID。可通过 [证书选择接口](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md/arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md#openauthorizedialog) 获取keyUri作为resourceId，或通过[getResourceId](arkts-universalkeystore-huksexternalcrypto-getresourceid-f.md#getresourceid)获取外部密钥管理扩展的资源ID。 |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | No | 需要传递给 [Extension Ability](arkts-security-cryptoextensionability.md)的输入参数。不传入时，不向Extension Ability传递额外参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | API is not supported. |
| 12000006 | Failed to call the UKey driver interface. Please check the UKey connection and driver status. |
| 12000005 | IPC communication failed. |
| 12000020 | The provider operation failed. This means an error occurred in the crypto extension before calling the UKey driver interface. |
| 12000018 | Input parameters are invalid. Possible causes: 1. The resourceId length is invalid. 2. The parameters contain invalid tags or invalid value types. |
| 12000014 | The memory is insufficient. |
| 12000012 | Device environment or input parameters are abnormal. This error may occur if the process function is not found, or due to other issues. |
| 12000024 | The provider or UKey is busy. |

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

huksExternalCrypto.closeResource(testResourceId)
    .then(() => {
      console.info('promise: closeResource success.');
    });
```

