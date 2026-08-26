# FullScreenExitHandler

Implements the **FullScreenExitHandler** object to notify you that the **Web** component exits full screen mode. For details about the sample code, see [onFullScreenEnter](arkts-arkweb-web-attribute.md#onfullscreenenter).

**Since:** 9

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## constructor

```TypeScript
constructor()
```

Constructs a **FullScreenExitHandler** API.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## exitFullScreen

```TypeScript
exitFullScreen(): void
```

Exits full screen mode.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core
