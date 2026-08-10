# Circle

用于绘制圆形的组件。 

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 子组件

无

## Circle

```TypeScript
Circle(value?: CircleOptions)
```

use new function to set the value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CircleInterface-new (value?: CircleOptions): CircleAttribute--><!--Device-CircleInterface-new (value?: CircleOptions): CircleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CircleOptions](arkts-arkui-circleoptions-i.md) | No |  |

## Circle

```TypeScript
Circle(value?: CircleOptions)
```

用于绘制圆形的构造函数。调用后创建一个Circle对象，可设置宽高属性。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CircleInterface-(value?: CircleOptions): CircleAttribute--><!--Device-CircleInterface-(value?: CircleOptions): CircleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CircleOptions](arkts-arkui-circleoptions-i.md) | No | 设置圆形尺寸。当需要自定义圆形大小时传入此参数，不传入时width和height默认为0。 <br>异常值undefined和null按照无效值处理，本次设置不生效。 |

## Summary

- [CircleOptions](arkts-arkui-circle-circleoptions-i.md)
