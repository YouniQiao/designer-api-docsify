# PathOptions

用于描述Path组件绘制属性。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface PathOptions--><!--Device-unnamed-declare interface PathOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## commands

```TypeScript
commands?: ResourceStr
```

路径绘制的命令字符串，符合[SVG路径描述规范](../../../reference/apis-arkui/arkui-ts/ts-drawing-components-path.md#svg路径描述规范)，单位为px。

默认值：空字符串

异常值按照默认值处理。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-PathOptions-commands?: ResourceStr--><!--Device-PathOptions-commands?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Length
```

路径所在矩形的高度。取值范围≥0。

值为异常值或缺省时按照路径内容自动计算高度。

默认单位：vp

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-PathOptions-height?: Length--><!--Device-PathOptions-height?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Length
```

路径所在矩形的宽度。取值范围≥0。

值为异常值或缺省时按照路径内容自动计算宽度。

默认单位：vp

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-PathOptions-width?: Length--><!--Device-PathOptions-width?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

