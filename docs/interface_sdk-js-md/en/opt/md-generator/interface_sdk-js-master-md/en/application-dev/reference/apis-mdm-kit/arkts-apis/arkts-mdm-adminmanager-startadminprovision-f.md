# startAdminProvision

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## startAdminProvision

```TypeScript
function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void
```

Enables the device administrator application to open a page for the BYOD administrator to perform activation.

**Since:** 15

**Required permissions:** ohos.permission.START_PROVISIONING_MESSAGE

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void--><!--Device-adminManager-function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| type | [AdminType](arkts-mdm-adminmanager-admintype-e.md) | Yes |
| context | common.Context | Yes |
| parameters | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let recordParameters: Record<string, string> = {
  // Replace with actual values.
  "activateId": "activateId testValue",
  "customizedInfo": "customizedInfo testValue"
};
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  console.info('context:' + JSON.stringify(context));
  adminManager.startAdminProvision(wantTemp, adminManager.AdminType.ADMIN_TYPE_BYOD, context, recordParameters);
  console.info('startAdminProvision::success');
} catch (error) {
  console.error('startAdminProvision::errorCode: ' + error.code + ' errorMessage: ' + error.message);
}
```
