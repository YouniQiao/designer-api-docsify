# getWatermarkImageApps

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getWatermarkImageApps

```TypeScript
function getWatermarkImageApps(admin: Want, accountId: number): Array<string>
```

Obtains the list of application bundle names for which watermarks have been set for a specified user.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getWatermarkImageApps(admin: Want, accountId: number): Array<string>--><!--Device-securityManager-function getWatermarkImageApps(admin: Want, accountId: number): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let accountId: number = 100;
try {
  let result: Array<string> = securityManager.getWatermarkImageApps(wantTemp, accountId);
  console.info(`Succeeded in getting watermark image apps, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get watermark image apps. Code: ${err.code}, message: ${err.message}`);
}
```
