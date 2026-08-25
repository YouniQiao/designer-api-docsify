# addDockApp

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addDockApp

```TypeScript
function addDockApp(admin: Want, bundleName: string, abilityName: string, index?: number): void
```

Adds an application to the bottom shortcut bar of a PC/2-in-1 device based on the location index. Then users can tap the application icon in the shortcut bar to directly launch the application. The application icon is the default icon displayed on the home screen.

> **NOTE：**&gt;
> 1. If location 0 or 1 is already occupied by the application center or task center, adding an application to that
> location returns error code 9201019. If that location is occupied by another app, the addition succeeds.&gt;
> 2. The following applications cannot be added to the shortcut bar using this API: Application Center, Task
> Center, Files, and Recycle Bin.&gt;
> 3. Only applications with an entry (that is, an icon) can be added.&gt;
> 4. Only the shortcut bar of the current user can be configured. Each user's shortcut bar can contain a maximum of
> 100 applications.&gt;
> 5. When a new application is inserted into an occupied location, the new application will directly take that
> location, and the original application along with all subsequent applications will shift back by one location.&gt;
> 6. If the **index** parameter is not passed or the passed value is greater than the number of applications in the
> shortcut bar, the new application is added to the end of the shortcut bar by default.&gt;
> 7. After an application is added to the shortcut bar using this API, users can manually remove the application or
> adjust its position.

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
| index | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9200015](../errorcode-enterpriseDeviceManager.md#9200015-component-not-exist) |
| [9201013](../errorcode-enterpriseDeviceManager.md#9201013-number-of-applications-in-dock-reaches-maximum) |
| [9201014](../errorcode-enterpriseDeviceManager.md#9201014-specified-application-already-in-docker) |
| [9201015](../errorcode-enterpriseDeviceManager.md#9201015-specified-application-not-installed) |
| [9201018](../errorcode-enterpriseDeviceManager.md#9201018-specified-application-inoperable) |
| [9201019](../errorcode-enterpriseDeviceManager.md#9201019-specified-location-inoperable) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
