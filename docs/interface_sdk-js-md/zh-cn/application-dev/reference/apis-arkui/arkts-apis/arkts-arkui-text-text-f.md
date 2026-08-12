# Text

## Text

```TypeScript
export declare function Text(
    style: CustomBuilderT<TextAttribute>,
    content_?: CustomBuilder,
): TextAttribute
```

定义Text组件。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.1.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Text(    style: CustomBuilderT<TextAttribute>,    content_?: CustomBuilder,): TextAttribute--><!--Device-unnamed-export declare function Text(    style: CustomBuilderT<TextAttribute>,    content_?: CustomBuilder,): TextAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[TextAttribute](arkts-arkui-text-textattribute-i.md)&gt; | 是 | Text属性实例。 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | 容器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |  |


## Text

```TypeScript
export declare function Text(
    content?: string | Resource, value?: TextOptions, 
    content_?: CustomBuilder,
): TextAttribute
```

定义Text组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Text(    content?: string | Resource, value?: TextOptions,     content_?: CustomBuilder,): TextAttribute--><!--Device-unnamed-export declare function Text(    content?: string | Resource, value?: TextOptions,     content_?: CustomBuilder,): TextAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string \| [Resource](arkts-arkui-resource-t.md) | 否 |  |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | 否 |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextAttribute](arkts-arkui-text-textattribute-i.md) |  |

