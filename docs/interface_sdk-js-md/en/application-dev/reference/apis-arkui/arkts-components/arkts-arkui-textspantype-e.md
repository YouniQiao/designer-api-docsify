# TextSpanType

[Span](../arkts-apis/arkts-arkui-span-span-f.md/arkts-arkui-span-span-f.md#span)类型信息。

> **说明：**
> 
> 菜单类型的匹配顺序如下。例如，用户长按文本时，根据以下规则查找：
> 
> 1. 查找是否注册了TextSpanType.TEXT、TextResponseType.LONG_PRESS菜单
> 
> 2. 查找是否注册了TextSpanType.TEXT、TextResponseType.DEFAULT菜单
> 
> 3. 查找是否注册了TextSpanType.DEFAULT、TextResponseType.LONG_PRESS菜单
> 
> 4. 查找是否注册了TextSpanType.DEFAULT、TextResponseType.DEFAULT菜单

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum TextSpanType--><!--Device-unnamed-declare enum TextSpanType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TEXT

```TypeScript
TEXT = 0
```

Span为文字类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextSpanType-TEXT = 0--><!--Device-TextSpanType-TEXT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMAGE

```TypeScript
IMAGE = 1
```

Span为图像类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextSpanType-IMAGE = 1--><!--Device-TextSpanType-IMAGE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MIXED

```TypeScript
MIXED = 2
```

Span为图文混合类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextSpanType-MIXED = 2--><!--Device-TextSpanType-MIXED = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 3
```

注册此类型菜单但未注册TEXT、IMAGE、MIXED菜单时，文字类型、图片类型、图文混合类型都会触发并显示此类型对应的菜单。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextSpanType-DEFAULT = 3--><!--Device-TextSpanType-DEFAULT = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

