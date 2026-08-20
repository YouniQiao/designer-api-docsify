# ProgressAttribute

除支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)外，还支持以下属性。

支持[通用事件](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md)。

> **说明：**
> 
> 该组件重写了通用属性backgroundColor，直接添加在Progress组件上，设置进度条的底色。如需设 &gt; 置整个Progress组件的背景色，需要在外层容器上添加backgroundColor，并用该容器包裹Progress组件。

**继承/实现关系：** ProgressAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface ProgressAttribute--><!--Device-unnamed-export declare interface ProgressAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ProgressAttribute-attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ProgressAttribute](arkts-progress-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## color

```TypeScript
color(value: ResourceColor | LinearGradient | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-color(value: ResourceColor | LinearGradient | undefined): this--><!--Device-ProgressAttribute-color(value: ResourceColor | LinearGradient | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-datapanel-lineargradient-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this--><!--Device-ProgressAttribute-contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ProgressConfiguration](arkts-progress-progressconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## privacySensitive

```TypeScript
privacySensitive(isPrivacySensitiveMode: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this--><!--Device-ProgressAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacySensitiveMode | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setProgressOptions

```TypeScript
setProgressOptions(options: ProgressOptions): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-setProgressOptions(options: ProgressOptions): this--><!--Device-ProgressAttribute-setProgressOptions(options: ProgressOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ProgressOptions](arkts-progress-progressoptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## style

```TypeScript
style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this--><!--Device-ProgressAttribute-style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LinearStyleOptions](arkts-progress-linearstyleoptions-i.md) \| [RingStyleOptions](arkts-progress-ringstyleoptions-i.md) \| [CapsuleStyleOptions](arkts-progress-capsulestyleoptions-i.md) \| [ProgressStyleOptions](arkts-progress-progressstyleoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## value

```TypeScript
value(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ProgressAttribute-value(value: double | undefined): this--><!--Device-ProgressAttribute-value(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置Progress组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressAttribute-default--><!--Device-ProgressAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

