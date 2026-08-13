# hangupCalling

## Modules to Import

```TypeScript
import { telephonyManager } from '@kit.MDMKit';
```

## hangupCalling

```TypeScript
function hangupCalling(admin: Want): void
```

Ends the current call. Only carrier calls are supported, excluding MeeTime calls. For example, an enterprise device administrator can forcibly hang up a non-compliant call that an employee is currently on in enterprise security management scenarios.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function hangupCalling(admin: Want): void--><!--Device-telephonyManager-function hangupCalling(admin: Want): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

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
  // Hang up the current call.
  telephonyManager.hangupCalling(wantTemp);
} catch (err) {
  console.error(`Failed to hang up calling. Code: ${err.code}, message: ${err.message}`);
}
```
