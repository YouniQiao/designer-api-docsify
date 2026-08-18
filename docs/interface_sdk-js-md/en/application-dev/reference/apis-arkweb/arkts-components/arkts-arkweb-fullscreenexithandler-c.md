# FullScreenExitHandler

Implements the **FullScreenExitHandler** object to notify you that the **Web** component exits full screen mode. For details about the sample code, see [onFullScreenEnter](arkts-arkweb-web-attribute.md#onfullscreenenter).

**Since:** 9

<!--Device-unnamed-declare class FullScreenExitHandler--><!--Device-unnamed-declare class FullScreenExitHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

Constructs a **FullScreenExitHandler** API.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FullScreenExitHandler-constructor()--><!--Device-FullScreenExitHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## exitFullScreen

```TypeScript
exitFullScreen(): void
```

Exits full screen mode.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FullScreenExitHandler-exitFullScreen(): void--><!--Device-FullScreenExitHandler-exitFullScreen(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

