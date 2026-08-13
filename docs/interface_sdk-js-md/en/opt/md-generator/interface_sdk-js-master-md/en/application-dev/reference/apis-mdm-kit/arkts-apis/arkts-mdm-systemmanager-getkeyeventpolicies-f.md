# getKeyEventPolicies

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## getKeyEventPolicies

```TypeScript
function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>
```

Obtains the key event handling policy.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>--><!--Device-systemManager-function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[KeyEventPolicy](arkts-mdm-systemmanager-keyeventpolicy-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |


## getKeyEventPolicies

```TypeScript
function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>
```

Obtains the key event handling policy. This API is applicable to scenarios where you need to query the current key event handling policy configuration. It helps enterprise administrators verify whether the policy has been correctly applied or obtain the current configuration before making policy adjustments.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>--><!--Device-systemManager-function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[KeyEventPolicy](arkts-mdm-systemmanager-keyeventpolicy-i.md)&gt; |

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
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let result: Array<systemManager.KeyEventPolicy> = [];
try {
  result = systemManager.getKeyEventPolicies(wantTemp);
  console.info('Succeeded in getting key event policies.');
} catch (err) {
  console.error(`Failed to get key event policies. Code is ${err.code}, message is ${err.message}`);
}
```
