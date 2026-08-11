# removeAllowedRunningBundles

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## removeAllowedRunningBundles

```TypeScript
function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void
```

Removes applications from the application running trustlist of the specified user. After an application is removed,it is not allowed to run under the current or specified user.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void--><!--Device-applicationManager-function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appIdentifiers | Array&lt;string&gt; | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIdentifiers: Array<string> = ['0123456789123456789'];

try {
  applicationManager.removeAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in removing allowed running bundles.');
} catch (err) {
  console.error(`Failed to remove allowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```
