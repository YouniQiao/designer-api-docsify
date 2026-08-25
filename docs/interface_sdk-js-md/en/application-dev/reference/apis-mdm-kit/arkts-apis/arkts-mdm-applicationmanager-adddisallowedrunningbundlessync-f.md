# addDisallowedRunningBundlesSync

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addDisallowedRunningBundlesSync

```TypeScript
function addDisallowedRunningBundlesSync(
    admin: Want,
    appIds: Array<string>,
    accountId?: number
  ): void
```

Adds applications to the application running blocklist. Applications added to the blocklist are not allowed to run under the current or specified user. Since API version 21, if the application running trustlist [addAllowedRunningBundles](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md) is not empty, the application running blocklist cannot be added via this API. Otherwise, the error code 9200010 is reported.

> **NOTE：**&gt;
> If a specified application is running, the system will immediately terminate the application process once it is
> added to the blocklist.

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
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
