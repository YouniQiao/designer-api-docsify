# removeDockApp

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## removeDockApp

```TypeScript
function removeDockApp(admin: Want, bundleName: string, abilityName: string): void
```

Removes an application from the shortcut bar.

> **NOTE：**&gt;
> The following applications cannot be removed from the shortcut bar using this API: Application Center, Task
> Center, Files, and Recycle Bin. Otherwise, error code 9201018 will be reported.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Dyn, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |
| abilityName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9201016](../errorcode-enterpriseDeviceManager.md#9201016-specified-application-not-in-dock) |
| [9201018](../errorcode-enterpriseDeviceManager.md#9201018-specified-application-inoperable) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
