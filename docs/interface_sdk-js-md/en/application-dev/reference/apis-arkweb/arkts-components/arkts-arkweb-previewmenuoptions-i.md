# PreviewMenuOptions

Configures preview menu options, supporting the vibration effect when the menu pops up. It is suitable for scenarios where enhanced menu interaction feedback is required, improving user experience.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## hapticFeedbackMode

```TypeScript
hapticFeedbackMode?: HapticFeedbackMode
```

Vibration effect when the menu is displayed. The **ohos.permission.VIBRATE** permission is required.Default value: **HapticFeedbackMode.DISABLED**, indicating no vibration when the menu is displayed.

**Type:** [HapticFeedbackMode](../../apis-arkui/arkts-components/arkts-arkui-hapticfeedbackmode-e.md)

**Default:** HapticFeedbackMode.DISABLED

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core
