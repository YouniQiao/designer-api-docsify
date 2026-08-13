# turnOnMobileData

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## turnOnMobileData

```TypeScript
function turnOnMobileData(admin: Want, isForce: boolean): void
```

Turns on mobile data.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function turnOnMobileData(admin: Want, isForce: boolean): void--><!--Device-networkManager-function turnOnMobileData(admin: Want, isForce: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| isForce | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  networkManager.turnOnMobileData(wantTemp, true);
  console.info(`Turn on mobile data succeeded`);
} catch (err) {
  console.error(`Failed to turn on mobile data. Code: ${err.code}, message: ${err.message}`);
}
```
