# RelativeContainer

## RelativeContainer

```TypeScript
export declare function RelativeContainer(

    content_?: CustomBuilder,
): RelativeContainerAttribute
```

相对布局组件，用于复杂场景中元素对齐的布局。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function RelativeContainer(    content_?: CustomBuilder,): RelativeContainerAttribute--><!--Device-unnamed-export declare function RelativeContainer(    content_?: CustomBuilder,): RelativeContainerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | 定义子组件的Builder函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RelativeContainerAttribute](../arkts-components/arkts-arkui-relativecontainer-attribute.md) |  |


## RelativeContainer

```TypeScript
export declare function RelativeContainer(
    style: CustomBuilderT<RelativeContainerAttribute>,
    content_?: CustomBuilder,
): RelativeContainerAttribute
```

Defines RelativeContainer Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function RelativeContainer(    style: CustomBuilderT<RelativeContainerAttribute>,    content_?: CustomBuilder,): RelativeContainerAttribute--><!--Device-unnamed-export declare function RelativeContainer(    style: CustomBuilderT<RelativeContainerAttribute>,    content_?: CustomBuilder,): RelativeContainerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;RelativeContainerAttribute&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RelativeContainerAttribute](../arkts-components/arkts-arkui-relativecontainer-attribute.md) |  |

