# WindowFeatures

Provides the feature information of the new window requested to be created by the web page, including the size and location. It is suitable for scenarios where precise control of new window attributes is required, improving window layout accuracy and user experience.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## height

```TypeScript
height: number
```

Height of the new window, in pixels.

**Type:** number

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## width

```TypeScript
width: number
```

Width of the new window, in pixels.

**Type:** number

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## x

```TypeScript
x: number
```

X coordinate of the top-left corner of the new window, in pixels.

**Type:** number

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## y

```TypeScript
y: number
```

Y coordinate of the top-left corner of the new window, in pixels.

**Type:** number

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core
