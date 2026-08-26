# OnLoadInterceptEvent

Defines the callback information triggered when resource loading is intercepted, including the request details. It is suitable for scenarios where intercepting or handling resource loading is required, improving resource control flexibility and security.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## data

```TypeScript
data: WebResourceRequest
```

Information about the URL request.

**Type:** [WebResourceRequest](arkts-arkweb-webresourcerequest-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
