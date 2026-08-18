# OnLoadInterceptEvent

Defines the callback information triggered when resource loading is intercepted, including the request details. It is suitable for scenarios where intercepting or handling resource loading is required, improving resource control flexibility and security.

**Since:** 12

<!--Device-unnamed-declare interface OnLoadInterceptEvent--><!--Device-unnamed-declare interface OnLoadInterceptEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## data

```TypeScript
data: WebResourceRequest
```

Information about the URL request.

**Type:** [WebResourceRequest](arkts-arkweb-webresourcerequest-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnLoadInterceptEvent-data: WebResourceRequest--><!--Device-OnLoadInterceptEvent-data: WebResourceRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

