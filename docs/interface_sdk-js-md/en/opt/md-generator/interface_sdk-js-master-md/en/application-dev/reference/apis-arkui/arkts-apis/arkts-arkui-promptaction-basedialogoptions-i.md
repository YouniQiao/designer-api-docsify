# BaseDialogOptions

Defines the options of the dialog box.

**Since:** 11

**Deprecated since:** -1

<!--Device-promptAction-interface BaseDialogOptions--><!--Device-promptAction-interface BaseDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction. &lt;br&gt;Default value: **DialogAlignment.Default** &lt;br&gt;**NOTE：**&lt;br&gt;If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

**Type:** [DialogAlignment](arkts-arkui-dialogalignment-e.md)

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-alignment?: DialogAlignment--><!--Device-BaseDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Whether to dismiss the dialog box when the mask is touched. The value **true** means to dismiss the dialog box when the mask is touched, and **false** means the opposite.&lt;br&gt;Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-autoCancel?: boolean--><!--Device-BaseDialogOptions-autoCancel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.

**Type:** [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-BaseDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-BaseDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.

**Type:** [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-BaseDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-BaseDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dialogTransition

```TypeScript
dialogTransition?: TransitionEffect
```

Transition effect for the dialog box content. By default, there is no transition effect.

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-BaseDialogOptions-dialogTransition?: TransitionEffect--><!--Device-BaseDialogOptions-dialogTransition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayModeInSubWindow

```TypeScript
displayModeInSubWindow?: DialogDisplayMode
```

Defines the dialog display mode when show in subwindow.

**Type:** [DialogDisplayMode](arkts-arkui-dialogdisplaymode-e.md)

**Default:** DialogDisplayMode.SCREEN_BASED

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BaseDialogOptions-displayModeInSubWindow?: DialogDisplayMode--><!--Device-BaseDialogOptions-displayModeInSubWindow?: DialogDisplayMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode. &lt;br&gt;Default value: **false**, meaning not to respond when the device is in semi-folded mode. &lt;br&gt;**NOTE：**&lt;br&gt;For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the lower half of the screen. For other devices, the prompt is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the upper half of the screen.

**Type:** boolean

**Default:** false

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-BaseDialogOptions-enableHoverMode?: boolean--><!--Device-BaseDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## focusable

```TypeScript
focusable?: boolean
```

Whether the dialog box can gain focus. &lt;br&gt;**true**: The dialog box can gain focus. &lt;br&gt;**false**: The dialog box cannot gain focus. &lt;br&gt;Default value: **true**. &lt;br&gt;**NOTE：**&lt;br&gt;Only dialog boxes that are displayed on top of the current window can gain focus.

**Type:** boolean

**Default:** true

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-BaseDialogOptions-focusable?: boolean--><!--Device-BaseDialogOptions-focusable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the dialog box in the hover state. &lt;br&gt;Default value: **HoverModeAreaType.BOTTOM_SCREEN**

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-BaseDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-BaseDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Overlay effect for the page-level dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **ImmersiveMode.DEFAULT** &lt;br&gt;- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BaseDialogOptions-immersiveMode?: ImmersiveMode--><!--Device-BaseDialogOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other components around the dialog box. &lt;br&gt;**true**: The dialog box is a modal. &lt;br&gt;**false**: The dialog box is not a modal. &lt;br&gt;Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-isModal?: boolean--><!--Device-BaseDialogOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidDistance

```TypeScript
keyboardAvoidDistance?: LengthMetrics
```

Distance between the dialog box and the keyboard after keyboard avoidance is applied. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **16vp** &lt;br&gt;- Default unit: vp &lt;br&gt;- This parameter takes effect only when **keyboardAvoidMode** is set to **DEFAULT**.

**Type:** LengthMetrics

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BaseDialogOptions-keyboardAvoidDistance?: LengthMetrics--><!--Device-BaseDialogOptions-keyboardAvoidDistance?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode?: KeyboardAvoidMode
```

How the dialog box avoids the soft keyboard when it is brought up. &lt;br&gt;Default value: **KeyboardAvoidMode.DEFAULT**

**Type:** KeyboardAvoidMode

**Default:** KeyboardAvoidMode.DEFAULT

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-keyboardAvoidMode?: KeyboardAvoidMode--><!--Device-BaseDialogOptions-keyboardAvoidMode?: KeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Display level of the dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **LevelMode.OVERLAY** &lt;br&gt;- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BaseDialogOptions-levelMode?: LevelMode--><!--Device-BaseDialogOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

Display order of the dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;- Default value: **LevelOrder.clamp(0)** &lt;br&gt;- Dynamic updating is not supported.

**Type:** [LevelOrder](arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returned by LevelOrder.clamp(0)

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-BaseDialogOptions-levelOrder?: LevelOrder--><!--Device-BaseDialogOptions-levelOrder?: LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: number
```

Unique ID of the node under the display level for the page-level dialog box. &lt;br&gt;Value range: a number no less than 0 &lt;br&gt;**NOTE：**&lt;br&gt;- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** number

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BaseDialogOptions-levelUniqueId?: number--><!--Device-BaseDialogOptions-levelUniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskColor

```TypeScript
maskColor?: ResourceColor
```

Mask color. &lt;br&gt;Default value: **0x33000000**

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-maskColor?: ResourceColor--><!--Device-BaseDialogOptions-maskColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area. &lt;br&gt;Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }** &lt;br&gt;**NOTE：**&lt;br&gt;**maskRect** does not take effect when **showInSubWindow** is set to **true**. &lt;br&gt;If only some properties in [Rectangle](../arkui-ts/ts-methods-alert-dialog-box.md#rectangle8) are set, the unset properties default to 0.

**Type:** [Rectangle](../arkts-components/arkts-arkui-rectangle-i.md)

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-maskRect?: Rectangle--><!--Device-BaseDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskTransition

```TypeScript
maskTransition?: TransitionEffect
```

Transition effect for the mask. By default, there is no transition effect.

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-BaseDialogOptions-maskTransition?: TransitionEffect--><!--Device-BaseDialogOptions-maskTransition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the dialog box based on the **alignment** settings. &lt;br&gt;Default value: **{&nbsp;dx:&nbsp;0&nbsp;,&nbsp;dy:&nbsp;0&nbsp;}**

**Type:** Offset

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-offset?: Offset--><!--Device-BaseDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: () => void
```

Event callback after the dialog box appears. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. &lt;br&gt;2. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears. &lt;br&gt;3. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**. &lt;br&gt;4. If the dialog box is dismissed before its appearance animation is finished, this callback is not invoked.

**Type:** () =&gt; void

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-onDidAppear?: () => void--><!--Device-BaseDialogOptions-onDidAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: () => void
```

Event callback after the dialog box disappears. &lt;br&gt;**NOTE：**&lt;br&gt;The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. &lt;br&gt;This callback is not triggered if the dialog box disappearance animation is interrupted (for example, by page navigation).

**Type:** () =&gt; void

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-onDidDisappear?: () => void--><!--Device-BaseDialogOptions-onDidDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: () => void
```

Event callback when the dialog box is about to appear. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. &lt;br&gt;2. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Type:** () =&gt; void

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-onWillAppear?: () => void--><!--Device-BaseDialogOptions-onWillAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: () => void
```

Event callback when the dialog box is about to disappear. &lt;br&gt;**NOTE：**&lt;br&gt;1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. &lt;br&gt;2. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

**Type:** () =&gt; void

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-onWillDisappear?: () => void--><!--Device-BaseDialogOptions-onWillDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissDialogAction>
```

Callback for interactive dismissal of the dialog box. &lt;br&gt;**NOTE：**&lt;br&gt;1. If this callback is registered, the dialog box will not be dismissed immediately after the user touches the mask or the Back button, presses the Esc key, or swipes left or right on the screen. The **reason** parameter in the callback is used to determine whether the dialog box can be dismissed. The reason returned by the component does not support the value **CLOSE_BUTTON**. &lt;br&gt;2. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.

**Type:** Callback&lt;[DismissDialogAction](arkts-arkui-promptaction-dismissdialogaction-i.md)&gt;

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-onWillDismiss?: Callback<DismissDialogAction>--><!--Device-BaseDialogOptions-onWillDismiss?: Callback<DismissDialogAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window. &lt;br&gt;**true**: The dialog box is shown in a subwindow. &lt;br&gt;Default value: **false**, meaning the dialog box is displayed within the application, not in a separate subwindow

**Type:** boolean

**Default:** false

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-showInSubWindow?: boolean--><!--Device-BaseDialogOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

System material of the dialog box. Different materials have different effects and can affect visual attributes such as the background color, border, and shadow of the dialog box.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t-sys.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BaseDialogOptions-systemMaterial?: SystemUiMaterial--><!--Device-BaseDialogOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Transition effect for the appearance and disappearance of the dialog box.&lt;br&gt;**NOTE：**&lt;br&gt; 1. If this parameter is not set, the default effect is used. &lt;br&gt; 2. Touching the Back button during the appearance animation pauses the appearance animation and starts the disappearance animation. The final effect is one obtained after the curves of the appearance and disappearance animations are combined. &lt;br&gt; 3. Touching the Back button during the exit animation does not affect the animation playback. Touching the Back button again closes the application.

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseDialogOptions-transition?: TransitionEffect--><!--Device-BaseDialogOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
