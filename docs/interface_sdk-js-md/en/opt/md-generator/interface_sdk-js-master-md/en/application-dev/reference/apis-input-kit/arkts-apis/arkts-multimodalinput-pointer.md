# @ohos.multimodalInput.pointer

The **pointer** module provides APIs related to pointer attribute management, such as querying and setting pointer attributes.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace pointer--><!--Device-unnamed-declare namespace pointer-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getPointerStyle) |
| [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getPointerStyle) |
| [getPointerStyleSync](arkts-input-pointer-getpointerstylesync-f.md#getPointerStyleSync) |
| [isPointerVisible](arkts-input-pointer-ispointervisible-f.md#isPointerVisible) |
| [isPointerVisible](arkts-input-pointer-ispointervisible-f.md#isPointerVisible) |
| [isPointerVisibleSync](arkts-input-pointer-ispointervisiblesync-f.md#isPointerVisibleSync) |
| [setCustomCursor](arkts-input-pointer-setcustomcursor-f.md#setCustomCursor) |
| [setCustomCursor](arkts-input-pointer-setcustomcursor-f.md#setCustomCursor) |
| [setCustomCursorSync](arkts-input-pointer-setcustomcursorsync-f.md#setCustomCursorSync) |
| [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md#setPointerStyle) |
| [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md#setPointerStyle) |
| [setPointerStyleSync](arkts-input-pointer-setpointerstylesync-f.md#setPointerStyleSync) |
| [setPointerVisible](arkts-input-pointer-setpointervisible-f.md#setPointerVisible) |
| [setPointerVisible](arkts-input-pointer-setpointervisible-f.md#setPointerVisible) |
| [setPointerVisibleSync](arkts-input-pointer-setpointervisiblesync-f.md#setPointerVisibleSync) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getHoverScrollState](arkts-input-pointer-gethoverscrollstate-f-sys.md#getHoverScrollState-(System-API)) |
| [getHoverScrollState](arkts-input-pointer-gethoverscrollstate-f-sys.md#getHoverScrollState-(System-API)) |
| [getMousePrimaryButton](arkts-input-pointer-getmouseprimarybutton-f-sys.md#getMousePrimaryButton-(System-API)) |
| [getMousePrimaryButton](arkts-input-pointer-getmouseprimarybutton-f-sys.md#getMousePrimaryButton-(System-API)) |
| [getMouseScrollDirection](arkts-input-pointer-getmousescrolldirection-f-sys.md#getMouseScrollDirection-(System-API)) |
| [getMouseScrollRows](arkts-input-pointer-getmousescrollrows-f-sys.md#getMouseScrollRows-(System-API)) |
| [getMouseScrollRows](arkts-input-pointer-getmousescrollrows-f-sys.md#getMouseScrollRows-(System-API)) |
| [getPointerColor](arkts-input-pointer-getpointercolor-f-sys.md#getPointerColor-(System-API)) |
| [getPointerColor](arkts-input-pointer-getpointercolor-f-sys.md#getPointerColor-(System-API)) |
| [getPointerColorSync](arkts-input-pointer-getpointercolorsync-f-sys.md#getPointerColorSync-(System-API)) |
| [getPointerSize](arkts-input-pointer-getpointersize-f-sys.md#getPointerSize-(System-API)) |
| [getPointerSize](arkts-input-pointer-getpointersize-f-sys.md#getPointerSize-(System-API)) |
| [getPointerSizeSync](arkts-input-pointer-getpointersizesync-f-sys.md#getPointerSizeSync-(System-API)) |
| [getPointerSpeed](arkts-input-pointer-getpointerspeed-f-sys.md#getPointerSpeed-(System-API)) |
| [getPointerSpeed](arkts-input-pointer-getpointerspeed-f-sys.md#getPointerSpeed-(System-API)) |
| [getPointerSpeedSync](arkts-input-pointer-getpointerspeedsync-f-sys.md#getPointerSpeedSync-(System-API)) |
| [getTouchpadDoubleTapAndDragState](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md#getTouchpadDoubleTapAndDragState-(System-API)) |
| [getTouchpadDoubleTapAndDragState](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md#getTouchpadDoubleTapAndDragState-(System-API)) |
| [getTouchpadPinchSwitch](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md#getTouchpadPinchSwitch-(System-API)) |
| [getTouchpadPinchSwitch](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md#getTouchpadPinchSwitch-(System-API)) |
| [getTouchpadPointerSpeed](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md#getTouchpadPointerSpeed-(System-API)) |
| [getTouchpadPointerSpeed](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md#getTouchpadPointerSpeed-(System-API)) |
| [getTouchpadRightClickType](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md#getTouchpadRightClickType-(System-API)) |
| [getTouchpadRightClickType](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md#getTouchpadRightClickType-(System-API)) |
| [getTouchpadScrollDirection](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md#getTouchpadScrollDirection-(System-API)) |
| [getTouchpadScrollDirection](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md#getTouchpadScrollDirection-(System-API)) |
| [getTouchpadScrollSwitch](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md#getTouchpadScrollSwitch-(System-API)) |
| [getTouchpadScrollSwitch](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md#getTouchpadScrollSwitch-(System-API)) |
| [getTouchpadSwipeSwitch](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md#getTouchpadSwipeSwitch-(System-API)) |
| [getTouchpadSwipeSwitch](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md#getTouchpadSwipeSwitch-(System-API)) |
| [getTouchpadTapSwitch](arkts-input-pointer-gettouchpadtapswitch-f-sys.md#getTouchpadTapSwitch-(System-API)) |
| [getTouchpadTapSwitch](arkts-input-pointer-gettouchpadtapswitch-f-sys.md#getTouchpadTapSwitch-(System-API)) |
| [setHoverScrollState](arkts-input-pointer-sethoverscrollstate-f-sys.md#setHoverScrollState-(System-API)) |
| [setHoverScrollState](arkts-input-pointer-sethoverscrollstate-f-sys.md#setHoverScrollState-(System-API)) |
| [setMousePrimaryButton](arkts-input-pointer-setmouseprimarybutton-f-sys.md#setMousePrimaryButton-(System-API)) |
| [setMousePrimaryButton](arkts-input-pointer-setmouseprimarybutton-f-sys.md#setMousePrimaryButton-(System-API)) |
| [setMouseScrollDirection](arkts-input-pointer-setmousescrolldirection-f-sys.md#setMouseScrollDirection-(System-API)) |
| [setMouseScrollRows](arkts-input-pointer-setmousescrollrows-f-sys.md#setMouseScrollRows-(System-API)) |
| [setMouseScrollRows](arkts-input-pointer-setmousescrollrows-f-sys.md#setMouseScrollRows-(System-API)) |
| [setPointerColor](arkts-input-pointer-setpointercolor-f-sys.md#setPointerColor-(System-API)) |
| [setPointerColor](arkts-input-pointer-setpointercolor-f-sys.md#setPointerColor-(System-API)) |
| [setPointerColorSync](arkts-input-pointer-setpointercolorsync-f-sys.md#setPointerColorSync-(System-API)) |
| [setPointerSize](arkts-input-pointer-setpointersize-f-sys.md#setPointerSize-(System-API)) |
| [setPointerSize](arkts-input-pointer-setpointersize-f-sys.md#setPointerSize-(System-API)) |
| [setPointerSizeSync](arkts-input-pointer-setpointersizesync-f-sys.md#setPointerSizeSync-(System-API)) |
| [setPointerSpeed](arkts-input-pointer-setpointerspeed-f-sys.md#setPointerSpeed-(System-API)) |
| [setPointerSpeed](arkts-input-pointer-setpointerspeed-f-sys.md#setPointerSpeed-(System-API)) |
| [setPointerSpeedSync](arkts-input-pointer-setpointerspeedsync-f-sys.md#setPointerSpeedSync-(System-API)) |
| [setTouchpadDoubleTapAndDragState](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md#setTouchpadDoubleTapAndDragState-(System-API)) |
| [setTouchpadDoubleTapAndDragState](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md#setTouchpadDoubleTapAndDragState-(System-API)) |
| [setTouchpadPinchSwitch](arkts-input-pointer-settouchpadpinchswitch-f-sys.md#setTouchpadPinchSwitch-(System-API)) |
| [setTouchpadPinchSwitch](arkts-input-pointer-settouchpadpinchswitch-f-sys.md#setTouchpadPinchSwitch-(System-API)) |
| [setTouchpadPointerSpeed](arkts-input-pointer-settouchpadpointerspeed-f-sys.md#setTouchpadPointerSpeed-(System-API)) |
| [setTouchpadPointerSpeed](arkts-input-pointer-settouchpadpointerspeed-f-sys.md#setTouchpadPointerSpeed-(System-API)) |
| [setTouchpadRightClickType](arkts-input-pointer-settouchpadrightclicktype-f-sys.md#setTouchpadRightClickType-(System-API)) |
| [setTouchpadRightClickType](arkts-input-pointer-settouchpadrightclicktype-f-sys.md#setTouchpadRightClickType-(System-API)) |
| [setTouchpadScrollDirection](arkts-input-pointer-settouchpadscrolldirection-f-sys.md#setTouchpadScrollDirection-(System-API)) |
| [setTouchpadScrollDirection](arkts-input-pointer-settouchpadscrolldirection-f-sys.md#setTouchpadScrollDirection-(System-API)) |
| [setTouchpadScrollSwitch](arkts-input-pointer-settouchpadscrollswitch-f-sys.md#setTouchpadScrollSwitch-(System-API)) |
| [setTouchpadScrollSwitch](arkts-input-pointer-settouchpadscrollswitch-f-sys.md#setTouchpadScrollSwitch-(System-API)) |
| [setTouchpadSwipeSwitch](arkts-input-pointer-settouchpadswipeswitch-f-sys.md#setTouchpadSwipeSwitch-(System-API)) |
| [setTouchpadSwipeSwitch](arkts-input-pointer-settouchpadswipeswitch-f-sys.md#setTouchpadSwipeSwitch-(System-API)) |
| [setTouchpadTapSwitch](arkts-input-pointer-settouchpadtapswitch-f-sys.md#setTouchpadTapSwitch-(System-API)) |
| [setTouchpadTapSwitch](arkts-input-pointer-settouchpadtapswitch-f-sys.md#setTouchpadTapSwitch-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CursorConfig](arkts-input-pointer-cursorconfig-i.md) |
| [CustomCursor](arkts-input-pointer-customcursor-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PointerStyle](arkts-input-pointer-pointerstyle-e.md) |
| [PrimaryButton](arkts-input-pointer-primarybutton-e.md) |
| [RightClickType](arkts-input-pointer-rightclicktype-e.md) |
