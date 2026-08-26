# @ohos.multimodalInput.inputEventClient(Input Event Injection)

The **inputEventClient** module provides the capability of injecting key, mouse/touchpad, and touchscreen events.

**Since:** 26.0.0

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createKeyboardController(Input Event Injection)](arkts-input-inputeventclient-createkeyboardcontroller-f.md) | Creates a keyboard controller for simulating key operations. This API uses a promise to return the result. |
| [createMouseController(Input Event Injection)](arkts-input-inputeventclient-createmousecontroller-f.md) | Creates a mouse controller for simulating mouse operations. This API uses a promise to return the result. |
| [createTouchController(Input Event Injection)](arkts-input-inputeventclient-createtouchcontroller-f.md) | Creates a touch controller for simulating touch operations. This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [injectEvent(Input Event Injection)](arkts-input-inputeventclient-injectevent-f-sys.md) | Injects keys (including single keys and combination keys). |
| [injectKeyEvent(Input Event Injection)](arkts-input-inputeventclient-injectkeyevent-f-sys.md) | Injects key events (for both single keys and combination keys). |
| [injectMouseEvent(Input Event Injection)](arkts-input-inputeventclient-injectmouseevent-f-sys.md) | Injects a mouse/touchpad event. |
| [injectTouchEvent(Input Event Injection)](arkts-input-inputeventclient-injecttouchevent-f-sys.md) | Injects a touch event. |
| [permitInjection(Input Event Injection)](arkts-input-inputeventclient-permitinjection-f-sys.md) | Specifies whether to authorize event injection. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [KeyboardController(Input Event Injection)](arkts-input-inputeventclient-keyboardcontroller-i.md) | Provides the capability of simulating key operations. The simulated key operation sequence must meet the following requirements: 1. A key can only be pressed when it is in the released state, or when it is the most recently pressed key and has not been released. 2. A key can only be released after it has been pressed. 3. A maximum of five keys can be pressed and held simultaneously. |
| [MouseController(Input Event Injection)](arkts-input-inputeventclient-mousecontroller-i.md) | Provides the capability of simulating mouse operations. The simulated mouse operation sequence must meet the following requirements: 1. A mouse button can be pressed only when it is in the released state. 2. A mouse button can only be released after it has been pressed. 3. A valid axis event sequence must begin with a **beginAxis** call, followed by zero or more **updateAxis** calls, and end with an **endAxis** call. 4. Only one axis event sequence can be in progress at a time. |
| [TouchController(Input Event Injection)](arkts-input-inputeventclient-touchcontroller-i.md) | Provides the capability of simulating touch operations. The simulated touch operation sequence must meet the following requirements: 1. All touch points must share the same **displayId**. 2. Each touch point must begin with a **touchDown()** call, followed by zero or more **touchMove()** calls, and end with an **touchUp()** call. |
| [TouchPoint(Input Event Injection)](arkts-input-inputeventclient-touchpoint-i.md) | Represents information about a single touch point on the display. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [KeyEvent(Input Event Injection)](arkts-input-inputeventclient-keyevent-i-sys.md) | Defines the key event to inject. |
| [KeyEventData(Input Event Injection)](arkts-input-inputeventclient-keyeventdata-i-sys.md) | Defines the key event to inject. |
| [KeyEventInfo(Input Event Injection)](arkts-input-inputeventclient-keyeventinfo-i-sys.md) | Defines the key event information injected by the user. |
| [MouseEventData(Input Event Injection)](arkts-input-inputeventclient-mouseeventdata-i-sys.md) | Defines the mouse event data. |
| [TouchEventData(Input Event Injection)](arkts-input-inputeventclient-toucheventdata-i-sys.md) | Defines the touch event data. |
<!--DelEnd-->
