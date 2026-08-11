# addAllowedDistributeAbilityConnBundles

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addAllowedDistributeAbilityConnBundles

```TypeScript
function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void
```

Adds the cross-device application trustlist for a specific distributed service for a specified user. Applications in the trustlist can use the specific distributed service to transfer data across devices without being subject to the restrictions imposed by  
[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount).

Currently, the following distributed service type is supported:  
[collaboration service](arkts-mdm-applicationmanager-servicetype-e.md).

> **NOTE：**
> 
> 1. Before calling this API to set the application list allowed to use a specific distributed service, you must
> have already disabled one-way data transmission between devices (which is used for transferring data to other
> devices) via
> [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount).
> Otherwise, error code 9201043 is thrown.

> 2. When one-way data transmission between devices is re-enabled, the application list allowed to use the specific
> distributed service that was set via this API is automatically cleared.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void--><!--Device-applicationManager-function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appIdentifiers | Array&lt;string&gt; | Yes |
| serviceType | [ServiceType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-servicetype-e.md) | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9201043](../errorcode-enterpriseDeviceManager.md#9201043-prerequisites-for-calling-the-api-not-met) |

## Examples

```TypeScript
import { applicationManager, restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

// If you want to disable data transmission to other devices for all applications except specified ones on the device under user 100, perform the following two steps:
let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let accountId: number = 100;

// Step 1. Disable one-way data transmission between devices for user 100. (If this capability has been disabled before, you do not need to disable it again.)
try {
  restrictions.setDisallowedPolicyForAccount(wantTemp, restrictions.FeatureForAccount.DISTRIBUTED_TRANSMISSION_OUTGOING, true, accountId);
  console.info('Succeeded in setting distributedTransmissionOutgoing disabled');
} catch (err) {
  console.error(`Failed to set distributedTransmissionOutgoing disabled. Code is ${err.code}, message is ${err.message}`);
}

// Step 2: Set the list of applications that are allowed to use a specific distributed service (for example, the collaboration service) under user 100.
try {
  // Replace it as required.
  let appIdentifiers: Array<string> = ['6917****3569'];
  applicationManager.addAllowedDistributeAbilityConnBundles(wantTemp, appIdentifiers, applicationManager.ServiceType.COLLABORATION_SERVICE, accountId);
  console.info('Succeeded in adding allowed distribute ability conn bundles.');
} catch(err) {
  console.error(`Failed to add allowed distribute ability conn bundles. Code: ${err.code}, message: ${err.message}`);
}
// After the preceding two steps are performed, under user 100, only the application 6917****3569 can transmit data to other devices through the collaboration service. Other applications cannot transmit data to other devices.
// Note: After disabling one-way data transmission between devices for a specific user, whether to add an application list allowed to use collaboration services depends on actual business requirements.
```
