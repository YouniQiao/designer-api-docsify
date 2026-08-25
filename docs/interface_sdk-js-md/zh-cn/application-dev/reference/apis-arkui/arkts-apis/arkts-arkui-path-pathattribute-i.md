# PathAttribute

路径绘制组件属性，用于设置路径的相关属性。@extends CommonShapeMethod @interface PathAttribute

**继承/实现关系：** PathAttribute extends CommonShapeMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PathAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PathAttribute](arkts-arkui-path-pathattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |

## commands

```TypeScript
default commands(value: ResourceStr | undefined): this
```

设置符合 [SVG路径描述规范](arkts-arkui-path-path-f.md) 的命令字符串，单位为px。 像素单位转换方法请参考 像素单位转换。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |

## setPathOptions

```TypeScript
default setPathOptions(options?: PathOptions): this
```

Set Path options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PathOptions](arkts-arkui-path-pathoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |
