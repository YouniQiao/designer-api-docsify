# OnConsoleEvent

Represents the callback invoked to notify the host application of a JavaScript console message.

**Since:** 12

<!--Device-unnamed-declare interface OnConsoleEvent--><!--Device-unnamed-declare interface OnConsoleEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## message

```TypeScript
message: ConsoleMessage
```

Console message.

**Type:** [ConsoleMessage](arkts-arkweb-consolemessage-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnConsoleEvent-message: ConsoleMessage--><!--Device-OnConsoleEvent-message: ConsoleMessage-End-->

**System capability:** SystemCapability.Web.Webview.Core

