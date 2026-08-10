# Rect

## Rect

```TypeScript
export declare function Rect(
    options?: RectOptions | RoundedRectOptions
): RectAttribute
```

用于绘制矩形的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Rect(    options?: RectOptions | RoundedRectOptions): RectAttribute--><!--Device-unnamed-export declare function Rect(    options?: RectOptions | RoundedRectOptions): RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rect-rectoptions-i.md) \| RoundedRectOptions | No | Rect绘制属性。异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RectAttribute](../arkts-components/arkts-arkui-rect-attribute.md) | The attribute of the Rect |


## Rect

```TypeScript
export declare function Rect(
    style: CustomBuilderT<RectAttribute>,
): RectAttribute
```

Defines Rect Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Rect(    style: CustomBuilderT<RectAttribute>,): RectAttribute--><!--Device-unnamed-export declare function Rect(    style: CustomBuilderT<RectAttribute>,): RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;RectAttribute&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [RectAttribute](../arkts-components/arkts-arkui-rect-attribute.md) |  |

