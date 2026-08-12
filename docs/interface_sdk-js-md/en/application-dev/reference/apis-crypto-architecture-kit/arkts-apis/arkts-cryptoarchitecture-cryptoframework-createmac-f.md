# createMac

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## createMac

```TypeScript
function createMac(algName: string): Mac
```

Creates a **Mac** instance.

&lt;br&gt;For details about the supported specifications, see  
[MAC Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createMac(algName: string): Mac--><!--Device-cryptoFramework-function createMac(algName: string): Mac-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | Specifies the digest algorithm. For details about the supported algorithms, see [MAC Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md) . |

**Return value:**

| Type | Description |
| --- | --- |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) | Returns the **Mac** instance corresponding to the specified algorithm. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let mac = cryptoFramework.createMac('SHA256');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```


## createMac

```TypeScript
function createMac(macSpec: MacSpec): Mac
```

Creates a **Mac** instance.

&lt;br&gt;For details about the supported specifications, see  
[MAC Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md).

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-cryptoFramework-function createMac(macSpec: MacSpec): Mac--><!--Device-cryptoFramework-function createMac(macSpec: MacSpec): Mac-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| macSpec | [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md) | Yes | Specifies the input parameter struct based on the MAC algorithm. For details about the supported algorithms, see [MAC Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md) . |

**Return value:**

| Type | Description |
| --- | --- |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) | Returns the **Mac** instance corresponding to the specified algorithm. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17620002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) | Failed to obtain the native object or convert parameters. |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let spec: cryptoFramework.HmacSpec = {
    algName: 'HMAC',
    mdName: 'SHA256',
  };
  let mac = cryptoFramework.createMac(spec);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

