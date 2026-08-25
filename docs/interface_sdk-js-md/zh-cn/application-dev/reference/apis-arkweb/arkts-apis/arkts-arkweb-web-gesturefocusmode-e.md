# GestureFocusMode

Enum type supplied to [gestureFocusMode](arkts-arkweb-web-webattribute-i.md#gesturefocusmode) for setting the web gesture focus mode.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## DEFAULT

```TypeScript
DEFAULT = 0
```

Any action on a web component, such as tapping, long-pressing, scrolling, zooming, etc., will cause the web component to acquire focus on touch down.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## GESTURE_TAP_AND_LONG_PRESS

```TypeScript
GESTURE_TAP_AND_LONG_PRESS = 1
```

Tap and long-press gestures will cause the web component to acquire focus after touch up, while gestures such as scrolling, zooming, etc., do not request focus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core
