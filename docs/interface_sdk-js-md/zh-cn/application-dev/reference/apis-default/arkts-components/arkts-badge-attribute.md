# BadgeAttribute

支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)。

支持[通用事件](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md)。

**继承/实现关系：** BadgeAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface BadgeAttribute--><!--Device-unnamed-export declare interface BadgeAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<BadgeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-BadgeAttribute-attributeModifier(modifier: AttributeModifier<BadgeAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-BadgeAttribute-attributeModifier(modifier: AttributeModifier<BadgeAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[BadgeAttribute](arkts-badge-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setBadgeOptions

```TypeScript
setBadgeOptions(value: BadgeParamWithNumber | BadgeParamWithString): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-BadgeAttribute-setBadgeOptions(value: BadgeParamWithNumber | BadgeParamWithString): this--><!--Device-BadgeAttribute-setBadgeOptions(value: BadgeParamWithNumber | BadgeParamWithString): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BadgeParamWithNumber](arkts-badge-badgeparamwithnumber-i.md) \| [BadgeParamWithString](arkts-badge-badgeparamwithstring-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置数字或者字符串类型的标记组件参数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BadgeAttribute-default--><!--Device-BadgeAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

