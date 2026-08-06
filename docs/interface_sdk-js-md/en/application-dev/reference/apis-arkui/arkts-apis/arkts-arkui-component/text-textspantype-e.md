# TextSpanType

Defines span type.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The order for menu type matching is as follows.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_When the user interacts with text, the system follows this order to decides which type of menu to display.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_Check whether a menu is registered for TextSpanType.TEXT and TextResponseType.LONG\_PRESS.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_Check whether a menu is registered for TextSpanType.TEXT and TextResponseType.DEFAULT.\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_Check whether a menu is registered for TextSpanType.DEFAULT and TextResponseType.LONG\_PRESS.\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_Check whether a menu is registered for TextSpanType.DEFAULT and TextResponseType.DEFAULT.\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum TextSpanType--><!--Device-unnamed-export declare enum TextSpanType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TEXT

```TypeScript
TEXT = 0
```

Only contains text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextSpanType-TEXT = 0--><!--Device-TextSpanType-TEXT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMAGE

```TypeScript
IMAGE = 1
```

Only contains image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextSpanType-IMAGE = 1--><!--Device-TextSpanType-IMAGE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MIXED

```TypeScript
MIXED = 2
```

Contains both text and image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextSpanType-MIXED = 2--><!--Device-TextSpanType-MIXED = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 3
```

When no other types are explicitly specified, this type will be matched.When this type is registered but TEXT, IMAGE, or MIXED types are not registered,this type will be triggered and displayed for those registered types.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextSpanType-DEFAULT = 3--><!--Device-TextSpanType-DEFAULT = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

