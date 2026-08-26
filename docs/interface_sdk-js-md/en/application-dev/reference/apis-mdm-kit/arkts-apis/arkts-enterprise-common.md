# @ohos.enterprise.common(Common Module)

The module provides pure type definitions for common capabilities within MDM Kit, including enum types and data structs. It exports type declarations only and does not include any implementation logic or executable code.  
**Use cases:** In enterprise device administrator application development, the types defined in this module are used in scenarios such as configuring device management and control policies, managing application instances, handling application installation results, and listening for policy changes. These types provide unified parameter and return value standards for the APIs of various sub-modules within MDM Kit.  
**Benefits:** Standardized type definitions simplify the development process of enterprise device administrator applications, improve code maintainability and type safety, and reduce type-related runtime errors.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import common from '@kit.MDMKit';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ApplicationInstance(Common Module)](arkts-mdm-common-applicationinstance-i.md) | Defines application instance data.It is used as an input parameter in the [addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md), [removeUserNonStopApps](arkts-mdm-applicationmanager-removeusernonstopapps-f.md), [addFreezeExemptedApps](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md), and [removeFreezeExemptedApps](arkts-mdm-applicationmanager-removefreezeexemptedapps-f.md) APIs. |
| [InstallationResult(Common Module)](arkts-mdm-common-installationresult-i.md) | An object that holds the application installation result.This object is used as a callback parameter in [EnterpriseAdminExtensionAbility.onMarketAppInstallResult](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onmarketappinstallresult). |
| [PolicyChangedEvent(Common Module)](arkts-mdm-common-policychangedevent-i.md) | Defines the policy change event.This API is used as a callback input parameter of [onAdminPolicyChanged](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onadminpolicychanged). |

### Enums

| Name | Description |
| --- | --- |
| [ManagedPolicy(Common Module)](arkts-mdm-common-managedpolicy-e.md) | Enumerates enterprise device management policies. |
| [Result(Common Module)](arkts-mdm-common-result-e.md) | Enumerates application installation results. |
| [StartupScene(Common Module)](arkts-mdm-common-startupscene-e.md) | Startup wizard completion scenario. When the initial switch to a sub-user (only on PCs), OTA upgrade, and first- time startup wizard are complete, the device system calls the [onStartupGuideCompleted](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onstartupguidecompleted) API to notify the device administrator application. |

### Types

| Name | Description |
| --- | --- |
| [EnterpriseAdminExtensionContext(Common Module)](arkts-mdm-common-enterpriseadminextensioncontext-t.md) | **EnterpriseAdminExtensionContext** is the context of [EnterpriseAdminExtensionAbility](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md) and inherits from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md). |
