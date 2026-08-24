# Select

## Select

```TypeScript
@ComponentBuilder
export declare function Select(
    options: Array<SelectOption>,
    content_?: CustomBuilder,
): SelectAttribute
```

Defines Select Component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function Select(    options: Array<SelectOption>,    content_?: CustomBuilder,): SelectAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Select(    options: Array<SelectOption>,    content_?: CustomBuilder,): SelectAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Array&lt;[SelectOption](arkts-select-selectoption-i.md)&gt; | 是 | the options of Select. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SelectAttribute](arkts-select-attribute.md) |  |

