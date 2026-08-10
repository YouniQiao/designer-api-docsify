# getBoundDevices

## Modules to Import

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## getBoundDevices

```TypeScript
function getBoundDevices(): PartnerDeviceAddress[]
```

Gets the list of addresses of the bound partner device for this application.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function getBoundDevices(): PartnerDeviceAddress[]--><!--Device-partnerAgent-function getBoundDevices(): PartnerDeviceAddress[]-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Return value:**

| Type | Description |
| --- | --- |
| [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md)[] | Returns the list of addresses of partner device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 34900099 | Internal error. |
| 201 | Permission denied. |

