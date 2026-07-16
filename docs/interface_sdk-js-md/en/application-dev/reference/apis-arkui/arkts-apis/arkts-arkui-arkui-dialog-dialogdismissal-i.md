# DialogDismissal

Provides information about the action to dismiss the dialog box.

**Since:** 26.1.0

<!--Device-unnamed-export interface DialogDismissal--><!--Device-unnamed-export interface DialogDismissal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DialogButtonOrientation, DialogState, DialogResult, DialogBaseController, DialogBaseAlignment, DialogDismissal } from '@kit.ArkUI';
```

## dismiss

```TypeScript
dismiss: VoidCallback
```

Callback for dismissing the dialog box. This API is called only when the dialog box needs to be exited.

**Type:** VoidCallback

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogDismissal-dismiss: VoidCallback--><!--Device-DialogDismissal-dismiss: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

Reason why the dialog box cannot be dismissed.

**Type:** DismissReason

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogDismissal-reason: DismissReason--><!--Device-DialogDismissal-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

