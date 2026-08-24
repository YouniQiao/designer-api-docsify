# ScrollBar

## ScrollBar

```TypeScript
@ComponentBuilder
export declare function ScrollBar(
    value: ScrollBarOptions, 
    content_?: CustomBuilder,
): ScrollBarAttribute
```

定义滚动条组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function ScrollBar(    value: ScrollBarOptions,     content_?: CustomBuilder,): ScrollBarAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ScrollBar(    value: ScrollBarOptions,     content_?: CustomBuilder,): ScrollBarAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-scrollbar-scrollbaroptions-i.md) | 是 |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | 子组件 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollBarAttribute](arkts-scrollbar-attribute.md) |  |


## ScrollBar

```TypeScript
@Builder
export declare function ScrollBar(
    style_: CustomBuilderT<ScrollBarAttribute>, 
    content_?: CustomBuilder
): ScrollBarAttribute
```

定义滚动条组件。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,     content_?: CustomBuilder): ScrollBarAttribute--><!--Device-unnamed-@Builderexport declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,     content_?: CustomBuilder): ScrollBarAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ScrollBarAttribute](arkts-scrollbar-attribute.md)&gt; | 是 | The style to create a ScrollBar. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollBarAttribute](arkts-scrollbar-attribute.md) | ScrollBar的属性。 |

