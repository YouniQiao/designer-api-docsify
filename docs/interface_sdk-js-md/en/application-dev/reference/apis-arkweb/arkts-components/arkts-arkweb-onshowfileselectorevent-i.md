# OnShowFileSelectorEvent

Defines the callback information for the file selector result, including the result and parameter details.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## fileSelector

```TypeScript
fileSelector: FileSelectorParam
```

Information about the file selector.

**Type:** [FileSelectorParam](arkts-arkweb-fileselectorparam-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## result

```TypeScript
result: FileSelectorResult
```

File selection result to be sent to the **Web** component.

**Type:** [FileSelectorResult](arkts-arkweb-fileselectorresult-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core
