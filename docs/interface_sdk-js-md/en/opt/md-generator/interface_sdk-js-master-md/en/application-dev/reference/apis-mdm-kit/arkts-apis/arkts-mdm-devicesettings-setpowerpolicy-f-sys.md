# setPowerPolicy (System API)

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setPowerPolicy

```TypeScript
function setPowerPolicy(admin: Want, powerScene: PowerScene, powerPolicy: PowerPolicy): void
```

Sets the power policy.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [setValue](arkts-mdm-devicesettings-setvalue-f.md#setValue)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setPowerPolicy(admin: Want, powerScene: PowerScene, powerPolicy: PowerPolicy): void--><!--Device-deviceSettings-function setPowerPolicy(admin: Want, powerScene: PowerScene, powerPolicy: PowerPolicy): void-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let delayTime = 0;
  let powerScene: deviceSettings.PowerScene = deviceSettings.PowerScene.TIME_OUT;
  let powerPolicyAction: deviceSettings.PowerPolicyAction = deviceSettings.PowerPolicyAction.AUTO_SUSPEND;
  let powerPolicy: deviceSettings.PowerPolicy = {powerPolicyAction, delayTime};
  deviceSettings.setPowerPolicy(wantTemp, powerScene, powerPolicy);
  console.info(`Succeeded in setting power policy`);
} catch (err) {
  console.error(`Failed to set power policy. Code: ${err.code}, message: ${err.message}`);
}
```
