# OnPermissionRequestEvent

Defines the callback information triggered when a permission request is received, including the request details. It is suitable for scenarios where handling permission grants is required, improving permission management flexibility and security.

**Since:** 12

<!--Device-unnamed-declare interface OnPermissionRequestEvent--><!--Device-unnamed-declare interface OnPermissionRequestEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## request

```TypeScript
request: PermissionRequest
```

User operation.

**Type:** [PermissionRequest](arkts-arkweb-permissionrequest-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnPermissionRequestEvent-request: PermissionRequest--><!--Device-OnPermissionRequestEvent-request: PermissionRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

