# GestureFocusMode

Enum type supplied to gestureFocusMode for setting the web gesture focus mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum GestureFocusMode--><!--Device-unnamed-export declare enum GestureFocusMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## DEFAULT

```TypeScript
DEFAULT = 0
```

Any action on a web component, such as tapping, long-pressing, scrolling, zooming, etc., will cause the web component to acquire focus on touch down.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-GestureFocusMode-DEFAULT = 0--><!--Device-GestureFocusMode-DEFAULT = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## GESTURE_TAP_AND_LONG_PRESS

```TypeScript
GESTURE_TAP_AND_LONG_PRESS = 1
```

Tap and long-press gestures will cause the web component to acquire focus after touch up, while gestures such as scrolling, zooming, etc., do not request focus.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-GestureFocusMode-GESTURE_TAP_AND_LONG_PRESS = 1--><!--Device-GestureFocusMode-GESTURE_TAP_AND_LONG_PRESS = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

