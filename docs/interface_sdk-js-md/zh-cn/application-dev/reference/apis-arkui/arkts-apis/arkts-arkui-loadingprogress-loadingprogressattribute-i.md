# LoadingProgressAttribute

除支持通用属性外，还支持以下属性。支持通用事件。

**继承/实现关系：** LoadingProgressAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LoadingProgressAttribute](arkts-arkui-loadingprogress-loadingprogressattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LoadingProgressAttribute](arkts-arkui-loadingprogress-loadingprogressattribute-i.md) |

## color

```TypeScript
default color(value: ResourceColor | undefined): this
```

设置加载进度条前景色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LoadingProgressAttribute](arkts-arkui-loadingprogress-loadingprogressattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this
```

定制LoadingProgress内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[LoadingProgressConfiguration](arkts-arkui-loadingprogress-loadingprogressconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LoadingProgressAttribute](arkts-arkui-loadingprogress-loadingprogressattribute-i.md) |

## enableLoading

```TypeScript
default enableLoading(value: boolean | undefined): this
```

设置LoadingProgress动画是否显示。LoadingProgress动画不显示时，该组件依旧占位。通用属性Visibility.Hidden隐藏的是包括 border、padding等整个组件范围，而enableLoading=false只隐藏 LoadingProgress本身动画内容，不包括border等。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LoadingProgressAttribute](arkts-arkui-loadingprogress-loadingprogressattribute-i.md) |

## setLoadingProgressOptions

```TypeScript
default setLoadingProgressOptions(): this
```

设置LoadingProgress选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [LoadingProgressAttribute](arkts-arkui-loadingprogress-loadingprogressattribute-i.md) |
