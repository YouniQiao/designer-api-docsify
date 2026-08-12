# ShowDialogOptions

Defines the option of show dialog.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [ShowDialogOptions](ohos.promptAction/promptAction.ShowDialogOptions)

<!--Device-prompt-interface ShowDialogOptions--><!--Device-prompt-interface ShowDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { prompt } from '@kit.ArkUI';
```

## buttons

```TypeScript
buttons?: [Button, Button?, Button?]
```

Array of buttons in the dialog box.The array structure is {text:'button', color: '#666666'}.One to three buttons are supported. The first button is of the positiveButton type, the second is of the negativeButton type, and the third is of the neutralButton type.

**Type:** [Button, Button?, Button?]

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [buttons](ohos.promptAction/promptAction.ShowDialogOptions#buttons)

<!--Device-ShowDialogOptions-buttons?: [Button, Button?, Button?]--><!--Device-ShowDialogOptions-buttons?: [Button, Button?, Button?]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message?: string
```

Text body.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [message](ohos.promptAction/promptAction.ShowDialogOptions#message)

<!--Device-ShowDialogOptions-message?: string--><!--Device-ShowDialogOptions-message?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string
```

Title of the text to display.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [title](ohos.promptAction/promptAction.ShowDialogOptions#title)

<!--Device-ShowDialogOptions-title?: string--><!--Device-ShowDialogOptions-title?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
