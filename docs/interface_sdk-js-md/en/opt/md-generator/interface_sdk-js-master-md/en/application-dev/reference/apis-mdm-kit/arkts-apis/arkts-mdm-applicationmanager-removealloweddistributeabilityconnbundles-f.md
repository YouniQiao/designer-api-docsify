# removeAllowedDistributeAbilityConnBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## removeAllowedDistributeAbilityConnBundles

```TypeScript
function removeAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void
```

Removes the cross-device application trustlist for a specific distributed service for a specified user. After the trustlist is removed, if there are still remaining applications in the list, only those applications can use the specific distributed service to transmit data across devices without being subject to the restrictions imposed by [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount). If the list has been removed and there are no remaining applications, no applications under the specified user are allowed to use the specific distributed service for cross-device data transmission.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void--><!--Device-applicationManager-function removeAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appIdentifiers | Array & lt;string & gt; | Yes |
| serviceType | [ServiceType](../../apis-calendar-kit/arkts-apis/arkts-calendar-calendarmanager-servicetype-e.md) | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace it as required.
  let appIdentifiers: Array<string> = ['6917****3569'];
  let accountId: number = 100;
  applicationManager.removeAllowedDistributeAbilityConnBundles(wantTemp, appIdentifiers, applicationManager.ServiceType.COLLABORATION_SERVICE, accountId);
  console.info('Succeeded in removing allowed distribute ability conn bundles.');
  // Note: After removing the application list allowed to use collaboration services for a user, whether to lift the disablement of one-way data transmission between devices for that user should be determined based on actual business requirements.
} catch(err) {
  console.error(`Failed to remove allowed distribute ability conn bundles. Code: ${err.code}, message: ${err.message}`);
}
```
