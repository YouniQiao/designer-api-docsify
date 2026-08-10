# PathAttribute

路径绘制组件属性，用于设置路径的相关属性。

**Inheritance/Implementation:** PathAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PathAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface PathAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PathAttribute-default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PathAttribute-default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PathAttribute](arkts-arkui-path-pathattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## commands

```TypeScript
default commands(value: ResourceStr | undefined): this
```

设置符合  
[SVG路径描述规范](../../../reference/apis-arkui/arkui-ts/ts-drawing-components-path.md#svg路径描述规范)的命令字符串，单位为px。像素单位转换方法请参考  
[像素单位转换](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PathAttribute-default commands(value: ResourceStr | undefined): this--><!--Device-PathAttribute-default commands(value: ResourceStr | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes | 线条绘制的路径。 &lt;br&gt;默认值：空字符串&lt;br&gt;默认单位：px &lt;br&gt;异常值undefined和null按照默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setPathOptions

```TypeScript
default setPathOptions(options?: PathOptions): this
```

Set Path options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PathAttribute-default setPathOptions(options?: PathOptions): this--><!--Device-PathAttribute-default setPathOptions(options?: PathOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathOptions](../arkts-components/arkts-arkui-pathoptions-i.md) | No | Path constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the PathAttribute. |

