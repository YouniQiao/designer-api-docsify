# finishLogCollected

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## finishLogCollected

```TypeScript
function finishLogCollected(admin: Want): void
```

Deletes the device logs collected by the current MDM app under the current user.

> **NOTE：**&gt;
> After the app calls [startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md) to initiate log collection and
> receives the
> [EnterpriseAdminExtensionAbility.onLogCollected](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onlogcollected)
> callback, you are advised to immediately copy or process the logs, and then call this API to delete the collected
> logs.&gt;
> If this API is not called, device logs will occupy the system storage space, which does not affect the next call
> of [startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md) to start a log collection task.

**Since:** 23

**Required permissions:** ohos.permission.ENTERPRISE_READ_LOG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
