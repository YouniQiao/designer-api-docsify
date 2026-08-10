# PathAttribute

路径绘制组件属性，用于设置路径的相关属性。

**继承/实现关系：** PathAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface PathAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface PathAttribute extends CommonShapeMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PathAttribute-default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PathAttribute-default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PathAttribute](arkts-arkui-path-pathattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## commands

```TypeScript
default commands(value: ResourceStr | undefined): this
```

设置符合  
[SVG路径描述规范](../../../reference/apis-arkui/arkui-ts/ts-drawing-components-path.md#svg路径描述规范)的命令字符串，单位为px。像素单位转换方法请参考  
[像素单位转换](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PathAttribute-default commands(value: ResourceStr | undefined): this--><!--Device-PathAttribute-default commands(value: ResourceStr | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 | 线条绘制的路径。 &lt;br&gt;默认值：空字符串&lt;br&gt;默认单位：px &lt;br&gt;异常值undefined和null按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setPathOptions

```TypeScript
default setPathOptions(options?: PathOptions): this
```

Set Path options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PathAttribute-default setPathOptions(options?: PathOptions): this--><!--Device-PathAttribute-default setPathOptions(options?: PathOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PathOptions](../arkts-components/arkts-arkui-pathoptions-i.md) | 否 | Path constructor options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the instance of the PathAttribute. |

