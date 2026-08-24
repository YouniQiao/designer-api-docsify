# ProgressButton

文本下载按钮，可显示具体的下载进度。设备行为差异：该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

> **说明：**&gt;
> - 如果ProgressButton设置通用属性和通用事件，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到ProgressButton本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ProgressButton设置通用属性和通用事件。
@struct { ProgressButton }

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Component

<!--Device-unnamed-export declare struct ProgressButton--><!--Device-unnamed-export declare struct ProgressButton-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-@Builder  build(): void--><!--Device-ProgressButton-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## clickCallback

```TypeScript
clickCallback: () => void
```

下载按钮的点击回调。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-clickCallback: () => void--><!--Device-ProgressButton-clickCallback: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## colorOptions

```TypeScript
colorOptions?: ProgressButtonColorOptions
```

下载按钮颜色选项。

**类型：** [ProgressButtonColorOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-progressbutton-progressbuttoncoloroptions-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-@PropRef  colorOptions?: ProgressButtonColorOptions--><!--Device-ProgressButton-@PropRef  colorOptions?: ProgressButtonColorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: ResourceStr
```

下载按钮的文本。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-@PropRef  content: ResourceStr--><!--Device-ProgressButton-@PropRef  content: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enable

```TypeScript
enable: boolean
```

下载按钮是否可以点击。<br> true：可以点击。<br> false：不可点击。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-@PropRef  enable: boolean--><!--Device-ProgressButton-@PropRef  enable: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## progress

```TypeScript
progress: double
```

下载按钮的当前进度值。<br/>取值范围：[0,100]。设置小于0的数值时置为0，设置大于100的数值置为100。<br/>默认值：0

**类型：** double

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-@PropRef  progress: double--><!--Device-ProgressButton-@PropRef  progress: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## progressButtonRadius

```TypeScript
progressButtonRadius?: LengthMetrics
```

下载按钮的圆角（不支持百分比设置）。<br/>取值范围：[0, height/2]<br/>默认值：height/2<br/>设置非法数值时，按照默认值处理。

**类型：** LengthMetrics

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-@PropRef  progressButtonRadius?: LengthMetrics--><!--Device-ProgressButton-@PropRef  progressButtonRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## progressButtonWidth

```TypeScript
progressButtonWidth?: Length
```

下载按钮的宽度。<br/>默认值：44vp

**类型：** Length

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProgressButton-progressButtonWidth?: Length--><!--Device-ProgressButton-progressButtonWidth?: Length-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

