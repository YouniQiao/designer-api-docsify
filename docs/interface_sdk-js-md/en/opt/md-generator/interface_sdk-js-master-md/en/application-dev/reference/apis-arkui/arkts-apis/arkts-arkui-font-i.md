# Font

Sets the text style.

**Since:** 7

<!--Device-unnamed-declare interface Font--><!--Device-unnamed-declare interface Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## family

```TypeScript
family?: string | Resource
```

Font family. &lt;br&gt;To specify multiple fonts, separate them with commas (,), and fonts are applied in priority order.Example: **'Arial, HarmonyOS Sans'**.Default value: 'HarmonyOS Sans'.

**Type:** string \| Resource

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Font-family?: string | Resource--><!--Device-Font-family?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: Length
```

Font size. If the value is of the number type, the unit fp is used. Percentage strings are not supported.Default value: 16fp.

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Font-size?: Length--><!--Device-Font-size?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: FontStyle
```

Font style.Default value: FontStyle.Normal.

**Type:** [FontStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontstyle-e.md)

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Font-style?: FontStyle--><!--Device-Font-style?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## weight

```TypeScript
weight?: FontWeight | number | string
```

Font weight. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a thicker font.Default value: FontWeight.Normal.

**Type:** [FontWeight](arkts-arkui-fontweight-e.md) \| number \| string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Font-weight?: FontWeight | number | string--><!--Device-Font-weight?: FontWeight | number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
