# LoadingProgressAttribute

除支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)外，还支持以下属性。

支持[通用事件](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md)。

**继承/实现关系：** LoadingProgressAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface LoadingProgressAttribute--><!--Device-unnamed-export declare interface LoadingProgressAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LoadingProgressAttribute-attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LoadingProgressAttribute-attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LoadingProgressAttribute](arkts-loadingprogress-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## color

```TypeScript
color(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LoadingProgressAttribute-color(value: ResourceColor | undefined): this--><!--Device-LoadingProgressAttribute-color(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LoadingProgressAttribute-contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this--><!--Device-LoadingProgressAttribute-contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[LoadingProgressConfiguration](arkts-loadingprogress-loadingprogressconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableLoading

```TypeScript
enableLoading(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LoadingProgressAttribute-enableLoading(value: boolean | undefined): this--><!--Device-LoadingProgressAttribute-enableLoading(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setLoadingProgressOptions

```TypeScript
setLoadingProgressOptions(): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-LoadingProgressAttribute-setLoadingProgressOptions(): this--><!--Device-LoadingProgressAttribute-setLoadingProgressOptions(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置LoadingProgress选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingProgressAttribute-default--><!--Device-LoadingProgressAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

