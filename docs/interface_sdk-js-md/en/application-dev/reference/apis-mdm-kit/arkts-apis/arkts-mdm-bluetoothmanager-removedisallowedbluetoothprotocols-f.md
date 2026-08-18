# removeDisallowedBluetoothProtocols

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
```

## removeDisallowedBluetoothProtocols

```TypeScript
function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void
```

Removes disallowed Bluetooth protocols. After removing some protocols, the user is still restricted by the remaining disallowed protocols; after removing all protocols, the user can use any protocol; removing non-existent protocols results in a successful API call but no actual change.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void--><!--Device-bluetoothManager-function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. <br> You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) of @ ohos.account.osAccount to obtain the ID. |
| protocols | Array&lt;Protocol&gt; | Yes | Bluetooth protocol array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

**Examples**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let accountId: number = 100;
let protocols: Array<bluetoothManager.Protocol> = [bluetoothManager.Protocol.GATT, bluetoothManager.Protocol.SPP];
try{
    bluetoothManager.removeDisallowedBluetoothProtocols(wantTemp, accountId, protocols);
    console.info('Succeeded in removing disallowed bluetooth protocols policy.');
} catch (err) {
    console.error(`Failed to remove disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}`);
}
```


## removeDisallowedBluetoothProtocols

```TypeScript
function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void
```

Removes Bluetooth protocols from the blocklist. After the setting, specified users are no longer restricted by the transfer policy and can properly use these Bluetooth protocols. > **NOTE：**> > 1. When the SPP protocol is passed, the value of the **policy** parameter can only be > **TransferPolicy.RECEIVE_SEND**. Otherwise, error code 9200012 will be returned. > > 2. This API and > [removeDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](#removedisallowedbluetoothprotocols) are > overloaded APIs. This API adds the **policy** parameter to remove the disallowing configuration based on the > transfer policy. If the same protocol has been blocked under different policies via the two APIs, calling this > API removes only the blocking configuration for the corresponding policy, while blocking configurations of other > policies remain effective.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void--><!--Device-bluetoothManager-function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. <br> You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) of @ ohos.account.osAccount to obtain the ID. |
| protocols | Array&lt;Protocol&gt; | Yes | Array of Bluetooth protocols to be removed from the blocklist. |
| policy | [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) | Yes | Transfer policy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

