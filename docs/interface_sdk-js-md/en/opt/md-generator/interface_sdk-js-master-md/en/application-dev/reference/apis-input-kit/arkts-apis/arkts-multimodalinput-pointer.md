# @ohos.multimodalInput.pointer(Mouse Pointer)

The **pointer** module provides APIs related to pointer attribute management, such as querying and setting pointer attributes.

**Since:** 9

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
| [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getpointerstyle) |
| [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getpointerstyle-1) |
| [getPointerStyleSync](arkts-input-pointer-getpointerstylesync-f.md#getpointerstylesync) |
| [isPointerVisible](arkts-input-pointer-ispointervisible-f.md#ispointervisible) |
| [isPointerVisible](arkts-input-pointer-ispointervisible-f.md#ispointervisible-1) |
| [isPointerVisibleSync](arkts-input-pointer-ispointervisiblesync-f.md#ispointervisiblesync) |
| [setCustomCursor](arkts-input-pointer-setcustomcursor-f.md#setcustomcursor) |
| [setCustomCursor](arkts-input-pointer-setcustomcursor-f.md#setcustomcursor-1) |
| [setCustomCursorSync](arkts-input-pointer-setcustomcursorsync-f.md#setcustomcursorsync) |
| [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md#setpointerstyle) |
| [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md#setpointerstyle-1) |
| [setPointerStyleSync](arkts-input-pointer-setpointerstylesync-f.md#setpointerstylesync) |
| [setPointerVisible](arkts-input-pointer-setpointervisible-f.md#setpointervisible) |
| [setPointerVisible](arkts-input-pointer-setpointervisible-f.md#setpointervisible-1) |
| [setPointerVisibleSync](arkts-input-pointer-setpointervisiblesync-f.md#setpointervisiblesync) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getHoverScrollState](arkts-input-pointer-gethoverscrollstate-f-sys.md#gethoverscrollstate) |
| [getHoverScrollState](arkts-input-pointer-gethoverscrollstate-f-sys.md#gethoverscrollstate-1) |
| [getMousePrimaryButton](arkts-input-pointer-getmouseprimarybutton-f-sys.md#getmouseprimarybutton) |
| [getMousePrimaryButton](arkts-input-pointer-getmouseprimarybutton-f-sys.md#getmouseprimarybutton-1) |
| [getMouseScrollDirection](arkts-input-pointer-getmousescrolldirection-f-sys.md#getmousescrolldirection) |
| [getMouseScrollRows](arkts-input-pointer-getmousescrollrows-f-sys.md#getmousescrollrows) |
| [getMouseScrollRows](arkts-input-pointer-getmousescrollrows-f-sys.md#getmousescrollrows-1) |
| [getPointerColor](arkts-input-pointer-getpointercolor-f-sys.md#getpointercolor) |
| [getPointerColor](arkts-input-pointer-getpointercolor-f-sys.md#getpointercolor-1) |
| [getPointerColorSync](arkts-input-pointer-getpointercolorsync-f-sys.md#getpointercolorsync) |
| [getPointerSize](arkts-input-pointer-getpointersize-f-sys.md#getpointersize) |
| [getPointerSize](arkts-input-pointer-getpointersize-f-sys.md#getpointersize-1) |
| [getPointerSizeSync](arkts-input-pointer-getpointersizesync-f-sys.md#getpointersizesync) |
| [getPointerSpeed](arkts-input-pointer-getpointerspeed-f-sys.md#getpointerspeed) |
| [getPointerSpeed](arkts-input-pointer-getpointerspeed-f-sys.md#getpointerspeed-1) |
| [getPointerSpeedSync](arkts-input-pointer-getpointerspeedsync-f-sys.md#getpointerspeedsync) |
| [getTouchpadDoubleTapAndDragState](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md#gettouchpaddoubletapanddragstate) |
| [getTouchpadDoubleTapAndDragState](arkts-input-pointer-gettouchpaddoubletapanddragstate-f-sys.md#gettouchpaddoubletapanddragstate-1) |
| [getTouchpadPinchSwitch](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md#gettouchpadpinchswitch) |
| [getTouchpadPinchSwitch](arkts-input-pointer-gettouchpadpinchswitch-f-sys.md#gettouchpadpinchswitch-1) |
| [getTouchpadPointerSpeed](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md#gettouchpadpointerspeed) |
| [getTouchpadPointerSpeed](arkts-input-pointer-gettouchpadpointerspeed-f-sys.md#gettouchpadpointerspeed-1) |
| [getTouchpadRightClickType](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md#gettouchpadrightclicktype) |
| [getTouchpadRightClickType](arkts-input-pointer-gettouchpadrightclicktype-f-sys.md#gettouchpadrightclicktype-1) |
| [getTouchpadScrollDirection](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md#gettouchpadscrolldirection) |
| [getTouchpadScrollDirection](arkts-input-pointer-gettouchpadscrolldirection-f-sys.md#gettouchpadscrolldirection-1) |
| [getTouchpadScrollSwitch](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md#gettouchpadscrollswitch) |
| [getTouchpadScrollSwitch](arkts-input-pointer-gettouchpadscrollswitch-f-sys.md#gettouchpadscrollswitch-1) |
| [getTouchpadSwipeSwitch](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md#gettouchpadswipeswitch) |
| [getTouchpadSwipeSwitch](arkts-input-pointer-gettouchpadswipeswitch-f-sys.md#gettouchpadswipeswitch-1) |
| [getTouchpadTapSwitch](arkts-input-pointer-gettouchpadtapswitch-f-sys.md#gettouchpadtapswitch) |
| [getTouchpadTapSwitch](arkts-input-pointer-gettouchpadtapswitch-f-sys.md#gettouchpadtapswitch-1) |
| [setHoverScrollState](arkts-input-pointer-sethoverscrollstate-f-sys.md#sethoverscrollstate) |
| [setHoverScrollState](arkts-input-pointer-sethoverscrollstate-f-sys.md#sethoverscrollstate-1) |
| [setMousePrimaryButton](arkts-input-pointer-setmouseprimarybutton-f-sys.md#setmouseprimarybutton) |
| [setMousePrimaryButton](arkts-input-pointer-setmouseprimarybutton-f-sys.md#setmouseprimarybutton-1) |
| [setMouseScrollDirection](arkts-input-pointer-setmousescrolldirection-f-sys.md#setmousescrolldirection) |
| [setMouseScrollRows](arkts-input-pointer-setmousescrollrows-f-sys.md#setmousescrollrows) |
| [setMouseScrollRows](arkts-input-pointer-setmousescrollrows-f-sys.md#setmousescrollrows-1) |
| [setPointerColor](arkts-input-pointer-setpointercolor-f-sys.md#setpointercolor) |
| [setPointerColor](arkts-input-pointer-setpointercolor-f-sys.md#setpointercolor-1) |
| [setPointerColorSync](arkts-input-pointer-setpointercolorsync-f-sys.md#setpointercolorsync) |
| [setPointerSize](arkts-input-pointer-setpointersize-f-sys.md#setpointersize) |
| [setPointerSize](arkts-input-pointer-setpointersize-f-sys.md#setpointersize-1) |
| [setPointerSizeSync](arkts-input-pointer-setpointersizesync-f-sys.md#setpointersizesync) |
| [setPointerSpeed](arkts-input-pointer-setpointerspeed-f-sys.md#setpointerspeed) |
| [setPointerSpeed](arkts-input-pointer-setpointerspeed-f-sys.md#setpointerspeed-1) |
| [setPointerSpeedSync](arkts-input-pointer-setpointerspeedsync-f-sys.md#setpointerspeedsync) |
| [setTouchpadDoubleTapAndDragState](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md#settouchpaddoubletapanddragstate) |
| [setTouchpadDoubleTapAndDragState](arkts-input-pointer-settouchpaddoubletapanddragstate-f-sys.md#settouchpaddoubletapanddragstate-1) |
| [setTouchpadPinchSwitch](arkts-input-pointer-settouchpadpinchswitch-f-sys.md#settouchpadpinchswitch) |
| [setTouchpadPinchSwitch](arkts-input-pointer-settouchpadpinchswitch-f-sys.md#settouchpadpinchswitch-1) |
| [setTouchpadPointerSpeed](arkts-input-pointer-settouchpadpointerspeed-f-sys.md#settouchpadpointerspeed) |
| [setTouchpadPointerSpeed](arkts-input-pointer-settouchpadpointerspeed-f-sys.md#settouchpadpointerspeed-1) |
| [setTouchpadRightClickType](arkts-input-pointer-settouchpadrightclicktype-f-sys.md#settouchpadrightclicktype) |
| [setTouchpadRightClickType](arkts-input-pointer-settouchpadrightclicktype-f-sys.md#settouchpadrightclicktype-1) |
| [setTouchpadScrollDirection](arkts-input-pointer-settouchpadscrolldirection-f-sys.md#settouchpadscrolldirection) |
| [setTouchpadScrollDirection](arkts-input-pointer-settouchpadscrolldirection-f-sys.md#settouchpadscrolldirection-1) |
| [setTouchpadScrollSwitch](arkts-input-pointer-settouchpadscrollswitch-f-sys.md#settouchpadscrollswitch) |
| [setTouchpadScrollSwitch](arkts-input-pointer-settouchpadscrollswitch-f-sys.md#settouchpadscrollswitch-1) |
| [setTouchpadSwipeSwitch](arkts-input-pointer-settouchpadswipeswitch-f-sys.md#settouchpadswipeswitch) |
| [setTouchpadSwipeSwitch](arkts-input-pointer-settouchpadswipeswitch-f-sys.md#settouchpadswipeswitch-1) |
| [setTouchpadTapSwitch](arkts-input-pointer-settouchpadtapswitch-f-sys.md#settouchpadtapswitch) |
| [setTouchpadTapSwitch](arkts-input-pointer-settouchpadtapswitch-f-sys.md#settouchpadtapswitch-1) |
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
