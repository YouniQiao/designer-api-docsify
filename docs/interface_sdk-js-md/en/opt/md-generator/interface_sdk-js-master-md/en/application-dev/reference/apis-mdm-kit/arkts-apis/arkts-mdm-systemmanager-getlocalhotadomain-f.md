# getLocalHotaDomain

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## getLocalHotaDomain

```TypeScript
function getLocalHotaDomain(admin: Want): string
```

Get local HOTA domain for device.

**Since:** 26.1.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getLocalHotaDomain(admin: Want): string--><!--Device-systemManager-function getLocalHotaDomain(admin: Want): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200018](../errorcode-enterpriseDeviceManager.md#9200018-the-device-is-not-an-enterprise-device) |
