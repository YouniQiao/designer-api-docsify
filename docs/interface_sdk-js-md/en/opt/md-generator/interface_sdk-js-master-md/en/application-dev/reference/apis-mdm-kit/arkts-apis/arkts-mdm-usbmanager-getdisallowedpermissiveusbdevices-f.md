# getDisallowedPermissiveUsbDevices

## Modules to Import

```TypeScript
import { usbManager } from '@kit.MDMKit';
```

## getDisallowedPermissiveUsbDevices

```TypeScript
function getDisallowedPermissiveUsbDevices(admin: Want | null): Array<PermissiveUsbDeviceType>
```

Obtains the USB device types that have been disallowed via [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md#addDisallowedPermissiveUsbDevices).

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function getDisallowedPermissiveUsbDevices(admin: Want | null): Array<PermissiveUsbDeviceType>--><!--Device-usbManager-function getDisallowedPermissiveUsbDevices(admin: Want | null): Array<PermissiveUsbDeviceType>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[PermissiveUsbDeviceType](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
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
  let result: Array<usbManager.PermissiveUsbDeviceType> = usbManager.getDisallowedPermissiveUsbDevices(wantTemp);
  console.info(`Succeeded in getting disallowed permissive USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed permissive USB devices. Code: ${err.code}, message: ${err.message}`);
}
```
