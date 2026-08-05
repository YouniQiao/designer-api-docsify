# ActionMenuOptions

Describes the options for showing the action menu.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-promptAction-interface ActionMenuOptions--><!--Device-promptAction-interface ActionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ActionMenuOptions-buttons: [            Button,            Button?,            Button?,            Button?,            Button?,            Button?        ]--><!--Device-ActionMenuOptions-buttons: [            Button,            Button?,            Button?,            Button?,            Button?,            Button?        ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Overlay effect for the page-level menu. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Default value: **ImmersiveMode.DEFAULT** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** ImmersiveMode

**Default:** ImmersiveMode.DEFAULT

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode--><!--Device-ActionMenuOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether the menu is a modal, which has a mask applied and does not allow for interaction with other components around the menu. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**true**: The menu is a modal. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**false**: The menu is not a modal. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ActionMenuOptions-isModal?: boolean--><!--Device-ActionMenuOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Display level mode of the menu. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Default value: **LevelMode.OVERLAY** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Type:** LevelMode

**Default:** LevelMode.OVERLAY

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ActionMenuOptions-levelMode?: LevelMode--><!--Device-ActionMenuOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: number
```

\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ of the node under the display level for the page-level menu. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Value range: a number no less than 0 \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ActionMenuOptions-levelUniqueId?: number--><!--Device-ActionMenuOptions-levelUniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: Callback<void>
```

Callback invoked after the menu appears. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_2. When a menu is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.

**Type:** Callback&lt;void&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onDidAppear?: Callback<void>--><!--Device-ActionMenuOptions-onDidAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: Callback<void>
```

Callback invoked after the menu disappears. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** Callback&lt;void&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onDidDisappear?: Callback<void>--><!--Device-ActionMenuOptions-onDidDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: Callback<void>
```

Callback invoked before the menu appearance animation.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** Callback&lt;void&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onWillAppear?: Callback<void>--><!--Device-ActionMenuOptions-onWillAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: Callback<void>
```

Callback invoked before the menu disappearance animation. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** Callback&lt;void&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ActionMenuOptions-onWillDisappear?: Callback<void>--><!--Device-ActionMenuOptions-onWillDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the menu in a subwindow when the menu needs to be displayed outside the main window. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**true**: The menu is shown in a subwindow. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: **false**, indicating that the dialog box is not displayed in a subwindow.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ - A menu whose **showInSubWindow** attribute is **true** cannot trigger the display of another menu whose **showInSubWindow** attribute is also **true**. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_ - If **showInSubWindow** is set to **true** in **UIExtension**, the menu is aligned with the host window based on **UIExtension**.

**Type:** boolean

**Default:** false

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ActionMenuOptions-showInSubWindow?: boolean--><!--Device-ActionMenuOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

System material of the dialog box. Different materials have different effects and can affect visual attributes such as the background color, border, and shadow of the dialog box.

**Type:** SystemUiMaterial

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ActionMenuOptions-systemMaterial?: SystemUiMaterial--><!--Device-ActionMenuOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string | Resource
```

Title of the dialog box.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **undefined**, which indicates that no title is not displayed by default.

**Type:** string \| Resource

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ActionMenuOptions-title?: string | Resource--><!--Device-ActionMenuOptions-title?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

