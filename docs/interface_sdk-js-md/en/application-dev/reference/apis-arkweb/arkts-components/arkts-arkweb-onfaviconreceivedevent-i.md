# OnFaviconReceivedEvent

Defines the callback information triggered when the app receives a new favicon, including the icon PixelMap object. It is suitable for scenarios where obtaining web page favicons is required, improving icon management flexibility and user experience.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## favicon

```TypeScript
favicon: PixelMap
```

**PixelMap** object of the received favicon.

**Type:** PixelMap

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
