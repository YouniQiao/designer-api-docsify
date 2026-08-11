# getDisallowedBluetoothProtocols

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.MDMKit';
```

## getDisallowedBluetoothProtocols

```TypeScript
function getDisallowedBluetoothProtocols(admin: Want, accountId: number): Array<Protocol>
```

Obtains the disallowed Bluetooth protocols of a specified user.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function getDisallowedBluetoothProtocols(admin: Want, accountId: number): Array<Protocol>--><!--Device-bluetoothManager-function getDisallowedBluetoothProtocols(admin: Want, accountId: number): Array<Protocol>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;Protocol&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

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
try {
  // Obtains the Bluetooth protocol blocklist of a specified user.
  let result: Array<bluetoothManager.Protocol> = bluetoothManager.getDisallowedBluetoothProtocols(wantTemp, accountId);
  console.info(`Succeeded in getting disallowed bluetooth protocols. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}`);
}
```


## getDisallowedBluetoothProtocols

```TypeScript
function getDisallowedBluetoothProtocols(admin: Want | null, accountId: number, policy: TransferPolicy): Array<Protocol>
```

Obtains the list of disallowed Bluetooth protocols for a specified user under a specified transfer policy.

> **NOTE：**
> 
> 1. This API and
> [getDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md#getdisallowedbluetoothprotocols) are
> overloaded APIs. This API adds the **policy** parameter to query the disallowing configuration based on the
> transfer policy.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function getDisallowedBluetoothProtocols(admin: Want | null, accountId: number, policy: TransferPolicy): Array<Protocol>--><!--Device-bluetoothManager-function getDisallowedBluetoothProtocols(admin: Want | null, accountId: number, policy: TransferPolicy): Array<Protocol>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |
| accountId | number | Yes |
| policy | [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;Protocol&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

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

try {
  // Obtain the list of disallowed Bluetooth protocols for a specified user under a specified transfer policy.
  let result: Array<bluetoothManager.Protocol> = bluetoothManager.getDisallowedBluetoothProtocols(wantTemp, accountId, bluetoothManager.TransferPolicy.RECEIVE_SEND);
  console.info(`Succeeded in getting disallowed bluetooth protocols, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed bluetooth protocols. Code is ${err.code}, message is ${err.message}`);
}
```
