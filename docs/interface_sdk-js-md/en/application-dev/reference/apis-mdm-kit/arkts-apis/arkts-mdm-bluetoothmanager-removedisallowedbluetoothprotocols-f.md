# removeDisallowedBluetoothProtocols

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.MDMKit';
```

## removeDisallowedBluetoothProtocols

```TypeScript
function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void
```

Removes disallowed Bluetooth protocols. After removing some protocols, the user is still restricted by the remaining disallowed protocols; after removing all protocols, the user can use any protocol; removing non-existent protocols results in a successful API call but no actual change.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

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
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |


## removeDisallowedBluetoothProtocols

```TypeScript
function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void
```

Removes Bluetooth protocols from the blocklist. After the setting, specified users are no longer restricted by the transfer policy and can properly use these Bluetooth protocols.

> **NOTE：**&gt;
> 1. When the SPP protocol is passed, the value of the **policy** parameter can only be
> **TransferPolicy.RECEIVE_SEND**. Otherwise, error code 9200012 will be returned.&gt;
> 2. This API and
> [removeDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](#removedisallowedbluetoothprotocols) are
> overloaded APIs. This API adds the **policy** parameter to remove the disallowing configuration based on the
> transfer policy. If the same protocol has been blocked under different policies via the two APIs, calling this
> API removes only the blocking configuration for the corresponding policy, while blocking configurations of other
> policies remain effective.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

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
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
