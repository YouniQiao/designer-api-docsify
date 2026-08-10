# StackOptions

设置堆叠容器的子组件对齐方式。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface StackOptions--><!--Device-unnamed-declare interface StackOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignContent

```TypeScript
alignContent?: Alignment
```

设置子组件在容器内的对齐方式。该属性与接口的构造入参同时设置时，以属性设置的值为准。

默认值：Alignment.Center 

非法值：按默认值处理。

**说明：** 该参数与[align](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#align)同时设置时，后设置的属性值会覆盖先设置的属性值。

**Type:** [Alignment](../arkts-apis/arkts-arkui-alignment-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-StackOptions-alignContent?: Alignment--><!--Device-StackOptions-alignContent?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

