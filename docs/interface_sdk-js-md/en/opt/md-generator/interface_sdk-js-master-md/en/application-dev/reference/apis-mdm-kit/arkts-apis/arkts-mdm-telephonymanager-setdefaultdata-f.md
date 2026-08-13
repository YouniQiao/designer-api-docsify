# setDefaultData

## Modules to Import

```TypeScript
import { telephonyManager } from '@kit.MDMKit';
```

## setDefaultData

```TypeScript
function setDefaultData(admin: Want, slotId: number): void
```

Sets the SIM card in the specified slot as the default data SIM card. The device will use the data connection from the SIM card in that slot for internet access. For example, in dual-SIM device management scenarios, an enterprise can specify a default data SIM card for employee devices to centrally manage data usage. To successfully call this API, the SIM card must be inserted and airplane mode must be turned off.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function setDefaultData(admin: Want, slotId: number): void--><!--Device-telephonyManager-function setDefaultData(admin: Want, slotId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| slotId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201020](../errorcode-enterpriseDeviceManager.md#9201020-failed-to-set-the-default-mobile-data-sim) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
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
// Set the slot ID of the SIM card to be used as the default data SIM card.
let slotId: number = 0;
try {
  // Sets the specified slot as the default data SIM.
  telephonyManager.setDefaultData(wantTemp, slotId);
  console.info(`success to set default data SIM ID`);
} catch (err) {
  console.error(`Failed to set default data. Code: ${err.code}, message: ${err.message}`);
}
```
