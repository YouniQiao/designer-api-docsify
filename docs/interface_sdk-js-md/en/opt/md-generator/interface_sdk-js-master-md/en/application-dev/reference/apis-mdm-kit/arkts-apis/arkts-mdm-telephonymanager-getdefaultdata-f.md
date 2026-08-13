# getDefaultData

## Modules to Import

```TypeScript
import { telephonyManager } from '@kit.MDMKit';
```

## getDefaultData

```TypeScript
function getDefaultData(admin: Want): number
```

Obtains the slot ID of the SIM card currently used as the default data SIM card on the device. For example, an enterprise device administrator can query the current default data SIM during device management for data usage control or data card configuration switching. If no SIM card is inserted or the device is in airplane mode, the API returns the slot ID of the last used data SIM card. If the device has never had a default data SIM set, the API returns **0**, indicating slot 1.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function getDefaultData(admin: Want): number--><!--Device-telephonyManager-function getDefaultData(admin: Want): number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
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

try {
  // Obtain the slot ID of the SIM card currently used as the default data SIM card.
  let slotId: number = telephonyManager.getDefaultData(wantTemp);
  console.info(`success to get default data SIM ID, current is ${slotId}`);
} catch (err) {
  console.error(`Failed to get default data. Code: ${err.code}, message: ${err.message}`);
}
```
