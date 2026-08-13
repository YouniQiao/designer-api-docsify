# getVirtualAddressByHash

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## getVirtualAddressByHash

```TypeScript
function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string
```

Obtain the virtual address of the corresponding device based on the hash value of the real address.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string--><!--Device-connection-function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algorithmType | [HashAlgorithmType](arkts-connectivity-connection-hashalgorithmtype-e.md) | Yes |
| hashValue | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2900015](../errorcode-bluetoothManager.md#2900015-parameter-format-inconsistent-with-specifications) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2900016](../errorcode-bluetoothManager.md#2900016-device-not-paired) |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
// If the queried actual address is 11:22:33:44:55:AA,
// the corresponding 64-bit hash is d2204cb9b6d3d3962cc90fa54130efb4c10b57deb2e1aafd255596e0d4fd6789.
// If HashAlgorithmType is set to HASH_ALGORITHM_SHA256, the last 32 bits of the hash are used.
let hashValue: string = "c10b57deb2e1aafd255596e0d4fd6789";
try {
  let addr: string = connection.getVirtualAddressByHash(connection.HashAlgorithmType.HASH_ALGORITHM_SHA256, hashValue);
} catch (err) {
  console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
