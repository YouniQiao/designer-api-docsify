# OnErrorReceiveEvent

Defines the callback information triggered when an error occurs during web page loading, including the request and error details. It is suitable for scenarios where monitoring and handling web page loading errors are required, improving error handling timeliness and user experience.

**Since:** 12

<!--Device-unnamed-declare interface OnErrorReceiveEvent--><!--Device-unnamed-declare interface OnErrorReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## error

```TypeScript
error: WebResourceError
```

Encapsulated information about the web page resource loading error.

**Type:** [WebResourceError](arkts-arkweb-webresourceerror-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnErrorReceiveEvent-error: WebResourceError--><!--Device-OnErrorReceiveEvent-error: WebResourceError-End-->

**System capability:** SystemCapability.Web.Webview.Core

## request

```TypeScript
request: WebResourceRequest
```

Encapsulation of a web page request.

**Type:** [WebResourceRequest](arkts-arkweb-webresourcerequest-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnErrorReceiveEvent-request: WebResourceRequest--><!--Device-OnErrorReceiveEvent-request: WebResourceRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

