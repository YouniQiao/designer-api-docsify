# removeIncomingCallPolicyNumbers

## Modules to Import

```TypeScript
import { telephonyManager } from 'kits/@kit.MDMKit';
```

## removeIncomingCallPolicyNumbers

```TypeScript
function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void
```

Removes the trustlist or blocklist for incoming calls. If the list is not set, the removal fails. For example, an enterprise can use this API when lifting incoming call restrictions and restoring employees' normal answering permissions.A policy conflict is reported when this API is called in the following scenario:
1. If the device's call capability has been disabled via the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)
API, using this API to remove an incoming call trustlist or blocklist will return error code 203. To resolve the conflict, enable the call capability via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md).

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| policy | adminManager.Policy | Yes |
| numbers | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
