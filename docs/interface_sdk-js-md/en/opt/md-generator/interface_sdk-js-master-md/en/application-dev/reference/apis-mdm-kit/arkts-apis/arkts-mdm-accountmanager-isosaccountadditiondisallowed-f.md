# isOsAccountAdditionDisallowed

## Modules to Import

```TypeScript
import { accountManager } from '@kit.MDMKit';
```

## isOsAccountAdditionDisallowed

```TypeScript
function isOsAccountAdditionDisallowed(admin: Want, accountId?: number): boolean
```

Queries whether a user is not allowed to add an account.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function isOsAccountAdditionDisallowed(admin: Want, accountId?: number): boolean--><!--Device-accountManager-function isOsAccountAdditionDisallowed(admin: Want, accountId?: number): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |


## isOsAccountAdditionDisallowed

```TypeScript
function isOsAccountAdditionDisallowed(admin: Want | null, accountId?: number): boolean
```

Queries whether a user is not allowed to add an account. This API is applicable to enterprise audit and compliance check scenarios, helping administrators confirm the execution of account policies.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function isOsAccountAdditionDisallowed(admin: Want | null, accountId?: number): boolean--><!--Device-accountManager-function isOsAccountAdditionDisallowed(admin: Want | null, accountId?: number): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |
| accountId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

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
  let isDisallowed: boolean = accountManager.isOsAccountAdditionDisallowed(wantTemp, 100);
  console.info(`Succeeded in querying the os account addition or not: ${isDisallowed}`);
} catch (err) {
  console.error(`Failed to query the os account addition or not. Code: ${err.code}, message: ${err.message}`);
}
```
