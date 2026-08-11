# removeIncomingCallPolicyNumbers

## Modules to Import

```TypeScript
import { telephonyManager } from 'kits/@kit.MDMKit';
```

## removeIncomingCallPolicyNumbers

```TypeScript
function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void
```

Removes the trustlist or blocklist for incoming calls. If the list is not set, the removal fails. For example, an enterprise can use this API when lifting incoming call restrictions and restoring employees' normal answering permissions.

A policy conflict is reported when this API is called in the following scenario:

1. If the device's call capability has been disabled via the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy)API, using this API to remove an incoming call trustlist or blocklist will return error code 203. To resolve the conflict, enable the call capability via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy).

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void--><!--Device-telephonyManager-function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| policy | adminManager.Policy | Yes |
| numbers | Array&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace the values as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // Set the policy type to blocklist.
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  // Set the call numbers to be removed from the blocklist.
  let numbers: Array<string> = [
    // Replace the value as required.
    "13112345678"
  ];
  // Remove specified numbers from the incoming call blocklist.
  telephonyManager.removeIncomingCallPolicyNumbers(wantTemp, policy, numbers);
  console.info('Succeeded in removing incoming call policy.');
} catch (err) {
  console.error(`Failed to remove incoming call policy. Code: ${err.code}, message: ${err.message}`);
}
```
