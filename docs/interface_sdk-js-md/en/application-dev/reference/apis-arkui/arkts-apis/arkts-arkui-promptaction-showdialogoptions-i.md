# ShowDialogOptions

Describes the options for showing the dialog box.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-promptAction-interface ShowDialogOptions--><!--Device-promptAction-interface ShowDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction.&lt;br&gt; Default value: **DialogAlignment.Default**&lt;br&gt; **NOTE：**&lt;br&gt; If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

**Type:** DialogAlignment

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-alignment?: DialogAlignment--><!--Device-ShowDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box. &lt;br&gt;Default value: **BlurStyle.COMPONENT_ULTRA_THICK** &lt;br&gt;**NOTE：**&lt;br&gt;Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ShowDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.

**Type:** BackgroundBlurStyleOptions

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ShowDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-ShowDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the dialog box. &lt;br&gt;Default value: **Color.Transparent**. &lt;br&gt;**NOTE：**&lt;br&gt;The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Type:** ResourceColor

**Default:** Color.Transparent

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowDialogOptions-backgroundColor?: ResourceColor--><!--Device-ShowDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.

**Type:** BackgroundEffectOptions

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ShowDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-ShowDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttons

```TypeScript
buttons?: Array<Button>
```

Array of buttons in the dialog box. The array structure is {text:'button',&nbsp;color:&nbsp;'\#666666'}. More than one button is supported.

**Type:** Array&lt;Button&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-buttons?: Array<Button>--><!--Device-ShowDialogOptions-buttons?: Array<Button>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode. &lt;br&gt;Default value: **false**, meaning not to respond when the device is in semi-folded mode. &lt;br&gt;**NOTE：**&lt;br&gt;For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the lower half of the screen. For other devices, the prompt is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the upper half of the screen.

**Type:** boolean

**Default:** false

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ShowDialogOptions-enableHoverMode?: boolean--><!--Device-ShowDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Default display area of the dialog box in semi-folded mode. &lt;br&gt;Default value: **HoverModeAreaType.BOTTOM_SCREEN**

**Type:** HoverModeAreaType

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ShowDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-ShowDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Overlay effect for the page-level dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **ImmersiveMode.DEFAULT** &lt;br&gt;- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ShowDialogOptions-immersiveMode?: ImmersiveMode--><!--Device-ShowDialogOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other components around the dialog box. &lt;br&gt;**true**: The dialog box is a modal. &lt;br&gt;**false**: The dialog box is not a modal. &lt;br&gt;Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowDialogOptions-isModal?: boolean--><!--Device-ShowDialogOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Display level of the dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **LevelMode.OVERLAY** &lt;br&gt;- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ShowDialogOptions-levelMode?: LevelMode--><!--Device-ShowDialogOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

Display order of the dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **LevelOrder.clamp(0)** &lt;br&gt;- Dynamic updating is not supported.

**Type:** [LevelOrder](arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returned by LevelOrder.clamp(0)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ShowDialogOptions-levelOrder?: LevelOrder--><!--Device-ShowDialogOptions-levelOrder?: LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: number
```

Unique ID of the node under the display level for the page-level dialog box. &lt;br&gt;Value range: a number no less than 0&lt;br&gt;**NOTE：**&lt;br&gt;- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ShowDialogOptions-levelUniqueId?: number--><!--Device-ShowDialogOptions-levelUniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area of the dialog box. Events within the mask area are blocked, while events outside the mask area are transmitted.&lt;br&gt; Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**&lt;br&gt; **NOTE：**&lt;br&gt; **maskRect** does not take effect when **showInSubWindow** is set to **true**.&lt;br&gt; If only some properties in [Rectangle](../arkui-ts/ts-methods-alert-dialog-box.md#rectangle8) are set, the unset properties default to 0.

**Type:** Rectangle

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-maskRect?: Rectangle--><!--Device-ShowDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message?: string | Resource
```

Text body.&lt;br&gt;Default value: **undefined**, which indicates that no content is displayed by default.

**Type:** string \| Resource

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-message?: string | Resource--><!--Device-ShowDialogOptions-message?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the dialog box relative to the alignment position.&lt;br&gt; Default value: **{&nbsp;dx:&nbsp;0&nbsp;,&nbsp;dy:&nbsp;0&nbsp;}**

**Type:** Offset

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-offset?: Offset--><!--Device-ShowDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: Callback<void>
```

Callback invoked after the dialog box appears. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear. &lt;br&gt;2. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears. &lt;br&gt;3. When a dialog box is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**. &lt;br&gt;4. If the dialog box is dismissed before its appearance animation is finished, the animation will be interrupted, and **onDidAppear** will not be invoked.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ShowDialogOptions-onDidAppear?: Callback<void>--><!--Device-ShowDialogOptions-onDidAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: Callback<void>
```

Callback invoked after the dialog box disappears. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ShowDialogOptions-onDidDisappear?: Callback<void>--><!--Device-ShowDialogOptions-onDidDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: Callback<void>
```

Callback invoked before the dialog box appearance animation. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear. &lt;br&gt;2. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ShowDialogOptions-onWillAppear?: Callback<void>--><!--Device-ShowDialogOptions-onWillAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: Callback<void>
```

Callback invoked before the dialog box disappearance animation. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ShowDialogOptions-onWillDisappear?: Callback<void>--><!--Device-ShowDialogOptions-onWillDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box. &lt;br&gt; Default value on 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_MD** when the dialog box is focused and **ShadowStyle.OUTER_FLOATING_SM** otherwise On other devices, the dialog box has no shadow by default.

**Type:** ShadowOptions \| ShadowStyle

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-ShowDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window. &lt;br&gt;**true**: The dialog box is shown in a subwindow. &lt;br&gt;**false** (default): The dialog box is displayed within the application, not in a separate subwindow. &lt;br&gt;Note: A dialog box whose **showInSubWindow** attribute is **true** cannot trigger the display of another dialog box whose **showInSubWindow** attribute is also **true**.

**Type:** boolean

**Default:** false

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowDialogOptions-showInSubWindow?: boolean--><!--Device-ShowDialogOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

System material of the dialog box. Different materials have different effects and can affect visual attributes such as the background color, border, and shadow of the dialog box.

**Type:** SystemUiMaterial

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ShowDialogOptions-systemMaterial?: SystemUiMaterial--><!--Device-ShowDialogOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string | Resource
```

Title of the dialog box.&lt;br&gt;Default value: **undefined**, which indicates that no title is not displayed by default.

**Type:** string \| Resource

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-title?: string | Resource--><!--Device-ShowDialogOptions-title?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

