# getAllowedNotificationBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## getAllowedNotificationBundles

```TypeScript
function getAllowedNotificationBundles(admin: Want | null, accountId: number): Array<string>
```

Obtains the list of applications that are allowed to send notifications.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getAllowedNotificationBundles(admin: Want | null, accountId: number): Array<string>--><!--Device-applicationManager-function getAllowedNotificationBundles(admin: Want | null, accountId: number): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |
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
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getAllowedNotificationBundles(wantTemp, 100);
  console.info(`Succeeded in getting allowed notification bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed notification bundles. Code is ${err.code}, message is ${err.message}`);
}
```
