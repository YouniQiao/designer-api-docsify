# OnPageEndEvent

Defines the callback information triggered when the web page loading ends, including the page URL. It is suitable for scenarios where monitoring page loading completion is required, improving page lifecycle management capabilities.

**Since:** 12

<!--Device-unnamed-declare interface OnPageEndEvent--><!--Device-unnamed-declare interface OnPageEndEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## url

```TypeScript
url: string
```

URL of the page after the web page is loaded.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnPageEndEvent-url: string--><!--Device-OnPageEndEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

