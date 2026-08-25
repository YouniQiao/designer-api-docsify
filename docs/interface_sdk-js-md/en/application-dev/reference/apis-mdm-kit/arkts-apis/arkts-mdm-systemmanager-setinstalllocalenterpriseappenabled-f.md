# setInstallLocalEnterpriseAppEnabled

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setInstallLocalEnterpriseAppEnabled

```TypeScript
function setInstallLocalEnterpriseAppEnabled(admin: Want, isEnable: boolean): void
```

Sets whether local installation of enterprise applications is supported. When local installation is enabled, users can install enterprise applications (signing certificate distribution type: **enterprise_normal**) by number- tapping their installation packages on enterprise PCs/2-in-1 devices with the local installation capability.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| isEnable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
