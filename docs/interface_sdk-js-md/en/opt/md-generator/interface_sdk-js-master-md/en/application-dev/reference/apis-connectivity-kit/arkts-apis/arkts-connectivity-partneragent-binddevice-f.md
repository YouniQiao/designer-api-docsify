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

Bind the partner device. After successfully binding the device, if the device meets the discovery requirements, the [PartnerAgentExtensionAbility](arkts-connectivity-fusionconnectivity-partneragentextensionability-partneragentextensionability-c.md#PartnerAgentExtensionAbility) of the application will be launched. - If the [supportBR](arkts-connectivity-partneragent-devicecapability-i.md#supportBR) in the capability variable is set to true, the application's ability will be launched when the device is connected via Bluetooth. - If the [supportBleAdvertiser](arkts-connectivity-partneragent-devicecapability-i.md#supportBleAdvertiser) in the capability variable is set to true, the application's ability will be launched when the device is detected via Bluetooth scanning. Note: The device must be paired first.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>--><!--Device-partnerAgent-function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | Yes |
| deviceCapability | [DeviceCapability](arkts-connectivity-partneragent-devicecapability-i.md) | Yes |
| businessCapability | [BusinessCapability](arkts-connectivity-partneragent-businesscapability-i.md) | Yes |
| partnerAgentExtensionAbilityName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [34900004](../errorcode-fusionConnectivity.md#34900004-device-address-registered) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34900005](../errorcode-fusionConnectivity.md#34900005-bluetooth-disabled) |
| [34900003](../errorcode-fusionConnectivity.md#34900003-device-not-paired) |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
