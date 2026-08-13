# @ohos.multimodalInput.pointer

The **pointer** module provides APIs related to pointer attribute management, such as querying and setting pointer attributes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace pointer--><!--Device-unnamed-declare namespace pointer-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getPointerStyle) | Obtains the mouse pointer style type of a specified window. This API can obtain only the mouse pointer style type of windows within the current application process. This API uses an asynchronous callback to return the result. |
| [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getPointerStyle) | Obtains the mouse pointer style type. This API can obtain only the mouse pointer style type of windows within the current application process. This API uses a promise to return the result. |
| [getPointerStyleSync](arkts-input-pointer-getpointerstylesync-f.md#getPointerStyleSync) | Queries the mouse pointer style type of a specified window, such as east arrow, west arrow, south arrow, and north arrow. This API can obtain only the mouse pointer style type of windows within the current application process. |
| [isPointerVisible](arkts-input-pointer-ispointervisible-f.md#isPointerVisible) | Obtains the visible status of the mouse pointer. This API uses an asynchronous callback to return the result. |
| [isPointerVisible](arkts-input-pointer-ispointervisible-f.md#isPointerVisible) | Obtains the visible status of the mouse pointer. This API uses a promise to return the result. |
| [isPointerVisibleSync](arkts-input-pointer-ispointervisiblesync-f.md#isPointerVisibleSync) | Checks whether the mouse pointer is visible in the current window. This API returns the result synchronously. |
| [setCustomCursor](arkts-input-pointer-setcustomcursor-f.md#setCustomCursor) | Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). This API uses a promise to return the result. |
| [setCustomCursor](arkts-input-pointer-setcustomcursor-f.md#setCustomCursor) | Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). This API uses a promise to return the result. The cursor may be switched back to the system style in the following cases: application window layout change, hot zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of the cursor in different areas of the window. In this case, you need to reset the cursor style. |
| [setCustomCursorSync](arkts-input-pointer-setcustomcursorsync-f.md#setCustomCursorSync) | Sets a custom pointer style for a specified window synchronously. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). |
| [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md#setPointerStyle) | Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCursor). This API uses an asynchronous callback to return the result. |
| [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md#setPointerStyle) | Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCursor). This uses a promise to return the result. |
| [setPointerStyleSync](arkts-input-pointer-setpointerstylesync-f.md#setPointerStyleSync) | Sets the mouse pointer style type for a specified window and returns the result synchronously. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCursor). |
| [setPointerVisible](arkts-input-pointer-setpointervisible-f.md#setPointerVisible) | Sets whether the mouse pointer is visible in the current window. This API uses an asynchronous callback to return the result. |
| [setPointerVisible](arkts-input-pointer-setpointervisible-f.md#setPointerVisible) | Sets whether the mouse pointer is visible in the current window. This API uses a promise to return the result. |
| [setPointerVisibleSync](arkts-input-pointer-setpointervisiblesync-f.md#setPointerVisibleSync) | Sets whether the mouse pointer is visible in the current window. This API returns the result synchronously. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getHoverScrollState](arkts-input-pointer-gethoverscrollstate-f-sys.md#getHoverScrollState) | Obtains the mouse hover scrolling switch state. This API uses an asynchronous callback to return the result. |
| [getHoverScrollState](arkts-input-pointer-gethoverscrollstate-f-sys.md#getHoverScrollState-(System-API)) | Obtains the status of the mouse hover scroll switch. This API uses a promise to return the result. |
| [getMousePrimaryButton](arkts-input-pointer-getmouseprimarybutton-f-sys.md#getMousePrimaryButton) | Obtains the current primary mouse button. This API uses an asynchronous callback to return the result. |
| [getMousePrimaryButton](arkts-input-pointer-getmouseprimarybutton-f-sys.md#getMousePrimaryButton-(System-API)) | Obtains the current primary mouse button. This API uses a promise to return the result. |
| [getMouseScrollDirection](arkts-input-pointer-getmousescrolldirection-f-sys.md#getMouseScrollDirection) | Obtains the scroll direction of the mouse wheel. This API uses a promise to return the result asynchronously. |
| [getMouseScrollRows](arkts-input-pointer-getmousescrollrows-f-sys.md#getMouseScrollRows) | Obtains the number of mouse scroll lines. This API uses an asynchronous callback to return the result. |
| [getMouseScrollRows](arkts-input-pointer-getmousescrollrows-f-sys.md#getMouseScrollRows-(System-API)) | Obtains the number of mouse scroll lines. This API uses a promise to return the result. |
| [getPointerColor](arkts-input-pointer-getpointercolor-f-sys.md#getPointerColor) | Obtains the mouse pointer color. This API uses an asynchronous callback to return the result. |
| [getPointerColor](arkts-input-pointer-getpointercolor-f-sys.md#getPointerColor-(System-API)) | Obtains the current mouse pointer color. This API uses a promise to return the result. |
| [getPointerColorSync](arkts-input-pointer-getpointercolorsync-f-sys.md#getPointerColorSync) | Obtains the pointer color. This API returns the result synchronously. |
| [getPointerSize](arkts-input-pointer-getpointersize-f-sys.md#getPointerSize) | Obtains the current mouse pointer size. This API uses an asynchronous callback to return the result. |
| [getPointerSize](arkts-input-pointer-getpointersize-f-sys.md#getPointerSize-(System-API)) | Obtains the current mouse pointer size. This API uses a promise to return the result. |
| [getPointerSizeSync](arkts-input-pointer-getpointersizesync-f-sys.md#getPointerSizeSync) | Obtains the pointer size. This API returns the result synchronously. |
| [getPointerSpeed](arkts-input-pointer-getpointerspeed-f-sys.md#getPointerSpeed) | Obtains the mouse pointer speed. This API uses an asynchronous callback to return the result. |
| [getPointerSpeed](arkts-input-pointer-getpointerspeed-f-sys.md#getPointerSpeed-(System-API)) | Obtains the mouse pointer speed. This API uses a promise to return the result. |
| [getPointerSpeedSync](arkts-input-pointer-getpointerspeedsync-f-sys.md#getPointerSpeedSync) | Obtains the mouse pointer speed. This API returns the result synchronously. |
| [getTouchpadDoubleTapAndDragState](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md#getTouchpadDoubleTapAndDragState) | Obtains the touchpad double-tap and drag switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadDoubleTapAndDragState](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md#getTouchpadDoubleTapAndDragState-(System-API)) | Obtains the touchpad double-tap and drag switch state. This API uses a promise to return the result. |
| [getTouchpadPinchSwitch](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md#getTouchpadPinchSwitch) | Obtains the touchpad pinch switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadPinchSwitch](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md#getTouchpadPinchSwitch-(System-API)) | Obtains the touchpad pinch switch state. This API uses a promise to return the result. |
| [getTouchpadPointerSpeed](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md#getTouchpadPointerSpeed) | Obtains the touchpad pointer speed. This API uses an asynchronous callback to return the result. |
| [getTouchpadPointerSpeed](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md#getTouchpadPointerSpeed-(System-API)) | Obtains the touchpad pointer speed. This API uses a promise to return the result. |
| [getTouchpadRightClickType](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md#getTouchpadRightClickType) | Obtains the touchpad right-click menu type. This API uses an asynchronous callback to return the result. |
| [getTouchpadRightClickType](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md#getTouchpadRightClickType-(System-API)) | Obtains the touchpad right-click menu type. This API uses a promise to return the result. |
| [getTouchpadScrollDirection](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md#getTouchpadScrollDirection) | Obtains the touchpad scroll direction. This API uses an asynchronous callback to return the result. |
| [getTouchpadScrollDirection](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md#getTouchpadScrollDirection-(System-API)) | Obtains the scroll direction of the touchpad. This API uses a promise to return the result. |
| [getTouchpadScrollSwitch](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md#getTouchpadScrollSwitch) | Obtains the touchpad scroll switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadScrollSwitch](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md#getTouchpadScrollSwitch-(System-API)) | Obtains the touchpad scroll switch state. This API uses a promise to return the result. |
| [getTouchpadSwipeSwitch](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md#getTouchpadSwipeSwitch) | Obtains the touchpad multi-finger swipe switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadSwipeSwitch](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md#getTouchpadSwipeSwitch-(System-API)) | Obtains the touchpad multi-finger swipe switch state. This API uses a promise to return the result. |
| [getTouchpadTapSwitch](arkts-input-pointer-gettouchpadtapswitch-f-sys.md#getTouchpadTapSwitch) | Obtains the touchpad tap switch state. This API uses an asynchronous callback to return the result. |
| [getTouchpadTapSwitch](arkts-input-pointer-gettouchpadtapswitch-f-sys.md#getTouchpadTapSwitch-(System-API)) | Obtains the touchpad tap switch state. This API uses a promise to return the result. |
| [setHoverScrollState](arkts-input-pointer-sethoverscrollstate-f-sys.md#setHoverScrollState) | Sets the mouse hover scrolling switch state. This API uses an asynchronous callback to return the result. |
| [setHoverScrollState](arkts-input-pointer-sethoverscrollstate-f-sys.md#setHoverScrollState-(System-API)) | Sets the status of the mouse hover scroll switch. This API uses a promise to return the result. |
| [setMousePrimaryButton](arkts-input-pointer-setmouseprimarybutton-f-sys.md#setMousePrimaryButton) | Sets the primary mouse button. This API uses an asynchronous callback to return the result. |
| [setMousePrimaryButton](arkts-input-pointer-setmouseprimarybutton-f-sys.md#setMousePrimaryButton-(System-API)) | Sets the primary mouse button. This API uses a promise to return the result. |
| [setMouseScrollDirection](arkts-input-pointer-setmousescrolldirection-f-sys.md#setMouseScrollDirection) | Sets the scroll direction of the mouse wheel. This API uses a promise to return the result asynchronously. |
| [setMouseScrollRows](arkts-input-pointer-setmousescrollrows-f-sys.md#setMouseScrollRows) | Sets the number of mouse scroll lines. This API uses an asynchronous callback to return the result. |
| [setMouseScrollRows](arkts-input-pointer-setmousescrollrows-f-sys.md#setMouseScrollRows-(System-API)) | Sets the number of mouse scroll lines. This API uses a promise to return the result. |
| [setPointerColor](arkts-input-pointer-setpointercolor-f-sys.md#setPointerColor) | Sets the mouse pointer color. This API uses an asynchronous callback to return the result. > **NOTE：**> > When performing this operation, you need to connect an external device, such as a mouse or Bluetooth device. |
| [setPointerColor](arkts-input-pointer-setpointercolor-f-sys.md#setPointerColor-(System-API)) | Sets the mouse pointer color. This API uses a promise to return the result. > **NOTE：**> > When performing this operation, you need to connect an external device, such as a mouse or Bluetooth device. |
| [setPointerColorSync](arkts-input-pointer-setpointercolorsync-f-sys.md#setPointerColorSync) | Sets the pointer color. This API returns the result synchronously. > **NOTE：**> > When performing this operation, you need to connect an external device, such as a mouse or Bluetooth device. |
| [setPointerSize](arkts-input-pointer-setpointersize-f-sys.md#setPointerSize) | Sets the mouse pointer size. This API uses an asynchronous callback to return the result. |
| [setPointerSize](arkts-input-pointer-setpointersize-f-sys.md#setPointerSize-(System-API)) | Sets the mouse pointer size. This API uses a promise to return the result. |
| [setPointerSizeSync](arkts-input-pointer-setpointersizesync-f-sys.md#setPointerSizeSync) | Sets the pointer size. This API returns the result synchronously. |
| [setPointerSpeed](arkts-input-pointer-setpointerspeed-f-sys.md#setPointerSpeed) | Sets the mouse pointer speed. This API uses an asynchronous callback to return the result. |
| [setPointerSpeed](arkts-input-pointer-setpointerspeed-f-sys.md#setPointerSpeed-(System-API)) | Sets the mouse pointer speed. This API uses a promise to return the result. |
| [setPointerSpeedSync](arkts-input-pointer-setpointerspeedsync-f-sys.md#setPointerSpeedSync) | Sets the mouse pointer speed. This API returns the result synchronously. |
| [setTouchpadDoubleTapAndDragState](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md#setTouchpadDoubleTapAndDragState) | Sets the touchpad double-tap and drag switch state. This API uses an asynchronous callback to return the result. |
| [setTouchpadDoubleTapAndDragState](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md#setTouchpadDoubleTapAndDragState-(System-API)) | Sets the touchpad double-tap and drag switch state. This API uses a promise to return the result. |
| [setTouchpadPinchSwitch](arkts-input-pointer-settouchpadpinchswitch-f-sys.md#setTouchpadPinchSwitch) | Sets the touchpad pinch switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadPinchSwitch](arkts-input-pointer-settouchpadpinchswitch-f-sys.md#setTouchpadPinchSwitch-(System-API)) | Sets the touchpad pinch switch. This API uses a promise to return the result. |
| [setTouchpadPointerSpeed](arkts-input-pointer-settouchpadpointerspeed-f-sys.md#setTouchpadPointerSpeed) | Sets the touchpad pointer speed. This API uses an asynchronous callback to return the result. |
| [setTouchpadPointerSpeed](arkts-input-pointer-settouchpadpointerspeed-f-sys.md#setTouchpadPointerSpeed-(System-API)) | Sets the touchpad pointer speed. This API uses a promise to return the result. |
| [setTouchpadRightClickType](arkts-input-pointer-settouchpadrightclicktype-f-sys.md#setTouchpadRightClickType) | Sets the touchpad right-click menu type. This API uses an asynchronous callback to return the result. |
| [setTouchpadRightClickType](arkts-input-pointer-settouchpadrightclicktype-f-sys.md#setTouchpadRightClickType-(System-API)) | Sets the touchpad right-click menu type. This API uses a promise to return the result. |
| [setTouchpadScrollDirection](arkts-input-pointer-settouchpadscrolldirection-f-sys.md#setTouchpadScrollDirection) | Sets the touchpad scroll direction. This API uses an asynchronous callback to return the result. |
| [setTouchpadScrollDirection](arkts-input-pointer-settouchpadscrolldirection-f-sys.md#setTouchpadScrollDirection-(System-API)) | Sets the touchpad scroll direction. This API uses a promise to return the result. |
| [setTouchpadScrollSwitch](arkts-input-pointer-settouchpadscrollswitch-f-sys.md#setTouchpadScrollSwitch) | Sets the touchpad scroll switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadScrollSwitch](arkts-input-pointer-settouchpadscrollswitch-f-sys.md#setTouchpadScrollSwitch-(System-API)) | Sets the touchpad scroll switch. This API uses a promise to return the result. |
| [setTouchpadSwipeSwitch](arkts-input-pointer-settouchpadswipeswitch-f-sys.md#setTouchpadSwipeSwitch) | Sets the touchpad multi-finger swipe switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadSwipeSwitch](arkts-input-pointer-settouchpadswipeswitch-f-sys.md#setTouchpadSwipeSwitch-(System-API)) | Sets the touchpad multi-finger swipe switch. This API uses a promise to return the result. |
| [setTouchpadTapSwitch](arkts-input-pointer-settouchpadtapswitch-f-sys.md#setTouchpadTapSwitch) | Sets the touchpad tap switch. This API uses an asynchronous callback to return the result. |
| [setTouchpadTapSwitch](arkts-input-pointer-settouchpadtapswitch-f-sys.md#setTouchpadTapSwitch-(System-API)) | Sets the touchpad tap switch. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CursorConfig](arkts-input-pointer-cursorconfig-i.md) | Defines custom cursor configuration. |
| [CustomCursor](arkts-input-pointer-customcursor-i.md) | Defines custom cursor resources. |

### Enums

| Name | Description |
| --- | --- |
| [PointerStyle](arkts-input-pointer-pointerstyle-e.md) | Mouse pointer style types. |
| [PrimaryButton](arkts-input-pointer-primarybutton-e.md) | Type of the primary mouse button. |
| [RightClickType](arkts-input-pointer-rightclicktype-e.md) | Enumerates shortcut menu triggering modes. |

