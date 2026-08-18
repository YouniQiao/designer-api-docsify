# CameraCaptureStateChangeInfo

Provides the state change information of the camera when the callback is triggered, including the state before the change and the new state. It is suitable for scenarios where monitoring camera state changes is required, improving camera management visibility and user experience.

**Since:** 23

<!--Device-unnamed-declare interface CameraCaptureStateChangeInfo--><!--Device-unnamed-declare interface CameraCaptureStateChangeInfo-End-->

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
newState: CameraCaptureState
```

New state.

**Type:** [CameraCaptureState](arkts-arkweb-cameracapturestate-e.md)

**Since:** 23

<!--Device-CameraCaptureStateChangeInfo-newState: CameraCaptureState--><!--Device-CameraCaptureStateChangeInfo-newState: CameraCaptureState-End-->

**System capability:** SystemCapability.Web.Webview.Core

## originalState

```TypeScript
originalState: CameraCaptureState
```

State before the change.

**Type:** [CameraCaptureState](arkts-arkweb-cameracapturestate-e.md)

**Since:** 23

<!--Device-CameraCaptureStateChangeInfo-originalState: CameraCaptureState--><!--Device-CameraCaptureStateChangeInfo-originalState: CameraCaptureState-End-->

**System capability:** SystemCapability.Web.Webview.Core

