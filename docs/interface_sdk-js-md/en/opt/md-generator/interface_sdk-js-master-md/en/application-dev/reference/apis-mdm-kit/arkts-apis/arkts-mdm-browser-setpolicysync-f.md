# setPolicySync

## Modules to Import

```TypeScript
import { browser } from '@kit.MDMKit';
```

## setPolicySync

```TypeScript
function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void
```

Sets a browser sub-policy for a specified browser. This API is applicable to scenarios where an enterprise needs to manage employees' browser behavior in a unified manner.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_SET_BROWSER_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-browser-function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void--><!--Device-browser-function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appId | string | Yes |
| policyName | string | Yes |
| policyValue | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace the value of appId with the specified application ID of the browser.
let appId: string = 'com.example.******_******/******5t5CoBM=';
// Browser policy name.
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
// Browser policy value.
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setPolicySync(wantTemp, appId, policyName, policyValue);
  console.info('Succeeded in setting browser policies.');
} catch (err) {
  console.error(`Failed to set browser policies. Code is ${err.code}, message is ${err.message}`);
}
```
