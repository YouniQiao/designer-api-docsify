# Line

## Line

```TypeScript
export declare function Line(
    options?: LineOptions
): LineAttribute
```

用于绘制直线的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Line(    options?: LineOptions): LineAttribute--><!--Device-unnamed-export declare function Line(    options?: LineOptions): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-line-lineoptions-i.md) | No | Line绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LineAttribute](../arkts-components/arkts-arkui-line-attribute.md) | 直线的属性。 |


## Line

```TypeScript
export declare function Line(
    style: CustomBuilderT<LineAttribute>
): LineAttribute
```

定义Line组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Line(    style: CustomBuilderT<LineAttribute>): LineAttribute--><!--Device-unnamed-export declare function Line(    style: CustomBuilderT<LineAttribute>): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;LineAttribute&gt; | Yes | 设置组件属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LineAttribute](../arkts-components/arkts-arkui-line-attribute.md) |  |

