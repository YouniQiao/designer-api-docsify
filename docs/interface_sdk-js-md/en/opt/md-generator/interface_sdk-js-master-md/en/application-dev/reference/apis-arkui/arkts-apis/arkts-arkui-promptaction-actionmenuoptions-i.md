# ActionMenuOptions

Describes the options for showing the action menu.

**Since:** 9

<!--Device-promptAction-interface ActionMenuOptions--><!--Device-promptAction-interface ActionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## buttons

```TypeScript
buttons: [
            Button,
            Button?,
            Button?,
            Button?,
            Button?,
            Button?
        ]
```

Array of menu item buttons. The array structure is **{text:'button', color: '\#666666'}**. Up to six buttons are supported. If there are more than six buttons, only the first six buttons will be displayed.

**Type:** [             Button,             Button?,             Button?,             Button?,             Button?,             Button?         ]

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ActionMenuOptions-buttons: [            Button,            Button?,            Button?,            Button?,            Button?,            Button?        ]--><!--Device-ActionMenuOptions-buttons: [            Button,            Button?,            Button?,            Button?,            Button?,            Button?        ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Overlay effect for the page-level menu.&lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **ImmersiveMode.DEFAULT**&lt;br&gt;- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode--><!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether the menu is a modal, which has a mask applied and does not allow for interaction with other components around the menu. &lt;br&gt;**true**: The menu is a modal. &lt;br&gt;**false**: The menu is not a modal.&lt;br&gt;Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ActionMenuOptions-isModal?: boolean--><!--Device-ActionMenuOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Display level mode of the menu.&lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **LevelMode.OVERLAY**&lt;br&gt;- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ActionMenuOptions-levelMode?: LevelMode--><!--Device-ActionMenuOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: number
```

[Unique ID](js-apis-arkui-frameNode.md#getuniqueid12) of the node under the display level for the page-level menu.&lt;br&gt;Value range: a number no less than 0&lt;br&gt;**NOTE：**&lt;br&gt;- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** number

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ActionMenuOptions-levelUniqueId?: number--><!--Device-ActionMenuOptions-levelUniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: Callback<void>
```

Callback invoked after the menu appears.&lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.&lt;br&gt;2. When a menu is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.

**Type:** Callback&lt;void&gt;

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onDidAppear?: Callback<void>--><!--Device-ActionMenuOptions-onDidAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: Callback<void>
```

Callback invoked after the menu disappears.&lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** Callback&lt;void&gt;

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onDidDisappear?: Callback<void>--><!--Device-ActionMenuOptions-onDidDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: Callback<void>
```

Callback invoked before the menu appearance animation.&lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** Callback&lt;void&gt;

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onWillAppear?: Callback<void>--><!--Device-ActionMenuOptions-onWillAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: Callback<void>
```

Callback invoked before the menu disappearance animation.&lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** Callback&lt;void&gt;

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onWillDisappear?: Callback<void>--><!--Device-ActionMenuOptions-onWillDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the menu in a subwindow when the menu needs to be displayed outside the main window. &lt;br&gt;**true**: The menu is shown in a subwindow.&lt;br&gt;Default value: **false**, indicating that the dialog box is not displayed in a subwindow.&lt;br&gt;**NOTE：**&lt;br&gt; - A menu whose **showInSubWindow** attribute is **true** cannot trigger the display of another menu whose **showInSubWindow** attribute is also **true**.&lt;br&gt; - If **showInSubWindow** is set to **true** in **UIExtension**, the menu is aligned with the host window based on **UIExtension**.

**Type:** boolean

**Default:** false

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ActionMenuOptions-showInSubWindow?: boolean--><!--Device-ActionMenuOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

System material of the dialog box. Different materials have different effects and can affect visual attributes  such as the background color, border, and shadow of the dialog box.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ActionMenuOptions-systemMaterial?: SystemUiMaterial--><!--Device-ActionMenuOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string | Resource
```

Title of the dialog box.&lt;br&gt;Default value: **undefined**, which indicates that no title is not displayed by default.

**Type:** string \| Resource

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ActionMenuOptions-title?: string | Resource--><!--Device-ActionMenuOptions-title?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
