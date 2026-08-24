# Badge

## Badge

```TypeScript
@ComponentBuilder
export declare function Badge(
    value: BadgeParamWithNumber | BadgeParamWithString, 
    content_?: CustomBuilder
): BadgeAttribute
```

根据数字或者字符串创建标记组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function Badge(    value: BadgeParamWithNumber | BadgeParamWithString,     content_?: CustomBuilder): BadgeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Badge(    value: BadgeParamWithNumber | BadgeParamWithString,     content_?: CustomBuilder): BadgeAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BadgeParamWithNumber](arkts-badge-badgeparamwithnumber-i.md) \| [BadgeParamWithString](arkts-badge-badgeparamwithstring-i.md) | 是 | 数字、字符串类型的标记组件参数。 |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | 子组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BadgeAttribute](arkts-badge-attribute.md) |  |


## Badge

```TypeScript
@Builder
export declare function Badge(
    style: CustomBuilderT<BadgeAttribute>,
    content_?: CustomBuilder,
): BadgeAttribute
```

定义Badge组件

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function Badge(    style: CustomBuilderT<BadgeAttribute>,    content_?: CustomBuilder,): BadgeAttribute--><!--Device-unnamed-@Builderexport declare function Badge(    style: CustomBuilderT<BadgeAttribute>,    content_?: CustomBuilder,): BadgeAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[BadgeAttribute](arkts-badge-attribute.md)&gt; | 是 | badge属性实例。 |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | 子组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BadgeAttribute](arkts-badge-attribute.md) |  |

