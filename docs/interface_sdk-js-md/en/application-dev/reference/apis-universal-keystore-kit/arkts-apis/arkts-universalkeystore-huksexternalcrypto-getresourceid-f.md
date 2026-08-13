# getResourceId

## Modules to Import

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
```

## getResourceId

```TypeScript
function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>
```

Obtain the resource ID of the provider.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-huksExternalCrypto-function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>--><!--Device-huksExternalCrypto-function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| providerName | string | Yes | Indicates the name of the external crypto provider and must be globally unique. One effective way is to include manufacturer information. |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | Yes | Indicates the input operation parameters, including the bundle name, ability name, and the related information to get the resource ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | API is not supported. |
| [12000005](../errorcode-huks.md#12000005-ipc-error) | IPC communication failed. |
| [12000020](../errorcode-huks.md#12000020-dependent-module-error) | The provider operation failed. This means an error occurred in the crypto extension before calling the UKey driver interface. |
| [12000002](../errorcode-huks.md#12000002-missing-key-algorithm-parameter) | The ability name, bundle name parameter or resource information is missing. |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) | Input parameters are invalid. Possible causes: 1. The providerName length is invalid. 2. The parameters contain invalid tags or invalid value types. |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) | The memory is insufficient. |
| [12000012](../errorcode-huks.md#12000012-external-error) | Device environment or input parameters are abnormal. This error may occur if the process function is not found, or due to other issues. |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) | The provider is not found. |
| [12000024](../errorcode-huks.md#12000024-device-or-resource-busy) | The provider or UKey is busy. |

