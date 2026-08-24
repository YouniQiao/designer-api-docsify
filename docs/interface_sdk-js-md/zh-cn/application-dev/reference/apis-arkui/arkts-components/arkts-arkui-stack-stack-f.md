# Stack

## Stack

```TypeScript
@ComponentBuilder
export declare function Stack(
    options?: StackOptions,
    content_?: CustomBuilder,
): StackAttribute
```

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function Stack(    options?: StackOptions,    content_?: CustomBuilder,): StackAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Stack(    options?: StackOptions,    content_?: CustomBuilder,): StackAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [StackOptions](arkts-arkui-stack-stackoptions-i.md) | 否 | 设置子组件在容器内的对齐方式。 |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StackAttribute](arkts-arkui-stack-attribute.md) |  |


## Stack

```TypeScript
@Builder
export declare function Stack(
    style: CustomBuilderT<StackAttribute>,
    content_?: CustomBuilder,
): StackAttribute
```

Defines Stack Component.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function Stack(    style: CustomBuilderT<StackAttribute>,    content_?: CustomBuilder,): StackAttribute--><!--Device-unnamed-@Builderexport declare function Stack(    style: CustomBuilderT<StackAttribute>,    content_?: CustomBuilder,): StackAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[StackAttribute](arkts-arkui-stack-attribute.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StackAttribute](arkts-arkui-stack-attribute.md) |  |

