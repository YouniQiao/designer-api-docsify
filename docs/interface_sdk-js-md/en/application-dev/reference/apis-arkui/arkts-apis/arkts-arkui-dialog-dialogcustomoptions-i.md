# DialogCustomOptions

Options for the custom-style dialog.The dialog content is provided as the first parameter of present() method,not inside this options object.

**Inheritance/Implementation:** DialogCustomOptions extends [DialogBaseOptions](arkts-arkui-dialog-dialogbaseoptions-i.md)

**Since:** 26.1.0

<!--Device-dialog-declare interface DialogCustomOptions extends DialogBaseOptions--><!--Device-dialog-declare interface DialogCustomOptions extends DialogBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DialogButtonOrientation, DialogState, DialogResult, DialogBaseController, DialogBaseAlignment, DialogDismissal } from '@kit.ArkUI';
```

## customStyle

```TypeScript
customStyle?: boolean
```

Whether to enable the custom style.

**Type:** boolean

**Default:** false

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogCustomOptions-customStyle?: boolean--><!--Device-DialogCustomOptions-customStyle?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

