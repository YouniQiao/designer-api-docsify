# CustomDialogController

Use the CustomDialogController class to display the custom pop-up window.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class CustomDialogController--><!--Device-unnamed-export declare class CustomDialogController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
close(): void
```

Closes the custom pop-up window. If the window is closed, the window does not take effect.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-close(): void--><!--Device-CustomDialogController-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: CustomDialogControllerOptions)
```

The constructor transfers parameter settings.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-constructor(value: CustomDialogControllerOptions)--><!--Device-CustomDialogController-constructor(value: CustomDialogControllerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CustomDialogControllerOptions](arkts-customdialogcontroller-customdialogcontrolleroptions-i.md) | Yes |  |

## getExternalOptions

```TypeScript
getExternalOptions(): CustomDialogControllerExternalOptions
```

Obtains the external options of CustomDialogController.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-getExternalOptions(): CustomDialogControllerExternalOptions--><!--Device-CustomDialogController-getExternalOptions(): CustomDialogControllerExternalOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CustomDialogControllerExternalOptions](arkts-customdialogcontroller-customdialogcontrollerexternaloptions-i.md) | return the external options of dialog. |

## getState

```TypeScript
getState(): PromptActionCommonState
```

Get the state of the custom pop-up window.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-getState(): PromptActionCommonState--><!--Device-CustomDialogController-getState(): PromptActionCommonState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PromptActionCommonState](arkts-promptactioncommonstate-t.md) | return the state of dialog. |

## open

```TypeScript
open(): void
```

Display the content of the customized pop-up window. If the content has been displayed, it does not take effect.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-open(): void--><!--Device-CustomDialogController-open(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

