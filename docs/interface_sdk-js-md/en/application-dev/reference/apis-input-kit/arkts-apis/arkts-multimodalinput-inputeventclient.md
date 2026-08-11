# @ohos.multimodalInput.inputEventClient(Input Event Injection)

The **inputEventClient** module provides the capability of injecting key, mouse/touchpad, and touchscreen events.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace inputEventClient--><!--Device-unnamed-declare namespace inputEventClient-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createKeyboardController](arkts-input-inputeventclient-createkeyboardcontroller-f.md#createkeyboardcontroller) | Creates a keyboard controller for simulating key operations. This API uses a promise to return the result. |
| [createMouseController](arkts-input-inputeventclient-createmousecontroller-f.md#createmousecontroller) | Creates a mouse controller for simulating mouse operations. This API uses a promise to return the result. |
| [createTouchController](arkts-input-inputeventclient-createtouchcontroller-f.md#createtouchcontroller) | Creates a touch controller for simulating touch operations. This API uses a promise to return the result. |
| [injectEvent](arkts-input-inputeventclient-injectevent-f.md#injectevent) | Injects keys (including single keys and combination keys). |
| [injectEvent](arkts-input-inputeventclient-injectevent-f.md#injectevent-1) | Inject system keys. |
| [injectKeyEvent](arkts-input-inputeventclient-injectkeyevent-f.md#injectkeyevent) | Injects key events (for both single keys and combination keys). |
| [injectMouseEvent](arkts-input-inputeventclient-injectmouseevent-f.md#injectmouseevent) | Injects a mouse/touchpad event. |
| [injectTouchEvent](arkts-input-inputeventclient-injecttouchevent-f.md#injecttouchevent) | Injects a touch event. |
| [permitInjection](arkts-input-inputeventclient-permitinjection-f.md#permitinjection) | Specifies whether to authorize event injection. |

### Interfaces

| Name | Description |
| --- | --- |
| [KeyEvent](arkts-input-inputeventclient-keyevent-i.md) | Defines the key event to inject. |
| [KeyEventData](arkts-input-inputeventclient-keyeventdata-i.md) | Defines the key event to inject. |
| [KeyEventInfo](arkts-input-inputeventclient-keyeventinfo-i.md) | Defines the key event information injected by the user. |
| [KeyboardController](arkts-input-inputeventclient-keyboardcontroller-i.md) | Provides the capability of simulating key operations. The simulated key operation sequence must meet the following requirements:  1. A key can only be pressed when it is in the released state, or when it is the most recently pressed key and has not been released.2. A key can only be released after it has been pressed.3. A maximum of five keys can be pressed and held simultaneously. |
| [MouseController](arkts-input-inputeventclient-mousecontroller-i.md) | Provides the capability of simulating mouse operations. The simulated mouse operation sequence must meet the following requirements:  1. A mouse button can be pressed only when it is in the released state.2. A mouse button can only be released after it has been pressed.3. A valid axis event sequence must begin with a **beginAxis** call, followed by zero or more **updateAxis** calls,and end with an **endAxis** call.4. Only one axis event sequence can be in progress at a time. |
| [MouseEventData](arkts-input-inputeventclient-mouseeventdata-i.md) | Defines the mouse event data. |
| [TouchController](arkts-input-inputeventclient-touchcontroller-i.md) | Provides the capability of simulating touch operations. The simulated touch operation sequence must meet the following requirements:  1. All touch points must share the same **displayId**.2. Each touch point must begin with a **touchDown()** call, followed by zero or more **touchMove()** calls, and end with an **touchUp()** call. |
| [TouchEventData](arkts-input-inputeventclient-toucheventdata-i.md) | Defines the touch event data. |
| [TouchPoint](arkts-input-inputeventclient-touchpoint-i.md) | Represents information about a single touch point on the display. |

