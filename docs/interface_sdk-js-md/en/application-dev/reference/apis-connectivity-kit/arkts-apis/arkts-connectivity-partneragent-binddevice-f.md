# bindDevice

## Modules to Import

```TypeScript
import { partnerAgent } from '@kit.ConnectivityKit';
```

## bindDevice

```TypeScript
function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,
    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>
```

Bind the partner device.After successfully binding the device, if the device meets the discovery requirements,the [PartnerAgentExtensionAbility](arkts-connectivity-fusionconnectivity-partneragentextensionability-partneragentextensionability-c.md#PartnerAgentExtensionAbility) of the application will be launched.  
- If the [supportBR](arkts-connectivity-partneragent-devicecapability-i.md#supportBR) in the capability variable is set to true,  
 the application's ability will be launched when the device is connected via Bluetooth.  
- If the [supportBleAdvertiser](arkts-connectivity-partneragent-devicecapability-i.md#supportBleAdvertiser) in the capability variable is set to true,  
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
| deviceAddress | PartnerDeviceAddress | Yes | The address of partner device. |
| deviceCapability | DeviceCapability | Yes | The capability of partner device. |
| businessCapability | [BusinessCapability](arkts-connectivity-partneragent-businesscapability-i.md) | Yes | The business capability of application. |
| partnerAgentExtensionAbilityName | string | Yes | The name of PartnerAgentExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [34900004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900004-device-address-registered) | The device has already been bound to the PartnerAgentExtensionAbility. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [34900005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900005-bluetooth-disabled) | Bluetooth disabled. |
| [34900003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900003-device-not-paired) | The device is not paired. |
| [34900099](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900099-operation-failed) | Internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

