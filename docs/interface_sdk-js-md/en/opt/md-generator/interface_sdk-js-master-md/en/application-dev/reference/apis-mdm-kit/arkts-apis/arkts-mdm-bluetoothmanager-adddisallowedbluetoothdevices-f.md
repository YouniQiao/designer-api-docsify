# addDisallowedBluetoothDevices

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
```

## addDisallowedBluetoothDevices

```TypeScript
function addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void
```

Adds Bluetooth devices to the blocklist. The current device cannot connect to the disallowed Bluetooth devices.Since API version 22, the MAC addresses in the array must comply with the Bluetooth MAC address specifications (for example, 00:1A:2B:3C:4D:5E). Invalid MAC addresses will be removed and only valid MAC addresses will be added.

A policy conflict is reported when this API is called in the following scenarios:

1. Bluetooth has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy).In this case, you can call [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy)enable Bluetooth to solve the conflict.2. Allowed Bluetooth devices have been added by calling [addAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md#addAllowedBluetoothDevices).You can resolve the conflict by removing allowed Bluetooth devices through [removeAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md#removeAllowedBluetoothDevices).

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void--><!--Device-bluetoothManager-function addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| deviceIds | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

// Create an EnterpriseAdminExtensionAbility component.
let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Define the array of Bluetooth device MAC addresses. (Replace it as required.)
let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"];
try {
  // Add Bluetooth devices to the blocklist.
  bluetoothManager.addDisallowedBluetoothDevices(wantTemp,deviceIds);
  console.info(`Succeeded in adding disallowed bluetooth devices.`);
} catch(err) {
  console.error(`Failed to add disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
}
```
