# Circle

## Circle

```TypeScript
export declare function Circle(
    options?: CircleOptions
): CircleAttribute
```

用于绘制圆形的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Circle(    options?: CircleOptions): CircleAttribute--><!--Device-unnamed-export declare function Circle(    options?: CircleOptions): CircleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CircleOptions](../arkts-components/arkts-arkui-circleoptions-i.md) | No | 设置圆形尺寸。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CircleAttribute](../arkts-components/arkts-arkui-circle-attribute.md) | Circle的属性。 |


## Circle

```TypeScript
export declare function Circle(
    style: CustomBuilderT<CircleAttribute>
): CircleAttribute
```

定义Circle组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Circle(    style: CustomBuilderT<CircleAttribute>): CircleAttribute--><!--Device-unnamed-export declare function Circle(    style: CustomBuilderT<CircleAttribute>): CircleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;CircleAttribute&gt; | Yes | Circle选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CircleAttribute](../arkts-components/arkts-arkui-circle-attribute.md) |  |

