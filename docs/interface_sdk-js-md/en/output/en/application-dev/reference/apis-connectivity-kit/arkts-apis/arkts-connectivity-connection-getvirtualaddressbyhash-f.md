# getVirtualAddressByHash

## getVirtualAddressByHash

```TypeScript
function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string
```

Obtain the virtual address of the corresponding device based on the hash value of the real address.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string--><!--Device-connection-function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithmType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicate the hash algorithm type. |
| hashValue | string | Yes | Indicate the hash value of the device MAC address. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the virtual mac address. For example, "11:22:33:AA:BB:FF". |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| 2900003 | Bluetooth disabled. |
| [2900015](../errorcode-bluetoothManager.md#2900015-parameter-format-inconsistent-with-specifications) | Parameter format mismatch with specification. |
| [2900016](../errorcode-bluetoothManager.md#2900016-device-not-paired) | Device unpaired. |
| 2900099 | Internal system error. For example, IPC error.Detailed error messages can be used to assist in locating the problem. |

