# setScreenOffTime (System API)

## Modules to Import

```TypeScript
```

## setScreenOffTime

```TypeScript
function setScreenOffTime(admin: Want, time: number): void
```

Sets the device screen-off time.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue)

**Required permissions:** ohos.permission.ENTERPRISE_SET_SCREENOFF_TIME

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setScreenOffTime(admin: Want, time: number): void--><!--Device-deviceSettings-function setScreenOffTime(admin: Want, time: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| time | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // Replace parameters with actual values.
  deviceSettings.setScreenOffTime(wantTemp, 30000);
  console.info(`Succeeded in setting screen off time`);
} catch(err) {
  console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}
```
