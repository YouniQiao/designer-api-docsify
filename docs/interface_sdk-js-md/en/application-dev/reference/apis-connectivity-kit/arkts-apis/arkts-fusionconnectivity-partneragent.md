# @ohos.FusionConnectivity.partnerAgent

Provides APIs for managing partner agents.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace partnerAgent--><!--Device-unnamed-declare namespace partnerAgent-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

## Modules to Import

```TypeScript
import { partnerAgent } from 'partnerAgent';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [bindDevice](arkts-connectivity-partneragent-binddevice-f.md#bindDevice) | Bind the partner device. After successfully binding the device, if the device meets the discovery requirements, the [PartnerAgentExtensionAbility](arkts-connectivity-fusionconnectivity-partneragentextensionability-partneragentextensionability-c.md#PartnerAgentExtensionAbility) of the application will be launched. - If the [supportBR](arkts-connectivity-partneragent-devicecapability-i.md#supportBR) in the capability variable is set to true, the application's ability will be launched when the device is connected via Bluetooth. - If the [supportBleAdvertiser](arkts-connectivity-partneragent-devicecapability-i.md#supportBleAdvertiser) in the capability variable is set to true, the application's ability will be launched when the device is detected via Bluetooth scanning. Note: The device must be paired first. |
| [getBoundDevices](arkts-connectivity-partneragent-getbounddevices-f.md#getBoundDevices) | Gets the list of addresses of the bound partner device for this application. |
| [isDeviceBound](arkts-connectivity-partneragent-isdevicebound-f.md#isDeviceBound) | Checks whether a device is bound to this application. |
| [isDeviceControlEnabled](arkts-connectivity-partneragent-isdevicecontrolenabled-f.md#isDeviceControlEnabled) | Checks whether device control is enabled. |
| [isPartnerAgentSupported](arkts-connectivity-partneragent-ispartneragentsupported-f.md#isPartnerAgentSupported) | Checks whether the current device supports the partner agent feature. |
| [unbindDevice](arkts-connectivity-partneragent-unbinddevice-f.md#unbindDevice) | Unbinds a partner device. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disableDeviceControl](arkts-connectivity-partneragent-disabledevicecontrol-f-sys.md#disableDeviceControl) | Disables device control for a bound device. |
| [enableDeviceControl](arkts-connectivity-partneragent-enabledevicecontrol-f-sys.md#enableDeviceControl) | Enables device control for a bound device. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BusinessCapability](arkts-connectivity-partneragent-businesscapability-i.md) | Describes the business capabilities of the application. |
| [DeviceCapability](arkts-connectivity-partneragent-devicecapability-i.md) | Describes the capability of a partner device. |
| [PartnerDeviceAddress](arkts-connectivity-partneragent-partnerdeviceaddress-i.md) | Describes the partner device address. |

### Enums

| Name | Description |
| --- | --- |
| [PartnerAgentExtensionAbilityDestroyReason](arkts-connectivity-partneragent-partneragentextensionabilitydestroyreason-e.md) | The enum of reasons for destroying partner agent extension ability. |

