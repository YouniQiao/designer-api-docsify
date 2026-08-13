# setSimEnabled

## Modules to Import

```TypeScript
import { telephonyManager } from '@kit.MDMKit';
```

## setSimEnabled

```TypeScript
function setSimEnabled(admin: Want, slotId: number): void
```

Enables the SIM card in a specified slot. After it has been disabled with **setSimDisabled**, the card must be turned back on manually in **Settings** > **Mobile network** > **SIM management**, as this **setSimEnabled** API cannot re-enable it directly.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function setSimEnabled(admin: Want, slotId: number): void--><!--Device-telephonyManager-function setSimEnabled(admin: Want, slotId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| slotId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace the values as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // Set the ID of the slot to be enabled.
  let slotId: number = 0;
  // Enable the SIM card in the specified slot.
  telephonyManager.setSimEnabled(wantTemp, slotId);
  console.info(`Succeeded in setting slotId: ${slotId} enabled.`);
} catch (err) {
  console.error(`Failed to set slotId enabled. Code: ${err.code}, message: ${err.message}`);
}
```
