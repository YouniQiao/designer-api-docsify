# removeDisallowedBluetoothDevices

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.MDMKit';
```

## removeDisallowedBluetoothDevices

```TypeScript
function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void
```

Removes disallowed Bluetooth devices. If some Bluetooth devices are removed from the disallowed list, the current device cannot connect to the remaining ones; if all Bluetooth devices are removed, the current device can connect to any Bluetooth device.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| deviceIds | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
