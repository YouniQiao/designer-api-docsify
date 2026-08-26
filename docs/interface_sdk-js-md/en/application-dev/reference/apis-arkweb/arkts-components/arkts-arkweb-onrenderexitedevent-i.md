# OnRenderExitedEvent

Defines the callback triggered when the rendering process exits. It is suitable for scenarios where monitoring rendering process exceptions is required, improving rendering stability and troubleshooting efficiency.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## renderExitReason

```TypeScript
renderExitReason: RenderExitReason
```

Cause for the abnormal exit of the rendering process.

**Type:** [RenderExitReason](arkts-arkweb-renderexitreason-e.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
