# closeResource

## Modules to Import

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
```

## closeResource

```TypeScript
function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>
```

Close the resource with a specific resource ID.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-huksExternalCrypto-function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>--><!--Device-huksExternalCrypto-function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceId | string | Yes | Indicates the resource ID of the provider. |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | No | Indicates the input operation parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | API is not supported. |
| [12000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-algorithm-library-operation-failed) | Failed to call the UKey driver interface. Please check the UKey connection and driver status. |
| [12000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-ipc-error) | IPC communication failed. |
| [12000020](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000020-dependent-module-error) | The provider operation failed. This means an error occurred in the crypto extension before calling the UKey driver interface. |
| [12000018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-invalid-input-parameter) | Input parameters are invalid. Possible causes: 1. The resourceId length is invalid. 2. The parameters contain invalid tags or invalid value types. |
| [12000014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-insufficient-memory) | The memory is insufficient. |
| [12000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-external-error) | Device environment or input parameters are abnormal. This error may occur if the process function is not found, or due to other issues. |
| [12000024](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000024-device-or-resource-busy) | The provider or UKey is busy. |

