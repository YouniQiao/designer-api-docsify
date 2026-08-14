# isDeviceBound

## Modules to Import

```TypeScript
import { partnerAgent } from 'partnerAgent';
```

## isDeviceBound

```TypeScript
function isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean
```

Checks whether a device is bound to this application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean--><!--Device-partnerAgent-function isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceAddress | PartnerDeviceAddress | Yes | The address of partner device. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the device is bound. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

