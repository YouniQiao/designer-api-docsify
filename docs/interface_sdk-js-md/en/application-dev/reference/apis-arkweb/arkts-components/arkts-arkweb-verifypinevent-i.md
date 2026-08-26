# VerifyPinEvent

Defines the callback triggered to notify the user of PIN verification.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## handler

```TypeScript
handler: VerifyPinHandler
```

User operation.

**Type:** [VerifyPinHandler](arkts-arkweb-verifypinhandler-c.md)

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

## identity

```TypeScript
identity: string
```

Certificate credential ID used for verification.

**Type:** string

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core
