# Font

设置文本样式。

> **说明：**
> 
> 可以使用[loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md/arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync)注册自定义字体。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface Font--><!--Device-unnamed-export declare interface Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## family

```TypeScript
family?: string | Resource
```

字体列表。

使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-family?: string | Resource--><!--Device-Font-family?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: Length
```

设置文本尺寸，Length为number类型时，使用fp单位。不支持设置百分比字符串。

默认值：16.0

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-size?: Length--><!--Device-Font-size?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: FontStyle
```

设置文本的字体样式。

默认值：FontStyle.Normal

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-style?: FontStyle--><!--Device-Font-style?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## weight

```TypeScript
weight?: FontWeight | int | string
```

设置文本的字体粗细，number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。

默认值：400 | FontWeight.Normal

**Type:** [FontWeight](arkts-arkui-fontweight-e.md) \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-weight?: FontWeight | int | string--><!--Device-Font-weight?: FontWeight | int | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

