# Blank

## Blank

```TypeScript
export declare function Blank(
    min?: double | string,
): BlankAttribute
```

空白填充组件，在容器主轴方向上，空白填充组件具有自动填充容器空余部分的能力。仅当父组件为[Row](../../../reference/apis-arkui/arkui-ts/ts-container-row.md)/  
[Column](../../../reference/apis-arkui/arkui-ts/ts-container-column.md)/  
[Flex](../../../reference/apis-arkui/arkui-ts/ts-container-flex.md)时生效。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Blank(    min?: double | string,): BlankAttribute--><!--Device-unnamed-export declare function Blank(    min?: double | string,): BlankAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| min | double \| string | No | 空白填充组件在容器主轴上的最小大小。&lt;br&gt; 默认值：0，number类型单位为vp，string类型可以显式指定 [像素单位](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md)， 如'10px'。不指定像素单位时，默认单位vp，如'10'，等同于10vp。&lt;br&gt; 非法值：按默认值处理。&lt;br&gt; **说明：**&lt;br&gt; 不支持设置百分比。负值使用默认值。当最小值大于容器可用空间时， 使用最小值作为自身大小并超出容器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BlankAttribute](../arkts-components/arkts-arkui-blank-attribute.md) |  |


## Blank

```TypeScript
export declare function Blank(
    style: CustomBuilderT<BlankAttribute>
): BlankAttribute
```

Defines Blank Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Blank(    style: CustomBuilderT<BlankAttribute>): BlankAttribute--><!--Device-unnamed-export declare function Blank(    style: CustomBuilderT<BlankAttribute>): BlankAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;BlankAttribute&gt; | Yes | Blank options. |

**Return value:**

| Type | Description |
| --- | --- |
| [BlankAttribute](../arkts-components/arkts-arkui-blank-attribute.md) |  |

