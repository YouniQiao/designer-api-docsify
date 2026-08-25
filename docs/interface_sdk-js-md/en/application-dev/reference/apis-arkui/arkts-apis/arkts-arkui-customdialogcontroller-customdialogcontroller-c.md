# CustomDialogController

Use the CustomDialogController class to display the custom pop-up window.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
close(): void
```

Closes the custom pop-up window. If the window is closed, the window does not take effect.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: CustomDialogControllerOptions)
```

The constructor transfers parameter settings.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomDialogControllerOptions](arkts-arkui-customdialogcontroller-customdialogcontrolleroptions-i.md) | Yes |

## getExternalOptions

```TypeScript
getExternalOptions(): CustomDialogControllerExternalOptions
```

Obtains the external options of CustomDialogController.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomDialogControllerExternalOptions](arkts-arkui-customdialogcontroller-customdialogcontrollerexternaloptions-i.md) |

## getState

```TypeScript
getState(): PromptActionCommonState
```

Get the state of the custom pop-up window.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PromptActionCommonState](arkts-arkui-promptactioncommonstate-t.md) |

## open

```TypeScript
open(): void
```

Display the content of the customized pop-up window. If the content has been displayed, it does not take effect.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
