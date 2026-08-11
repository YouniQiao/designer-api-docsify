# setManagedBrowserPolicy

## Modules to Import

```TypeScript
import { browser } from 'kits/@kit.MDMKit';
```

## setManagedBrowserPolicy

```TypeScript
function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void
```

Sets a browser policy for a specified browser. This API is applicable to scenarios where an enterprise needs to manage employees' browser behavior in a unified manner, such as configuring browser security policies. After the setting is successful, the system common event  
[COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_managed_browser_policy_changed)is released.

> **NOTE：**
> 
> In multi-MDM application scenarios, once a policy for a specific browser is configured and takes effect by the
> first admin, it can no longer be configured by other admins.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Required permissions:** ohos.permission.ENTERPRISE_SET_BROWSER_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-browser-function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void--><!--Device-browser-function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Application bundle name, which is used to specify the browser. It uniquely identifies an application. |
| policyName | string | Yes | Browser policy name, which is agreed upon by the API caller and the specified browser. |
| policyValue | string | Yes | Browser policy value. If the value is an empty string, the policy corresponding to the policy name is removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.testbrowser';
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setManagedBrowserPolicy(wantTemp, bundleName, policyName, policyValue);
  console.info('Succeeded in setting managed browser policy.');
} catch (err) {
  console.error(`Failed to set managed browser policy. Code is ${err.code}, message is ${err.message}`);
}
```

