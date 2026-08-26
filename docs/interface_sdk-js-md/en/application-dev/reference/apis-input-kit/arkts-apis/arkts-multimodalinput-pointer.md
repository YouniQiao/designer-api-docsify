# @ohos.multimodalInput.pointer(Mouse Pointer)

The **pointer** module provides APIs related to pointer attribute management, such as querying and setting pointer attributes.

**Since:** 9

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getPointerStyle(Mouse Pointer)](arkts-input-pointer-getpointerstyle-f.md) | Obtains the mouse pointer style type of a specified window. This API can obtain only the mouse pointer style type of windows within the current application process. This API uses an asynchronous callback to return the result. |
| [getPointerStyle(Mouse Pointer)](arkts-input-pointer-getpointerstyle-f.md) | Obtains the mouse pointer style type. This API can obtain only the mouse pointer style type of windows within the current application process. This API uses a promise to return the result. |
| [getPointerStyleSync(Mouse Pointer)](arkts-input-pointer-getpointerstylesync-f.md) | Queries the mouse pointer style type of a specified window, such as east arrow, west arrow, south arrow, and north arrow. This API can obtain only the mouse pointer style type of windows within the current application process. |
| [isPointerVisible(Mouse Pointer)](arkts-input-pointer-ispointervisible-f.md) | Obtains the visible status of the mouse pointer. This API uses an asynchronous callback to return the result. |
| [isPointerVisible(Mouse Pointer)](arkts-input-pointer-ispointervisible-f.md) | Obtains the visible status of the mouse pointer. This API uses a promise to return the result. |
| [isPointerVisibleSync(Mouse Pointer)](arkts-input-pointer-ispointervisiblesync-f.md) | Checks whether the mouse pointer is visible in the current window. This API returns the result synchronously. |
| [setCustomCursor(Mouse Pointer)](arkts-input-pointer-setcustomcursor-f.md) | Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcustomcursor). This API uses a promise to return the result. |
| [setCustomCursor(Mouse Pointer)](arkts-input-pointer-setcustomcursor-f.md) | Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcustomcursor). This API uses a promise to return the result.The cursor may be switched back to the system style in the following cases: application window layout change, hot zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of the cursor in different areas of the window. In this case, you need to reset the cursor style. |
| [setCustomCursorSync(Mouse Pointer)](arkts-input-pointer-setcustomcursorsync-f.md) | Sets a custom pointer style for a specified window synchronously. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcustomcursor). |
| [setPointerStyle(Mouse Pointer)](arkts-input-pointer-setpointerstyle-f.md) | Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcursor). This API uses an asynchronous callback to return the result. |
| [setPointerStyle(Mouse Pointer)](arkts-input-pointer-setpointerstyle-f.md) | Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcursor). This uses a promise to return the result. |
| [setPointerStyleSync(Mouse Pointer)](arkts-input-pointer-setpointerstylesync-f.md) | Sets the mouse pointer style type for a specified window and returns the result synchronously. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcursor). |
| [setPointerVisible(Mouse Pointer)](arkts-input-pointer-setpointervisible-f.md) | Sets whether the mouse pointer is visible in the current window. This API uses an asynchronous callback to return the result. |
| [setPointerVisible(Mouse Pointer)](arkts-input-pointer-setpointervisible-f.md) | Sets whether the mouse pointer is visible in the current window. This API uses a promise to return the result. |
| [setPointerVisibleSync(Mouse Pointer)](arkts-input-pointer-setpointervisiblesync-f.md) | Sets whether the mouse pointer is visible in the current window. This API returns the result synchronously. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getHoverScrollState(Mouse Pointer)](arkts-input-pointer-gethoverscrollstate-f-sys.md) | Obtains the mouse hover scrolling switch state. This API uses an asynchronous callback to return the result. |
| [getHoverScrollState(Mouse Pointer)](arkts-input-pointer-gethoverscrollstate-f-sys.md) | Obtains the status of the mouse hover scroll switch. This API uses a promise to return the result. |
| [getMousePrimaryButton(Mouse Pointer)](arkts-input-pointer-getmouseprimarybutton-f-sys.md) | Obtains the current primary mouse button. This API uses an asynchronous callback to return the result. |
| [getMousePrimaryButton(Mouse Pointer)](arkts-input-pointer-getmouseprimarybutton-f-sys.md) | Obtains the current primary mouse button. This API uses a promise to return the result. |
| [getMouseScrollDirection(Mouse Pointer)](arkts-input-pointer-getmousescrolldirection-f-sys.md) | Obtains the scroll direction of the mouse wheel. This API uses a promise to return the result asynchronously. |
| [getMouseScrollRows(Mouse Pointer)](arkts-input-pointer-getmousescrollrows-f-sys.md) | Obtains the number of mouse scroll lines. This API uses an asynchronous callback to return the result. |
| [getMouseScrollRows(Mouse Pointer)](arkts-input-pointer-getmousescrollrows-f-sys.md) | Obtains the number of mouse scroll lines. This API uses a promise to return the result. |
| [getPointerColor(Mouse Pointer)](arkts-input-pointer-getpointercolor-f-sys.md) | Obtains the mouse pointer color. This API uses an asynchronous callback to return the result. |
| [getPointerColor(Mouse Pointer)](arkts-input-pointer-getpointercolor-f-sys.md) | Obtains the current mouse pointer color. This API uses a promise to return the result. |
| [getPointerColorSync(Mouse Pointer)](arkts-input-pointer-getpointercolorsync-f-sys.md) | Obtains the pointer color. This API returns the result synchronously. |
| [getPointerSize(Mouse Pointer)](arkts-input-pointer-getpointersize-f-sys.md) | Obtains the current mouse pointer size. This API uses an asynchronous callback to return the result. |
| [getPointerSize(Mouse Pointer)](arkts-input-pointer-getpointersize-f-sys.md) | Obtains the current mouse pointer size. This API uses a promise to return the result. |
| [getPointerSizeSync(Mouse Pointer)](arkts-input-pointer-getpointersizesync-f-sys.md) | Obtains the pointer size. This API returns the result synchronously. |
| [getPointerSpeed(Mouse Pointer)](arkts-input-pointer-getpointerspeed-f-sys.md) | Obtains the mouse pointer speed. This API uses an asynchronous callback to return the result. |
| [getPointerSpeed(Mouse Pointer)](arkts-input-pointer-getpointerspeed-f-sys.md) | Obtains the mouse pointer speed. This API uses a promise to return the result. |
| [getPointerSpeedSync(Mouse Pointer)](arkts-input-pointer-getpointerspeedsync-f-sys.md) | Obtains the mouse pointer speed. This API returns the result synchronously. |
| [getTouchpadDoubleTapAndDragState(Mouse Pointer)](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md) | Obtains the touchpad number-tap and drag switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadDoubleTapAndDragState(Mouse Pointer)](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md) | Obtains the touchpad number-tap and drag switch state. This API uses a promise to return the result. |
| [getTouchpadPinchSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md) | Obtains the touchpad pinch switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadPinchSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md) | Obtains the touchpad pinch switch state. This API uses a promise to return the result. |
| [getTouchpadPointerSpeed(Mouse Pointer)](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md) | Obtains the touchpad pointer speed. This API uses an asynchronous callback to return the result. |
| [getTouchpadPointerSpeed(Mouse Pointer)](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md) | Obtains the touchpad pointer speed. This API uses a promise to return the result. |
| [getTouchpadRightClickType(Mouse Pointer)](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md) | Obtains the touchpad right-click menu type. This API uses an asynchronous callback to return the result. |
| [getTouchpadRightClickType(Mouse Pointer)](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md) | Obtains the touchpad right-click menu type. This API uses a promise to return the result. |
| [getTouchpadScrollDirection(Mouse Pointer)](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md) | Obtains the touchpad scroll direction. This API uses an asynchronous callback to return the result. |
| [getTouchpadScrollDirection(Mouse Pointer)](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md) | Obtains the scroll direction of the touchpad. This API uses a promise to return the result. |
| [getTouchpadScrollSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md) | Obtains the touchpad scroll switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadScrollSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md) | Obtains the touchpad scroll switch state. This API uses a promise to return the result. |
| [getTouchpadSwipeSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md) | Obtains the touchpad multi-finger swipe switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadSwipeSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md) | Obtains the touchpad multi-finger swipe switch state. This API uses a promise to return the result. |
| [getTouchpadTapSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadtapswitch-f-sys.md) | Obtains the touchpad tap switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadTapSwitch(Mouse Pointer)](arkts-input-pointer-gettouchpadtapswitch-f-sys.md) | Obtains the touchpad tap switch state. This API uses a promise to return the result. |
| [setHoverScrollState(Mouse Pointer)](arkts-input-pointer-sethoverscrollstate-f-sys.md) | Sets the mouse hover scrolling switch state. This API uses an asynchronous callback to return the result. |
| [setHoverScrollState(Mouse Pointer)](arkts-input-pointer-sethoverscrollstate-f-sys.md) | Sets the status of the mouse hover scroll switch. This API uses a promise to return the result. |
| [setMousePrimaryButton(Mouse Pointer)](arkts-input-pointer-setmouseprimarybutton-f-sys.md) | Sets the primary mouse button. This API uses an asynchronous callback to return the result. |
| [setMousePrimaryButton(Mouse Pointer)](arkts-input-pointer-setmouseprimarybutton-f-sys.md) | Sets the primary mouse button. This API uses a promise to return the result. |
| [setMouseScrollDirection(Mouse Pointer)](arkts-input-pointer-setmousescrolldirection-f-sys.md) | Sets the scroll direction of the mouse wheel. This API uses a promise to return the result asynchronously. |
| [setMouseScrollRows(Mouse Pointer)](arkts-input-pointer-setmousescrollrows-f-sys.md) | Sets the number of mouse scroll lines. This API uses an asynchronous callback to return the result. |
| [setMouseScrollRows(Mouse Pointer)](arkts-input-pointer-setmousescrollrows-f-sys.md) | Sets the number of mouse scroll lines. This API uses a promise to return the result. |
| [setPointerColor(Mouse Pointer)](arkts-input-pointer-setpointercolor-f-sys.md) | Sets the mouse pointer color. This API uses an asynchronous callback to return the result. |
| [setPointerColor(Mouse Pointer)](arkts-input-pointer-setpointercolor-f-sys.md) | Sets the mouse pointer color. This API uses a promise to return the result. |
| [setPointerColorSync(Mouse Pointer)](arkts-input-pointer-setpointercolorsync-f-sys.md) | Sets the pointer color. This API returns the result synchronously. |
| [setPointerSize(Mouse Pointer)](arkts-input-pointer-setpointersize-f-sys.md) | Sets the mouse pointer size. This API uses an asynchronous callback to return the result. |
| [setPointerSize(Mouse Pointer)](arkts-input-pointer-setpointersize-f-sys.md) | Sets the mouse pointer size. This API uses a promise to return the result. |
| [setPointerSizeSync(Mouse Pointer)](arkts-input-pointer-setpointersizesync-f-sys.md) | Sets the pointer size. This API returns the result synchronously. |
| [setPointerSpeed(Mouse Pointer)](arkts-input-pointer-setpointerspeed-f-sys.md) | Sets the mouse pointer speed. This API uses an asynchronous callback to return the result. |
| [setPointerSpeed(Mouse Pointer)](arkts-input-pointer-setpointerspeed-f-sys.md) | Sets the mouse pointer speed. This API uses a promise to return the result. |
| [setPointerSpeedSync(Mouse Pointer)](arkts-input-pointer-setpointerspeedsync-f-sys.md) | Sets the mouse pointer speed. This API returns the result synchronously. |
| [setTouchpadDoubleTapAndDragState(Mouse Pointer)](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md) | Sets the touchpad number-tap and drag switch state. This API uses an asynchronous callback to return the result. |
| [setTouchpadDoubleTapAndDragState(Mouse Pointer)](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md) | Sets the touchpad number-tap and drag switch state. This API uses a promise to return the result. |
| [setTouchpadPinchSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadpinchswitch-f-sys.md) | Sets the touchpad pinch switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadPinchSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadpinchswitch-f-sys.md) | Sets the touchpad pinch switch. This API uses a promise to return the result. |
| [setTouchpadPointerSpeed(Mouse Pointer)](arkts-input-pointer-settouchpadpointerspeed-f-sys.md) | Sets the touchpad pointer speed. This API uses an asynchronous callback to return the result. |
| [setTouchpadPointerSpeed(Mouse Pointer)](arkts-input-pointer-settouchpadpointerspeed-f-sys.md) | Sets the touchpad pointer speed. This API uses a promise to return the result. |
| [setTouchpadRightClickType(Mouse Pointer)](arkts-input-pointer-settouchpadrightclicktype-f-sys.md) | Sets the touchpad right-click menu type. This API uses an asynchronous callback to return the result. |
| [setTouchpadRightClickType(Mouse Pointer)](arkts-input-pointer-settouchpadrightclicktype-f-sys.md) | Sets the touchpad right-click menu type. This API uses a promise to return the result. |
| [setTouchpadScrollDirection(Mouse Pointer)](arkts-input-pointer-settouchpadscrolldirection-f-sys.md) | Sets the touchpad scroll direction. This API uses an asynchronous callback to return the result. |
| [setTouchpadScrollDirection(Mouse Pointer)](arkts-input-pointer-settouchpadscrolldirection-f-sys.md) | Sets the touchpad scroll direction. This API uses a promise to return the result. |
| [setTouchpadScrollSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadscrollswitch-f-sys.md) | Sets the touchpad scroll switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadScrollSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadscrollswitch-f-sys.md) | Sets the touchpad scroll switch. This API uses a promise to return the result. |
| [setTouchpadSwipeSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadswipeswitch-f-sys.md) | Sets the touchpad multi-finger swipe switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadSwipeSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadswipeswitch-f-sys.md) | Sets the touchpad multi-finger swipe switch. This API uses a promise to return the result. |
| [setTouchpadTapSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadtapswitch-f-sys.md) | Sets the touchpad tap switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadTapSwitch(Mouse Pointer)](arkts-input-pointer-settouchpadtapswitch-f-sys.md) | Sets the touchpad tap switch. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CursorConfig(Mouse Pointer)](arkts-input-pointer-cursorconfig-i.md) | Defines custom cursor configuration. |
| [CustomCursor(Mouse Pointer)](arkts-input-pointer-customcursor-i.md) | Defines custom cursor resources. |

### Enums

| Name | Description |
| --- | --- |
| [PointerStyle(Mouse Pointer)](arkts-input-pointer-pointerstyle-e.md) | Mouse pointer style types. |
| [PrimaryButton(Mouse Pointer)](arkts-input-pointer-primarybutton-e.md) | Type of the primary mouse button. |
| [RightClickType(Mouse Pointer)](arkts-input-pointer-rightclicktype-e.md) | Enumerates shortcut menu triggering modes. |
