# ExtendableText

定义扩展文本组件

**继承/实现关系：** ExtendableText implements [TextAttribute](arkts-arkui-text-textattribute-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableText>(
    factory: ConstructorT<T>, 
    content?: string | Resource, 
    value?: TextOptions, 
    content_?: CustomBuilder
  ): T
```

扩展文本组件构造器

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |
| content | string \| [Resource](arkts-arkui-resource-t.md) | 否 |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | 否 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableText>(
      styles: CustomBuilderT<T>, 
      factory: ConstructorT<T>, 
      content_?: CustomBuilder
  ): void
```

扩展文本组件入口

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styles | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | 是 |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

## setTextOptions

```TypeScript
public setTextOptions(
    content?: string | Resource, 
    value?: TextOptions
  ): this
```

设置文本组件的选项

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | string \| [Resource](arkts-arkui-resource-t.md) | 否 |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ExtendableText](arkts-arkui-text-extendabletext-c.md) |
