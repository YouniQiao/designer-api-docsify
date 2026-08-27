# BaseDialogOptions

Defines the options of the dialog box.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## onDidAppear

```TypeScript
onDidAppear?: () => void
```

Event callback after the dialog box appears.   
**NOTE：**
1. The normal timing sequence is as follows: onWillAppear &gt; onDidAppear &gt; (onDateAccept/onCancel/onDateChange) &gt; onWillDisappear &gt; onDidDisappear. 
2. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears. 
3. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**. 
4. If the dialog box is dismissed before its appearance animation is finished, this callback is not invoked.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: () => void
```

Event callback after the dialog box disappears.   
**NOTE：**The normal timing sequence is as follows: onWillAppear &gt; onDidAppear &gt; (onDateAccept/onCancel/onDateChange) &gt; onWillDisappear &gt; onDidDisappear. This callback is not triggered if the dialog box disappearance animation is interrupted (for example, by page navigation).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: () => void
```

Event callback when the dialog box is about to appear.   
**NOTE：**
1. The normal timing sequence is as follows: onWillAppear &gt; onDidAppear &gt; (onDateAccept/onCancel/onDateChange) &gt; onWillDisappear &gt; onDidDisappear. 
2. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: () => void
```

Event callback when the dialog box is about to disappear.   
**NOTE：**
1. The normal timing sequence is as follows: onWillAppear &gt; onDidAppear &gt; (onDateAccept/onCancel/onDateChange) &gt; onWillDisappear &gt; onDidDisappear. 
2. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction. Default value: **DialogAlignment.Default**   
**NOTE：**If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

**Type:** [DialogAlignment](arkts-arkui-dialogalignment-e.md)

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Whether to dismiss the dialog box when the mask is touched. The value **true** means to dismiss the dialog box when the mask is touched, and **false** means the opposite.Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.

**Type:** [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.

**Type:** [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dialogTransition

```TypeScript
dialogTransition?: TransitionEffect
```

Transition effect for the dialog box content. By default, there is no transition effect.

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayModeInSubWindow

```TypeScript
displayModeInSubWindow?: DialogDisplayMode
```

Defines the dialog display mode when show in subwindow.

**Type:** [DialogDisplayMode](arkts-arkui-dialogdisplaymode-e.md)

**Default:** DialogDisplayMode.SCREEN_BASED

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode. Default value: **false**, meaning not to respond when the device is in semi-folded mode.   
**NOTE：**For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the lower half of the screen. For other devices, the prompt is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the upper half of the screen.

**Type:** boolean

**Default:** false

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## focusable

```TypeScript
focusable?: boolean
```

Whether the dialog box can gain focus.   
**true**: The dialog box can gain focus.   
**false**: The dialog box cannot gain focus. Default value: **true**.   
**NOTE：**Only dialog boxes that are displayed on top of the current window can gain focus.

**Type:** boolean

**Default:** true

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the dialog box in the hover state. Default value: **HoverModeAreaType.BOTTOM_SCREEN**

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Overlay effect for the page-level dialog box.   
**NOTE：**
- Default value: **ImmersiveMode.DEFAULT**
- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other components around the dialog box.   
**true**: The dialog box is a modal.   
**false**: The dialog box is not a modal. Default value: **true**.

**Type:** boolean

**Default:** true

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidDistance

```TypeScript
keyboardAvoidDistance?: LengthMetrics
```

Distance between the dialog box and the keyboard after keyboard avoidance is applied.   
**NOTE：**
- Default value: **16vp**
- Default unit: vp
- This parameter takes effect only when **keyboardAvoidMode** is set to **DEFAULT**.

**Type:** LengthMetrics

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode?: KeyboardAvoidMode
```

How the dialog box avoids the soft keyboard when it is brought up. Default value: **KeyboardAvoidMode.DEFAULT**

**Type:** KeyboardAvoidMode

**Default:** KeyboardAvoidMode.DEFAULT

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Display level of the dialog box.   
**NOTE：**
- Default value: **LevelMode.OVERLAY**
- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

Display order of the dialog box.   
**NOTE：**
- Default value: **LevelOrder.clamp(0)**
- Dynamic updating is not supported.

**Type:** [LevelOrder](arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returned by LevelOrder.clamp(0)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: number
```

Unique ID of the node under the display level for the page-level dialog box. Value range: a number no less than 0   
**NOTE：**
- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Type:** number

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskColor

```TypeScript
maskColor?: ResourceColor
```

Mask color. Default value: **0x33000000**

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area. Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**   
**NOTE：**
**maskRect** does not take effect when **showInSubWindow** is set to **true**. If only some properties in [Rectangle](../arkui-ts/ts-methods-alert-dialog-box.md#rectangle8) are set, the unset properties default to 0.

**Type:** [Rectangle](../arkts-components/arkts-arkui-rectangle-i.md)

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskTransition

```TypeScript
maskTransition?: TransitionEffect
```

Transition effect for the mask. By default, there is no transition effect.

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the dialog box based on the **alignment** settings. Default value: **{&nbsp;dx:&nbsp;0&nbsp;,&nbsp;dy:&nbsp;0&nbsp;}**

**Type:** Offset

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissDialogAction>
```

Callback for interactive dismissal of the dialog box.   
**NOTE：**
1. If this callback is registered, the dialog box will not be dismissed immediately after the user touches the mask or the Back button, presses the Esc key, or swipes left or right on the screen. The **reason** parameter in the callback is used to determine whether the dialog box can be dismissed. The reason returned by the component does not support the value **CLOSE_BUTTON**. 
2. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.

**Type:** Callback&lt;[DismissDialogAction](arkts-arkui-promptaction-dismissdialogaction-i.md)&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.   
**true**: The dialog box is shown in a subwindow. Default value: **false**, meaning the dialog box is displayed within the application, not in a separate subwindow

**Type:** boolean

**Default:** false

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

System material of the dialog box. Different materials have different effects and can affect visual attributes such as the background color, border, and shadow of the dialog box.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Transition effect for the appearance and disappearance of the dialog box.  
**NOTE：**
 1. If this parameter is not set, the default effect is used. 
 2. Touching the Back button during the appearance animation pauses the appearance animation and starts the disappearance animation. The final effect is one obtained after the curves of the appearance and disappearance animations are combined. 
 3. Touching the Back button during the exit animation does not affect the animation playback. Touching the Back button again closes the application.

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
