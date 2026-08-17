# UICommonEvent

Defines a UICommonEvent which is used to set different common event to target component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface UICommonEvent--><!--Device-unnamed-export declare interface UICommonEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOnAppear

```TypeScript
setOnAppear(callback: VoidCallback | undefined): void
```

Set or reset the callback is triggered when a component mounts a display.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnAppear(callback: VoidCallback | undefined): void--><!--Device-UICommonEvent-setOnAppear(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes | The callback will be triggered when a component mounts a display. If set undefined will reset the target callback. |

## setOnBlur

```TypeScript
setOnBlur(callback: VoidCallback | undefined): void
```

Set or reset the callback which is triggered when lose focus.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnBlur(callback: VoidCallback | undefined): void--><!--Device-UICommonEvent-setOnBlur(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes | The callback will be triggered when a component lose focus. If set undefined will reset the target callback. |

## setOnClick

```TypeScript
setOnClick(callback: Callback<ClickEvent> | undefined): void
```

Set or reset the callback which will be triggered a click event when clicked.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnClick(callback: Callback<ClickEvent> | undefined): void--><!--Device-UICommonEvent-setOnClick(callback: Callback<ClickEvent> | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-na-callback-t.md)&lt;[ClickEvent](arkts-na-common-clickevent-i.md)&gt; \| undefined | Yes | The callback about the click event. If set undefined will reset the target callback. |

## setOnDisappear

```TypeScript
setOnDisappear(callback: VoidCallback | undefined): void
```

Set or reset the callback is triggered when component uninstallation disappears.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnDisappear(callback: VoidCallback | undefined): void--><!--Device-UICommonEvent-setOnDisappear(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes | The callback will be triggered when component uninstallation disappears. If set undefined will reset the target callback. |

## setOnFocus

```TypeScript
setOnFocus(callback: VoidCallback | undefined): void
```

Set or reset the callback which is triggered when component get focus.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnFocus(callback: VoidCallback | undefined): void--><!--Device-UICommonEvent-setOnFocus(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes | The callback will be triggered when a component get focus. If set undefined will reset the target callback. |

## setOnHover

```TypeScript
setOnHover(callback: HoverCallback | undefined): void
```

Set or reset the callback which is triggered when has a hover event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnHover(callback: HoverCallback | undefined): void--><!--Device-UICommonEvent-setOnHover(callback: HoverCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [HoverCallback](arkts-na-hovercallback-t.md) \| undefined | Yes | The callback will be triggered when has a hover event. If set undefined will reset the target callback. |

## setOnKeyEvent

```TypeScript
setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void
```

Set or reset the callback is triggered when component has keyboard input.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void--><!--Device-UICommonEvent-setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-na-callback-t.md)&lt;[KeyEvent](arkts-na-common-keyevent-i.md)&gt; \| undefined | Yes | The callback will be triggered when has keyboard input. If set undefined will reset the target callback. |

## setOnMouse

```TypeScript
setOnMouse(callback: Callback<MouseEvent> | undefined): void
```

Set or reset the callback which is triggered when has a mouse event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnMouse(callback: Callback<MouseEvent> | undefined): void--><!--Device-UICommonEvent-setOnMouse(callback: Callback<MouseEvent> | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-na-callback-t.md)&lt;[MouseEvent](arkts-na-common-mouseevent-i.md)&gt; \| undefined | Yes | The callback will be triggered when has mouse input. If set undefined will reset the target callback. |

## setOnSizeChange

```TypeScript
setOnSizeChange(callback: SizeChangeCallback | undefined): void
```

Sets the callback for the onSizeChange event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnSizeChange(callback: SizeChangeCallback | undefined): void--><!--Device-UICommonEvent-setOnSizeChange(callback: SizeChangeCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SizeChangeCallback](arkts-na-sizechangecallback-t.md) \| undefined | Yes | The callback will be triggered when the size of component changed. If set undefined will reset the target callback. |

## setOnTouch

```TypeScript
setOnTouch(callback: Callback<TouchEvent> | undefined): void
```

Set or reset the callback which will be triggered a touch event when touched.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnTouch(callback: Callback<TouchEvent> | undefined): void--><!--Device-UICommonEvent-setOnTouch(callback: Callback<TouchEvent> | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-na-callback-t.md)&lt;[TouchEvent](arkts-na-common-touchevent-i.md)&gt; \| undefined | Yes | The callback about the touch event. If set undefined will reset the target callback. |

## setOnVisibleAreaApproximateChange

```TypeScript
setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void
```

Sets the onVisibleAreaChange callback that limits the callback interval.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UICommonEvent-setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void--><!--Device-UICommonEvent-setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [VisibleAreaEventOptions](arkts-na-common-visibleareaeventoptions-i.md) | Yes | The options for the visibility event. |
| event | [VisibleAreaChangeCallback](arkts-na-visibleareachangecallback-t.md) \| undefined | Yes | The callback will be triggered when the visibleArea of component changed and get close to any number in ratios defined by options. If set undefined will reset the target callback. |

