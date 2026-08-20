# addAllowedDistributeAbilityConnBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addAllowedDistributeAbilityConnBundles

```TypeScript
function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void
```

Adds the cross-device application trustlist for a specific distributed service for a specified user. Applications in the trustlist can use the specific distributed service to transfer data across devices without being subject to the restrictions imposed by [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md).

Currently, the following distributed service type is supported: [collaboration service](arkts-mdm-applicationmanager-servicetype-e.md).

> **NOTE：**
> 
> 1. Before calling this API to set the application list allowed to use a specific distributed service, you must &gt; have already disabled one-way data transmission between devices (which is used for transferring data to other &gt; devices) via &gt; [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md).
> Otherwise, error code 9201043 is thrown.

> 2. When one-way data transmission between devices is re-enabled, the application list allowed to use the specific &gt; distributed service that was set via this API is automatically cleared.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void--><!--Device-applicationManager-function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appIdentifiers | Array&lt;string&gt; | Yes | Array of [unique identifiers](../../apis-ability-kit/arkts-apis/arkts-ability-bundleinfo-signatureinfo-i.md) of an application. You can call the [bundleManager.getBundleInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfo-f.md) API to obtain the **bundleInfo.signatureInfo.appIdentifier**. The total number of applications in the array cannot exceed 200. |
| serviceType | ServiceType | Yes | Distributed service type. |
| accountId | number | Yes | Account ID. The value is an integer greater than or equal to 0. <br> You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) of @ ohos.account.osAccount to obtain the ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9201043](../errorcode-enterpriseDeviceManager.md#9201043-prerequisites-for-calling-the-api-not-met) | Prerequisites for the API call have not been satisfied. For example, distributed outgoing transmission is not disallowed before adding the distributed bidirectional collaboration trustlist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

