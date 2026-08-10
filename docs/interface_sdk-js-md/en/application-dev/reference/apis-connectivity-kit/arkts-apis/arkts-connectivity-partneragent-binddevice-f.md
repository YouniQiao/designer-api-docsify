# bindDevice

## Modules to Import

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## bindDevice

```TypeScript
function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,
    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>
```

Bind the partner device.After successfully binding the device, if the device meets the discovery requirements,the {@link PartnerAgentExtensionAbility} of the application will be launched.  
- If the {@link DeviceCapability.supportBR} in the capability variable is set to true,  
 the application's ability will be launched when the device is connected via Bluetooth.  
- If the {@link DeviceCapability.supportBleAdvertiser} in the capability variable is set to true,  
 the application's ability will be launched when the device is detected via Bluetooth scanning.

Note: The device must be paired first.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>--><!--Device-partnerAgent-function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | Yes | The address of partner device. |
| deviceCapability | [DeviceCapability](arkts-connectivity-partneragent-devicecapability-i.md) | Yes | The capability of partner device. |
| businessCapability | [BusinessCapability](arkts-connectivity-partneragent-businesscapability-i.md) | Yes | The business capability of application. |
| partnerAgentExtensionAbilityName | string | Yes | The name of PartnerAgentExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 34900004 | The device has already been bound to the PartnerAgentExtensionAbility. |
| 801 | Capability not supported. |
| 34900005 | Bluetooth disabled. |
| 34900003 | The device is not paired. |
| 34900099 | Internal error. |
| 201 | Permission denied. |

