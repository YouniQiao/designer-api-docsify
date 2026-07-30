# addAllowedDistributeAbilityConnBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addAllowedDistributeAbilityConnBundles

```TypeScript
function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void
```

Adds the applications that are allowed to distribute ability connection.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void--><!--Device-applicationManager-function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) | Yes | admin indicates the enterprise admin extension ability information. |
| appIdentifiers | Array&lt;string&gt; | Yes | appIdentifiers indicates the list of application appIdentifiers. |
| serviceType | [ServiceType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-servicetype-e.md) | Yes | serviceType indicates the type of distribute ability. |
| accountId | number | Yes | accountId indicates the ID of OS account.<br>The value must be an integer greater than or equal to 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9201043](../errorcode-enterpriseDeviceManager.md#9201043-prerequisites-for-calling-the-api-not-met) | Prerequisites for the API call have not been satisfied. For example,distributed outgoing transmission is not disallowed before adding the distributed bidirectional collaboration trustlist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |

**Example**

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

