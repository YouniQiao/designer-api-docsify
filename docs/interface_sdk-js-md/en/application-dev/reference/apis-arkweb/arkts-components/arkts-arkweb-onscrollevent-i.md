# OnScrollEvent

Defines the callback information triggered when the scrollbar scrolls to a specified position, including the horizontal and vertical offsets.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## xOffset

```TypeScript
xOffset: number
```

Position of the scrollbar on the x-axis relative to the leftmost of the web page.Unit: vp.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## yOffset

```TypeScript
yOffset: number
```

Position of the scrollbar on the y-axis relative to the top of the web page.Unit: vp.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
