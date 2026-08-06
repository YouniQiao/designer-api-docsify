# bindDevice

## bindDevice

```TypeScript
function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability,
    businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>
```

Bind the partner device.After successfully binding the device, if the device meets the discovery requirements,the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ of the application will be launched.  
- If the \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ in the capability variable is set to true,  
the application's ability will be launched when the device is connected via Bluetooth.  
- If the \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ in the capability variable is set to true,  
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
| deviceAddress | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The address of partner device. |
| deviceCapability | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The capability of partner device. |
| businessCapability | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The business capability of application. |
| partnerAgentExtensionAbilityName | string | Yes | The name of PartnerAgentExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [34900003](../errorcode-fusionConnectivity.md#34900003-device-not-paired) | The device is not paired. |
| [34900004](../errorcode-fusionConnectivity.md#34900004-device-address-registered) | The device has already been bound to the PartnerAgentExtensionAbility. |
| [34900005](../errorcode-fusionConnectivity.md#34900005-bluetooth-disabled) | Bluetooth disabled. |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) | Internal error. |

