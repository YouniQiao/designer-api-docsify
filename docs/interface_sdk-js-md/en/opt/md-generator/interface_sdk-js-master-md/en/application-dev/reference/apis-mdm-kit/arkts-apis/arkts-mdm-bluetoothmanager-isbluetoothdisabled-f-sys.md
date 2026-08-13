# isBluetoothDisabled (System API)

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
```

## isBluetoothDisabled

```TypeScript
function isBluetoothDisabled(admin: Want): boolean
```

Queries whether Bluetooth is disabled.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy)(admin: Want | null, feature: FeatureForDevice)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bluetoothManager-function isBluetoothDisabled(admin: Want): boolean--><!--Device-bluetoothManager-function isBluetoothDisabled(admin: Want): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let isDisabled: boolean = bluetoothManager.isBluetoothDisabled(wantTemp);
  console.info(`Succeeded in querying the bluetooth is disabled or not, isDisabled : ${isDisabled}`);
} catch(err) {
  console.error(`Failed to query the bluetooth is disabled or not. Code: ${err.code}, message: ${err.message}`);
};
```
