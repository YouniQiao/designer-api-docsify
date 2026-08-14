# getOutgoingCallPolicyNumbers

## Modules to Import

```TypeScript
import { telephonyManager } from 'telephonyManager';
```

## getOutgoingCallPolicyNumbers

```TypeScript
function getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>
```

Obtains the trustlist or blocklist for outgoing calls.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>--><!--Device-telephonyManager-function getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| policy | adminManager.Policy | Yes | Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist, and **TRUST_LIST** indicates a trustlist. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | An array of numbers in the outgoing call blocklist or trustlist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = telephonyManager.getOutgoingCallPolicyNumbers(wantTemp, policy);
  console.info(`Succeeded in getting outgoing call policy. result: ${JSON.stringify(numbers)}`);
} catch (err) {
  console.error(`Failed to get outgoing call policy. Code: ${err.code}, message: ${err.message}`);
}
```


## getOutgoingCallPolicyNumbers

```TypeScript
function getOutgoingCallPolicyNumbers(admin: Want | null, policy: adminManager.Policy): Array<string>
```

Obtains the trustlist or blocklist for outgoing calls.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function getOutgoingCallPolicyNumbers(admin: Want | null, policy: adminManager.Policy): Array<string>--><!--Device-telephonyManager-function getOutgoingCallPolicyNumbers(admin: Want | null, policy: adminManager.Policy): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the. EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies that actually take effect on the device are returned. |
| policy | adminManager.Policy | Yes | Policy for trustlist or blocklist. **BLOCK_LIST** indicates a blocklist, and **TRUST_LIST** indicates a trustlist. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | An array of numbers in the outgoing call blocklist or trustlist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

