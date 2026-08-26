# OnPermissionRequestEvent

Defines the callback information triggered when a permission request is received, including the request details. It is suitable for scenarios where handling permission grants is required, improving permission management flexibility and security.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## request

```TypeScript
request: PermissionRequest
```

User operation.

**Type:** [PermissionRequest](arkts-arkweb-permissionrequest-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
