# RelativeContainer

## RelativeContainer

```TypeScript
export declare function RelativeContainer(

    content_?: CustomBuilder,
): RelativeContainerAttribute
```

相对布局组件，用于复杂场景中元素对齐的布局。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |


## RelativeContainer

```TypeScript
export declare function RelativeContainer(
    style: CustomBuilderT<RelativeContainerAttribute>,
    content_?: CustomBuilder,
): RelativeContainerAttribute
```

Defines RelativeContainer Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md)&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |
