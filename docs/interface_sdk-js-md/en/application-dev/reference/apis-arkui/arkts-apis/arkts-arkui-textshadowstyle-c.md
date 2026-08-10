# TextShadowStyle

文本阴影对象说明。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class TextShadowStyle--><!--Device-unnamed-declare class TextShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: ShadowOptions | Array<ShadowOptions>)
```

文本阴影对象的构造函数。

ShadowOptions对象中不支持fill字段。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextShadowStyle-constructor(value: ShadowOptions | Array<ShadowOptions>)--><!--Device-TextShadowStyle-constructor(value: ShadowOptions | Array<ShadowOptions>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ShadowOptions](arkts-arkui-common-shadowoptions-i.md) \| Array&lt;ShadowOptions&gt; | Yes | 文本阴影设置项。 |

## textShadow

```TypeScript
readonly textShadow: Array<ShadowOptions>
```

获取属性字符串的文本阴影。

**Type:** Array&lt;ShadowOptions&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextShadowStyle-readonly textShadow: Array<ShadowOptions>--><!--Device-TextShadowStyle-readonly textShadow: Array<ShadowOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

