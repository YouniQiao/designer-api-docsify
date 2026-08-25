# TextSpanType

Defines span type.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The order for menu type matching is as follows. <br>When the user interacts with text, the system follows this order to decides which type of menu to display. &lt;ol&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.TEXT and TextResponseType.LONG_PRESS.&lt;/li&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.TEXT and TextResponseType.DEFAULT.&lt;/li&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.DEFAULT and TextResponseType.LONG_PRESS.&lt;/li&gt; &lt;li&gt;Check whether a menu is registered for TextSpanType.DEFAULT and TextResponseType.DEFAULT.&lt;/li&gt; &lt;/ol&gt; </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TEXT

```TypeScript
TEXT = 0
```

Only contains text.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMAGE

```TypeScript
IMAGE = 1
```

Only contains image.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MIXED

```TypeScript
MIXED = 2
```

Contains both text and image.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 3
```

When no other types are explicitly specified, this type will be matched. When this type is registered but TEXT, IMAGE, or MIXED types are not registered, this type will be triggered and displayed for those registered types.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
