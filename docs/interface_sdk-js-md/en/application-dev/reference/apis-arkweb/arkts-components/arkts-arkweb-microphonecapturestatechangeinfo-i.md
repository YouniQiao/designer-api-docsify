# MicrophoneCaptureStateChangeInfo

Provides the state change information of the microphone when the callback is triggered, including the state before the change and the state after the change. It is suitable for scenarios where monitoring microphone state changes is required, improving microphone management visibility and user experience.

**Since:** 23

<!--Device-unnamed-declare interface MicrophoneCaptureStateChangeInfo--><!--Device-unnamed-declare interface MicrophoneCaptureStateChangeInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## newState

```TypeScript
newState: MicrophoneCaptureState
```

New state.

**Type:** [MicrophoneCaptureState](arkts-arkweb-microphonecapturestate-e.md)

**Since:** 23

<!--Device-MicrophoneCaptureStateChangeInfo-newState: MicrophoneCaptureState--><!--Device-MicrophoneCaptureStateChangeInfo-newState: MicrophoneCaptureState-End-->

**System capability:** SystemCapability.Web.Webview.Core

## originalState

```TypeScript
originalState: MicrophoneCaptureState
```

State before the change.

**Type:** [MicrophoneCaptureState](arkts-arkweb-microphonecapturestate-e.md)

**Since:** 23

<!--Device-MicrophoneCaptureStateChangeInfo-originalState: MicrophoneCaptureState--><!--Device-MicrophoneCaptureStateChangeInfo-originalState: MicrophoneCaptureState-End-->

**System capability:** SystemCapability.Web.Webview.Core

