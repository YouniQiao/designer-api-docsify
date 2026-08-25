# addDisallowedPermissiveUsbDevices

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## addDisallowedPermissiveUsbDevices

```TypeScript
function addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void
```

Adds disallowed USB device types. Unlike the [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) API, this API does not require matching based on the [defined-class-codes](https://www.usb.org/defined-class-codes) standard. This API takes effect immediately on connected USB devices without requiring re-plugging. For example, if a USB wired headset is in normal use and this API is called to disable it, the headset will become unavailable immediately.A policy conflict is reported when this API is called in the following scenarios:
1. Disallowed USB device types have been added using the [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) API.
2. The USB capability of the device has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md).
3. The available USB devices have been added through [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md).
4. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md).

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| usbDevices | Array&lt;[PermissiveUsbDeviceType](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
