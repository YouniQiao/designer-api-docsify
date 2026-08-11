# addDisallowedUsbDevices

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## addDisallowedUsbDevices

```TypeScript
function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void
```

Adds disallowed USB device types.

Use cases:

- Disable specific types of USB devices in enterprise security management scenarios.  
- Prevent data leaks by disabling USB storage device types.  
- Enable device administrators to prohibit the use of certain USB device types based on security policies.  
- Work with the [removeDisallowedUsbDevices](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md#removedisallowedusbdevices) API to implement dynamic  
management of USB device types.

> **NOTE：**
> 
> The [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md#adddisallowedpermissiveusbdevices) API is recommended.
> A policy conflict is reported when this API is called in the following scenarios:

1. The USB capability of the device has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy).2. The available USB devices have been added through [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md#addallowedusbdevices).3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount).4. Disallowed USB device types have been added via [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md#adddisallowedpermissiveusbdevices).

**Since:** 14

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void--><!--Device-usbManager-function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| usbDevices | Array&lt;UsbDeviceType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = [{
    baseClass: 8,
    subClass: 0,
    protocol: 0,
    descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.addDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in adding disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to add disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```
