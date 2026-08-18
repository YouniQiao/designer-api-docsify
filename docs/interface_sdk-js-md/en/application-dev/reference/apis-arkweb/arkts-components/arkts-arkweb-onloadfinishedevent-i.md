# OnLoadFinishedEvent

Defines the callback information triggered when the web page loading ends, including the page URL. It is suitable for scenarios where monitoring page loading completion is required, improving page lifecycle management capabilities.

**Since:** 20

<!--Device-unnamed-declare interface OnLoadFinishedEvent--><!--Device-unnamed-declare interface OnLoadFinishedEvent-End-->

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

URL of the page.

**Type:** string

**Since:** 20

<!--Device-OnLoadFinishedEvent-url: string--><!--Device-OnLoadFinishedEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

