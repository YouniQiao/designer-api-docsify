# LinearGradientStyle

显示为线性渐变。LinearGradientStyle继承自[ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md)。

**继承/实现关系：** LinearGradientStyle extends [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options: LinearGradientOptions)
```

用于创建LinearGradientStyle对象的构造函数。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [options](#options) | [LinearGradientOptions](../arkts-components/arkts-arkui-lineargradientoptions-i.md) | 是 |

## options

```TypeScript
options: LinearGradientOptions
```

显示为线性渐变效果。  
LinearGradientOptions 中的direction默认值按 GradientDirection中的NONE处理。

**类型：** [LinearGradientOptions](../arkts-components/arkts-arkui-lineargradientoptions-i.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
