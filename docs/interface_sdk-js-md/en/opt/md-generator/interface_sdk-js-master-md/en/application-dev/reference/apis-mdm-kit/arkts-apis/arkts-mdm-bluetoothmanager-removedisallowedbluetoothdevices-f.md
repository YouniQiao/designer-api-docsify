# removeDisallowedBluetoothDevices

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
```

## removeDisallowedBluetoothDevices

```TypeScript
function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void
```

Removes disallowed Bluetooth devices. If some Bluetooth devices are removed from the disallowed list, the current device cannot connect to the remaining ones; if all Bluetooth devices are removed, the current device can connect to any Bluetooth device.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void--><!--Device-bluetoothManager-function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| deviceIds | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

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
  // Remove Bluetooth devices from the blocklist.
  bluetoothManager.removeDisallowedBluetoothDevices(wantTemp,deviceIds);
  console.info(`Succeeded in removing disallowed bluetooth devices.`);
} catch(err) {
  console.error(`Failed to remove disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
}
```
