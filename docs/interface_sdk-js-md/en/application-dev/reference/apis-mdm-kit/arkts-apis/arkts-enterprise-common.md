# @ohos.enterprise.common(Common Module)

The module provides pure type definitions for common capabilities within MDM Kit, including enum types and data structs. It exports type declarations only and does not include any implementation logic or executable code.  
**Use cases:** In enterprise device administrator application development, the types defined in this module are used in scenarios such as configuring device management and control policies, managing application instances, handling application installation results, and listening for policy changes. These types provide unified parameter and return value standards for the APIs of various sub-modules within MDM Kit.  
**Benefits:** Standardized type definitions simplify the development process of enterprise device administrator applications, improve code maintainability and type safety, and reduce type-related runtime errors.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { common } from '@kit.MDMKit';
```

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationInstance(Common Module)](arkts-mdm-common-applicationinstance-i.md) |
| [InstallationResult(Common Module)](arkts-mdm-common-installationresult-i.md) |
| [PolicyChangedEvent(Common Module)](arkts-mdm-common-policychangedevent-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ManagedPolicy(Common Module)](arkts-mdm-common-managedpolicy-e.md) |
| [Result(Common Module)](arkts-mdm-common-result-e.md) |
| [StartupScene(Common Module)](arkts-mdm-common-startupscene-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EnterpriseAdminExtensionContext(Common Module)](arkts-mdm-common-enterpriseadminextensioncontext-t.md) |
