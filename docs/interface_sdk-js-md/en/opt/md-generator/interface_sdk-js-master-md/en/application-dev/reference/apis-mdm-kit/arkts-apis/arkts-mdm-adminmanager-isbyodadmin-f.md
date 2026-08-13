# isByodAdmin

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## isByodAdmin

```TypeScript
function isByodAdmin(admin: Want): boolean
```

Checks whether the current application is activated as a BYOD device administrator application based on the **EnterpriseAdminExtensionAbility** component.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.START_PROVISIONING_MESSAGE

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function isByodAdmin(admin: Want): boolean--><!--Device-adminManager-function isByodAdmin(admin: Want): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: boolean = adminManager.isByodAdmin(wantTemp);
  console.info(`Succeeded in querying admin is byod admin or not : ${result}`);
} catch (error) {
  console.error(`Failed to query admin is byod admin or not. Code is ${error.code}, message is ${error.message}`);
}
```
