# addDisallowedBluetoothProtocols

## Modules to Import

```TypeScript
```

## addDisallowedBluetoothProtocols

```TypeScript
function addDisallowedBluetoothProtocols(admin: Want, accountId: number,  protocols: Array<Protocol>): void
```

Adds disallowed Bluetooth protocols. Specified users cannot use the disallowed Bluetooth protocols to send files to other devices. This API is used to disable the GATT or SPP protocol, which does not take effect for system services and system applications. When the SPP protocol is passed, both the receiving and sending functions are disabled.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function addDisallowedBluetoothProtocols(admin: Want, accountId: number,  protocols: Array<Protocol>): void--><!--Device-bluetoothManager-function addDisallowedBluetoothProtocols(admin: Want, accountId: number,  protocols: Array<Protocol>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | Yes |
| [protocols](../../apis-network-kit/arkts-apis/arkts-network-socket-tlssecureoptions-i.md) | Array & lt;Protocol & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

// Create an EnterpriseAdminExtensionAbility component.
let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Define the user ID. (Replace it as required.)
let accountId: number = 100;
// Define the array of Bluetooth protocols. (Replace it as required.)
let protocols: Array<bluetoothManager.Protocol> = [bluetoothManager.Protocol.GATT, bluetoothManager.Protocol.SPP];
try {
  // Add Bluetooth protocols to the blocklist.
  bluetoothManager.addDisallowedBluetoothProtocols(wantTemp, accountId, protocols);
  console.info('Succeeded in adding disallowed bluetooth protocols policy.');
} catch (err) {
  console.error(`Failed to add disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}`);
}
```


## addDisallowedBluetoothProtocols

```TypeScript
function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void
```

Adds disallowed Bluetooth protocols. After the setting, specified users cannot use the disallowed Bluetooth protocols based on the specified transfer policy. > **NOTE：**> > 1. This API is used to disable the GATT or SPP protocol, which does not take effect for system services and > system applications. > > 2. When the SPP protocol is passed, the value of the **policy** parameter can only be > **TransferPolicy.RECEIVE_SEND**. Otherwise, error code 9200012 will be returned. > > 3. This API and > [addDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](#adddisallowedbluetoothprotocols) are > overloaded APIs. This API adds the **policy** parameter to specify the transfer policy, enabling more fine- > grained control over Bluetooth protocol disabling behavior (for example, blocking only sending, only receiving, > or both sending and receiving). If both APIs are used to configure disabling policies, the policies will be > combined and take effect.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void--><!--Device-bluetoothManager-function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | Yes |
| [protocols](../../apis-network-kit/arkts-apis/arkts-network-socket-tlssecureoptions-i.md) | Array & lt;Protocol & gt; | Yes |
| policy | [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

// Create an EnterpriseAdminExtensionAbility component.
let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Define the user ID.
let accountId: number = 100;
// Define the Bluetooth protocol array.
let protocols: Array<bluetoothManager.Protocol> = [
  bluetoothManager.Protocol.GATT,
  bluetoothManager.Protocol.SPP,
  bluetoothManager.Protocol.OPP
];

try {
  // Add Bluetooth protocols to the blocklist and specify the transfer policy as disabling sending and receiving.
  bluetoothManager.addDisallowedBluetoothProtocols(wantTemp, accountId, protocols, bluetoothManager.TransferPolicy.RECEIVE_SEND);
  console.info('Succeeded in adding disallowed bluetooth protocols.');
} catch (err) {
  console.error(`Failed to add disallowed bluetooth protocols. Code is ${err.code}, message is ${err.message}`);
}
```
