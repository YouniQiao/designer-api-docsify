# TextResponseType

ResponseType for contextMenu &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The order for menu type matching is as follows. When the user interacts with text, the system follows this order to decides which type of menu to display. &lt;ol&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.TEXT and TextResponseType.LONG_PRESS.&lt;/li&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.TEXT and TextResponseType.DEFAULT.&lt;/li&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.DEFAULT and TextResponseType.LONG_PRESS.&lt;/li&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.DEFAULT and TextResponseType.DEFAULT.&lt;/li&gt; &lt;/ol&gt; &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare enum TextResponseType--><!--Device-unnamed-export declare enum TextResponseType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT_CLICK

```TypeScript
RIGHT_CLICK = 0
```

Right click.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextResponseType-RIGHT_CLICK = 0--><!--Device-TextResponseType-RIGHT_CLICK = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LONG_PRESS

```TypeScript
LONG_PRESS = 1
```

Long press.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextResponseType-LONG_PRESS = 1--><!--Device-TextResponseType-LONG_PRESS = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELECT

```TypeScript
SELECT = 2
```

Selected by mouse.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextResponseType-SELECT = 2--><!--Device-TextResponseType-SELECT = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 3
```

When no other types are explicitly specified, this type will be matched. When this type is registered but RIGHT_CLICK, LONG_PRESS, or SELECT types are not registered, this type will be triggered and displayed for right-click, long press, and mouse selection actions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextResponseType-DEFAULT = 3--><!--Device-TextResponseType-DEFAULT = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

