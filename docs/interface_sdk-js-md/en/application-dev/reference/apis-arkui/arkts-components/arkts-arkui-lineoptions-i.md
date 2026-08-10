# LineOptions

用于描述Line组件绘制属性。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface LineOptions--><!--Device-unnamed-interface LineOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Length
```

高度。

值为异常值或缺省时，根据startPoint和endPoint自动计算所需的绘制区域高度。

默认单位：vp

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineOptions-height?: Length--><!--Device-LineOptions-height?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Length
```

宽度。

值为异常值或缺省时，根据startPoint和endPoint自动计算所需的绘制区域宽度。

默认单位：vp

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineOptions-width?: Length--><!--Device-LineOptions-width?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

