# BackgroundColorStyle

文本背景颜色对象说明。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare class BackgroundColorStyle--><!--Device-unnamed-declare class BackgroundColorStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(textBackgroundStyle: TextBackgroundStyle)
```

文本背景颜色的构造函数。未通过该接口设置时，默认背景颜色为Color.Transparent，圆角为0。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-BackgroundColorStyle-constructor(textBackgroundStyle: TextBackgroundStyle)--><!--Device-BackgroundColorStyle-constructor(textBackgroundStyle: TextBackgroundStyle)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textBackgroundStyle | [TextBackgroundStyle](arkts-arkui-span-textbackgroundstyle-i.md) | Yes | 文本背景色设置项。 |

## textBackgroundStyle

```TypeScript
readonly textBackgroundStyle: TextBackgroundStyle
```

获取属性字符串的文本背景颜色。

默认值：

{

color: Color.Transparent,

radius: 0

}

**Type:** [TextBackgroundStyle](arkts-arkui-span-textbackgroundstyle-i.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-BackgroundColorStyle-readonly textBackgroundStyle: TextBackgroundStyle--><!--Device-BackgroundColorStyle-readonly textBackgroundStyle: TextBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

