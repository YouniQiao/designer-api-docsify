# setLocationPolicy

## Modules to Import

```TypeScript
import { locationManager } from 'kits/@kit.MDMKit';
```

## setLocationPolicy

```TypeScript
function setLocationPolicy(admin: Want, policy: LocationPolicy): void
```

Sets a location service policy. This API can be used in enterprise management and control scenarios. For example, you can disable the location service in confidential areas to protect information security, or forcibly enable the location service in logistics and distribution applications to track device locations.

> **NOTE：**&gt;
> - Disabled: Set this option when privacy protection or power saving is required.&gt;
> - Forced on: Set this option in scenarios such as device security tracking and asset management.&gt;
> - Default: This option removes policy restrictions and allows the user to control the setting independently.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_LOCATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| policy | [LocationPolicy](arkts-mdm-locationmanager-locationpolicy-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
