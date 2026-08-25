# setPowerPolicy (System API)

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## setPowerPolicy

```TypeScript
function setPowerPolicy(admin: Want, powerScene: PowerScene, powerPolicy: PowerPolicy): void
```

Sets the power policy.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [setValue](arkts-mdm-devicesettings-setvalue-f.md)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| powerScene | [PowerScene](arkts-mdm-devicesettings-powerscene-e-sys.md) | Yes |
| powerPolicy | [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
