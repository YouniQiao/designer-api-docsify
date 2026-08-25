# removeDisallowedRunningBundlesSync

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## removeDisallowedRunningBundlesSync

```TypeScript
function removeDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void
```

Removes applications from the application running blocklist of the current or specified user. After an application is removed, it is allowed to run under the current or specified user.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appIds | Array & lt;string & gt; | Yes |
| accountId | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
