# TextArea

## TextArea

```TypeScript
@ComponentBuilder
export declare function TextArea(
    value?: TextAreaOptions
): TextAreaAttribute
```

定义多行输入框组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function TextArea(    value?: TextAreaOptions): TextAreaAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function TextArea(    value?: TextAreaOptions): TextAreaAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextAreaOptions](arkts-arkui-textarea-textareaoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextAreaAttribute](arkts-arkui-textarea-attribute.md) |  |


## TextArea

```TypeScript
@Builder
export declare function TextArea(
    style: CustomBuilderT<TextAreaAttribute>,
): TextAreaAttribute
```

定义TextArea组件。

**起始版本：** 26.1.0

**ArkTS模式：** ArkTS-Sta起始版本为26.1.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function TextArea(    style: CustomBuilderT<TextAreaAttribute>,): TextAreaAttribute--><!--Device-unnamed-@Builderexport declare function TextArea(    style: CustomBuilderT<TextAreaAttribute>,): TextAreaAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[TextAreaAttribute](arkts-arkui-textarea-attribute.md)&gt; | 是 | TextArea属性实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextAreaAttribute](arkts-arkui-textarea-attribute.md) |  |

