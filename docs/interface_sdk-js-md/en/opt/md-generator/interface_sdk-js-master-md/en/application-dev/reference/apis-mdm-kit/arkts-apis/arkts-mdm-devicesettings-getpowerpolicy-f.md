# getPowerPolicy

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## getPowerPolicy

```TypeScript
function getPowerPolicy(admin: Want, powerScene: PowerScene): PowerPolicy
```

Obtains the power policy.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [deviceSettings.getValue](arkts-mdm-devicesettings-getvalue-f.md#getvalue)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function getPowerPolicy(admin: Want, powerScene: PowerScene): PowerPolicy--><!--Device-deviceSettings-function getPowerPolicy(admin: Want, powerScene: PowerScene): PowerPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| powerScene | [PowerScene](arkts-mdm-devicesettings-powerscene-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
  let powerScene: deviceSettings.PowerScene = deviceSettings.PowerScene.TIME_OUT;
  let powerPolicy: deviceSettings.PowerPolicy = deviceSettings.getPowerPolicy(wantTemp, powerScene);
  console.info(`Succeeded in getting power policy ${JSON.stringify(powerPolicy)}`);
} catch (err) {
  console.error(`Failed to get power policy. Code: ${err.code}, message: ${err.message}`);
}
```
