# ScrollBar

## ScrollBar

```TypeScript
export declare function ScrollBar(
    value: ScrollBarOptions, 
    content_?: CustomBuilder,
): ScrollBarAttribute
```

定义滚动条组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function ScrollBar(    value: ScrollBarOptions,     content_?: CustomBuilder,): ScrollBarAttribute--><!--Device-unnamed-export declare function ScrollBar(    value: ScrollBarOptions,     content_?: CustomBuilder,): ScrollBarAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-arkui-scrollbar-scrollbaroptions-i.md) | 是 |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | 子组件 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollBarAttribute](arkts-arkui-scrollbar-scrollbarattribute-i.md) |  |


## ScrollBar

```TypeScript
export declare function ScrollBar(
    style_: CustomBuilderT<ScrollBarAttribute>, 
    content_?: CustomBuilder
): ScrollBarAttribute
```

定义滚动条组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,     content_?: CustomBuilder): ScrollBarAttribute--><!--Device-unnamed-export declare function ScrollBar(    style_: CustomBuilderT<ScrollBarAttribute>,     content_?: CustomBuilder): ScrollBarAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ScrollBarAttribute](arkts-arkui-scrollbar-scrollbarattribute-i.md)&gt; | 是 | The style to create a ScrollBar. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollBarAttribute](arkts-arkui-scrollbar-scrollbarattribute-i.md) | ScrollBar的属性。 |

