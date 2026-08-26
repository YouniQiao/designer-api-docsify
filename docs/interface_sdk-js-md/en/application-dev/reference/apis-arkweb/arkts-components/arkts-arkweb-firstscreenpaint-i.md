# FirstScreenPaint

Provides the event information when the first screen paint is detected, including the URL and paint time. It is suitable for scenarios where monitoring page first screen rendering performance is required, improving performance optimization accuracy and user experience.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## firstScreenPaintTime

```TypeScript
firstScreenPaintTime: number
```

Time when the first screen paint is completed for the page pointed to by url.Unit: ms.

**Type:** number

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## navigationStartTime

```TypeScript
navigationStartTime: number
```

Time when navigation starts for the page pointed to by url.Unit: ms.

**Type:** number

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

URL of the first screen paint statistics.

**Type:** string

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core
