# disallowAddOsAccountByUser (System API)

## Modules to Import

```TypeScript
```

## disallowAddOsAccountByUser

```TypeScript
function disallowAddOsAccountByUser(admin: Want, userId: number, disallow: boolean): void
```

Disallows a user to add accounts.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [disallowOsAccountAddition](arkts-mdm-accountmanager-disallowosaccountaddition-f.md#disallowosaccountaddition)

**Required permissions:** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function disallowAddOsAccountByUser(admin: Want, userId: number, disallow: boolean): void--><!--Device-accountManager-function disallowAddOsAccountByUser(admin: Want, userId: number, disallow: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| userId | number | Yes |
| disallow | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { accountManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  accountManager.disallowAddOsAccountByUser(wantTemp, 100, true);
  console.info(`Succeeded in disallowing user add os account`);
} catch (err) {
  console.error(`Failed to disallow user add os account. Code: ${err.code}, message: ${err.message}`);
}
```
