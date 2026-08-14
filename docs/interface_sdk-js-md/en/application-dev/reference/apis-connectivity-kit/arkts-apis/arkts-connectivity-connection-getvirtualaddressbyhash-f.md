# getVirtualAddressByHash

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## getVirtualAddressByHash

```TypeScript
function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string
```

Obtain the virtual address of the corresponding device based on the hash value of the real address.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string--><!--Device-connection-function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithmType | [HashAlgorithmType](arkts-connectivity-connection-hashalgorithmtype-e.md) | Yes | Indicate the hash algorithm type. |
| hashValue | string | Yes | Indicate the hash value of the device MAC address. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the virtual mac address. For example, "11:22:33:AA:BB:FF". |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| [2900015](../errorcode-bluetoothManager.md#2900015-parameter-format-inconsistent-with-specifications) | Parameter format mismatch with specification. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2900016](../errorcode-bluetoothManager.md#2900016-device-not-paired) | Device unpaired. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Internal system error. For example, IPC error. Detailed error messages can be used to assist in locating the problem. |

