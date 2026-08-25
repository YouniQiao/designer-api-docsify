# setOtaUpdatePolicy

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setOtaUpdatePolicy

```TypeScript
function setOtaUpdatePolicy(admin: Want, policy: OtaUpdatePolicy): void
```

Sets the update policy. After the setting is successful, the system performs OTA updates based on the specified policy type. Different policy types correspond to different update behaviors. In intranet updates, call [systemManager.notifyUpdatePackages](arkts-mdm-systemmanager-notifyupdatepackages-f.md) to notify the system of the update packages and then call this API to set the upgrade policy.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| policy | [OtaUpdatePolicy](arkts-mdm-systemmanager-otaupdatepolicy-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
