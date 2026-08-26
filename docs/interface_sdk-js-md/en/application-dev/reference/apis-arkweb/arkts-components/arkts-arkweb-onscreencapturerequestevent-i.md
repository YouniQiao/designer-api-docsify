# OnScreenCaptureRequestEvent

Defines the callback information triggered when a screen capture request is received. It is suitable for scenarios where handling screen recording permissions is required, improving screen recording process controllability and security.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## handler

```TypeScript
handler: ScreenCaptureHandler
```

User operation.

**Type:** [ScreenCaptureHandler](arkts-arkweb-screencapturehandler-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
