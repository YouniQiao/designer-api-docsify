# disableDeviceAdmin

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## disableDeviceAdmin

```TypeScript
function disableDeviceAdmin(admin: Want): Promise<void>
```

Disables a [DA](../../../mdm/mdm-kit-term.md#device-admin-da) application by a [SDA](../../../mdm/mdm-kit-term.md#super-device-admin-sda) application. This API uses a promise to return the result. After this API is called successfully, the specified device administrator application is disabled and no longer has the device management capability. This API can be called only by super device administrator applications.

**Since:** 23

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200005](../errorcode-enterpriseDeviceManager.md#9200005-failed-to-disable-the-device-administrator-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
