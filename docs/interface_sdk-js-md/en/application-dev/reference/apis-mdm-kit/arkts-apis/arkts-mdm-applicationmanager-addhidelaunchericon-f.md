# addHideLauncherIcon

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addHideLauncherIcon

```TypeScript
function addHideLauncherIcon(admin: Want, bundleNames: Array<string>): void
```

Adds applications to the home screen icon hide list.

> **NOTE：**&gt;
> 1. This API can only hide home screen icons for applications of the current user. Hiding application widgets are
> not supported.&gt;
> 2. If a hidden application has clones, the clones are hidden synchronously.&gt;
> 3. Not all applications on the home screen can be added to the hidden list. Otherwise, all applications will
> still be displayed on the home screen.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleNames | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
