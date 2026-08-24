# @ohos.enterprise.EnterpriseAdminExtensionAbility

## Modules to Import

```TypeScript
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [EnterpriseAdminExtensionAbility](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md) | This module provides the [enterprise device management extension ability](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability) and is the core component of the enterprise device administrator application.  **Main functions**:  - Provides lifecycle management capabilities for device administrator applications (enabling, disabling, startup, and so on). - Provides application lifecycle event listening capabilities (installation, uninstallation, startup, stop, update). - Provides system account management event listening capabilities (account addition, switch, removal). - Provides system-level event callbacks for Kiosk mode, key events, log collection, and system updates. - Provides policy change event listening capabilities.  **Use cases:** Enterprise device administrator application development, enterprise application lifecycle management, device security control, account management, and device O&M monitoring.To have the capabilities provided by this module, for example, to receive a notification when a device administrator application is enabled or disabled, you need to create an **EnterpriseAdminExtensionAbility** instance for the device administrator application and overload related APIs. |

