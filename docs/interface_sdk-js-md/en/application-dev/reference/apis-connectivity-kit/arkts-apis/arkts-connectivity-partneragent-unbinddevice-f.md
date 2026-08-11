# unbindDevice

## Modules to Import

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## unbindDevice

```TypeScript
function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>
```

Unbinds a partner device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>--><!--Device-partnerAgent-function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | Yes | The address of partner device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [34900001](../errorcode-fusionConnectivity.md#34900001-device-not-registered) | The device is not bound. |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

