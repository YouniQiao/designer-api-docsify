# NativeEmbedVisibilityInfo

Provides visibility information about the same-layer tag, including the visibility status and tag ID. It is suitable for scenarios where monitoring same-layer element visibility is required, improving rendering state management accuracy and user experience.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## embedId

```TypeScript
embedId: string
```

ID of the same-layer rendered tag.

**Type:** string

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## visibility

```TypeScript
visibility: boolean
```

Whether the same-layer tag is visible.The value **true** indicates that the same-layer tag is visible, and **false** indicates the opposite.

**Type:** boolean

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core
