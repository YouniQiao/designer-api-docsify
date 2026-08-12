# ActionMenuOptions

ActionMenu options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-promptAction-export interface ActionMenuOptions--><!--Device-promptAction-export interface ActionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## buttons

```TypeScript
buttons: PromptActionSingleButton | PromptActionDoubleButtons | PromptActionTripleButtons |
            PromptActionQuadrupleButtons | PromptActionQuintupleButtons | PromptActionSextupleButtons
```

Array of buttons in the dialog box.The array structure is {text:'button', color: '#666666'}.One to six buttons are supported.

**Type:** [PromptActionSingleButton](arkts-arkui-promptaction-promptactionsinglebutton-t.md) \| [PromptActionDoubleButtons](arkts-arkui-promptaction-promptactiondoublebuttons-t.md) \| [PromptActionTripleButtons](arkts-arkui-promptaction-promptactiontriplebuttons-t.md) \| [PromptActionQuadrupleButtons](arkts-arkui-promptaction-promptactionquadruplebuttons-t.md) \| [PromptActionQuintupleButtons](arkts-arkui-promptaction-promptactionquintuplebuttons-t.md) \| [PromptActionSextupleButtons](arkts-arkui-promptaction-promptactionsextuplebuttons-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-buttons: PromptActionSingleButton | PromptActionDoubleButtons | PromptActionTripleButtons |            PromptActionQuadrupleButtons | PromptActionQuintupleButtons | PromptActionSextupleButtons--><!--Device-ActionMenuOptions-buttons: PromptActionSingleButton | PromptActionDoubleButtons | PromptActionTripleButtons |            PromptActionQuadrupleButtons | PromptActionQuintupleButtons | PromptActionSextupleButtons-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Determine the immersive mode of the dialog.

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode--><!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether it is a modal dialog

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-isModal?: boolean--><!--Device-ActionMenuOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Determine the display level of the dialog.

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-levelMode?: LevelMode--><!--Device-ActionMenuOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: int
```

The uniqueId of any node in the router or navigation page.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-levelUniqueId?: int--><!--Device-ActionMenuOptions-levelUniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Callback function when the menu appears.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onDidAppear?: VoidCallback--><!--Device-ActionMenuOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Callback function when the menu disappears.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onDidDisappear?: VoidCallback--><!--Device-ActionMenuOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Callback function before the menu openAnimation starts.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onWillAppear?: VoidCallback--><!--Device-ActionMenuOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Callback function before the menu closeAnimation starts.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-onWillDisappear?: VoidCallback--><!--Device-ActionMenuOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to display in the sub window.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-showInSubWindow?: boolean--><!--Device-ActionMenuOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: uiMaterial.Material
```

Set system-styled materials for dialog. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of dialog.

Device Behavior Differences:The effect of same material may vary across different devices depending on their computing power.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-systemMaterial?: uiMaterial.Material--><!--Device-ActionMenuOptions-systemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string | Resource
```

Title of the text to display.

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionMenuOptions-title?: string | Resource--><!--Device-ActionMenuOptions-title?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

