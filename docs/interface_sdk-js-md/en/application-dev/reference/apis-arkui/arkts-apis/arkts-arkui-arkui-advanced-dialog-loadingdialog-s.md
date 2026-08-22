# LoadingDialog

Declare CustomDialog LoadingDialog

**Since:** 18

<!--Device-unnamed-export declare struct LoadingDialog--><!--Device-unnamed-export declare struct LoadingDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialog, ButtonOptions, ConfirmDialog, LoadingDialog, SelectDialog, TipsDialog, CustomContentDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';
import { AlertDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonOptions, AdvancedDialogV2ButtonAction, AdvancedDialogV2OnCheckedChange, ConfirmDialogV2, LoadingDialogV2, SelectDialogV2, TipsDialogV2, CustomContentDialogV2, PopoverDialogV2, PopoverDialogV2OnVisibleChange, PopoverDialogV2Options } from '@kit.ArkUI';
```

## content

```TypeScript
content?: ResourceStr
```

Sets the LoadingDialog content.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LoadingDialog-content?: ResourceStr--><!--Device-LoadingDialog-content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Controller

```TypeScript
Controller: CustomDialogController
```

Sets the LoadingDialog Controller.

**Type:** CustomDialogController

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LoadingDialog-Controller: CustomDialogController--><!--Device-LoadingDialog-Controller: CustomDialogController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## theme

```TypeScript
theme?: Theme | CustomTheme
```

Custom Theme.

**Type:** [Theme](../../apis-default/arkts-apis/arkts-arkui-theme-theme-i.md) \| [CustomTheme](../../apis-default/arkts-apis/arkts-arkui-theme-customtheme-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LoadingDialog-theme?: Theme | CustomTheme--><!--Device-LoadingDialog-theme?: Theme | CustomTheme-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## themeColorMode

```TypeScript
themeColorMode?: ThemeColorMode
```

Sets the LoadingDialog dark or light Mode.

**Type:** ThemeColorMode

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LoadingDialog-themeColorMode?: ThemeColorMode--><!--Device-LoadingDialog-themeColorMode?: ThemeColorMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

