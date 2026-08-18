# PreviewMenuOptions

Configures preview menu options, supporting the vibration effect when the menu pops up. It is suitable for scenarios where enhanced menu interaction feedback is required, improving user experience.

**Since:** 20

<!--Device-unnamed-declare interface PreviewMenuOptions--><!--Device-unnamed-declare interface PreviewMenuOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## hapticFeedbackMode

```TypeScript
hapticFeedbackMode?: HapticFeedbackMode
```

Vibration effect when the menu is displayed. The **ohos.permission.VIBRATE** permission is required. Default value: **HapticFeedbackMode.DISABLED**, indicating no vibration when the menu is displayed.

**Type:** HapticFeedbackMode

**Default:** HapticFeedbackMode.DISABLED

**Since:** 20

<!--Device-PreviewMenuOptions-hapticFeedbackMode?: HapticFeedbackMode--><!--Device-PreviewMenuOptions-hapticFeedbackMode?: HapticFeedbackMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

