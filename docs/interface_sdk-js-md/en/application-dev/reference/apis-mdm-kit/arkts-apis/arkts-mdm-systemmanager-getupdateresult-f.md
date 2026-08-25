# getUpdateResult

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getUpdateResult

```TypeScript
function getUpdateResult(admin: Want, version: string): Promise<UpdateResult>
```

Obtains the system update result. This API uses a promise to return the result. This API is applicable to scenarios where you need to check whether a system update is successful. It helps enterprise administrators understand the device update status and handle update failures in a timely manner to ensure that the device system version meets enterprise requirements.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| version | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UpdateResult](arkts-mdm-systemmanager-updateresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
