# CounterOptions

Defines the counter options.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-declare class CounterOptions--><!--Device-unnamed-declare class CounterOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## dateOptions

```TypeScript
dateOptions?: DateStyleOptions
```

日期型内联型Counter的样式。 默认值：显示0001/01/01的日期型内联型Counter。

**类型：** [DateStyleOptions](arkts-arkui-advanced-counter-datestyleoptions-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterOptions-dateOptions?: DateStyleOptions--><!--Device-CounterOptions-dateOptions?: DateStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: Direction
```

布局方向。 默认值：Direction。

**类型：** Direction

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterOptions-direction?: Direction--><!--Device-CounterOptions-direction?: Direction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## inlineOptions

```TypeScript
inlineOptions?: InlineStyleOptions
```

普通数字内联调节型Counter的样式。 默认值：显示计数器为0的普通数字内联调节型Counter。

**类型：** [InlineStyleOptions](arkts-arkui-advanced-counter-inlinestyleoptions-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterOptions-inlineOptions?: InlineStyleOptions--><!--Device-CounterOptions-inlineOptions?: InlineStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## numberOptions

```TypeScript
numberOptions?: NumberStyleOptions
```

列表型和紧凑型Counter的样式。 默认值：显示计数器为0的列表型或紧凑型Counter。

**类型：** [NumberStyleOptions](arkts-arkui-advanced-counter-numberstyleoptions-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterOptions-numberOptions?: NumberStyleOptions--><!--Device-CounterOptions-numberOptions?: NumberStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: CounterType
```

指定当前Counter的类型。

默认值：CounterType.LIST

不支持设置undefined。

**类型：** [CounterType](arkts-arkui-advanced-counter-countertype-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterOptions-type: CounterType--><!--Device-CounterOptions-type: CounterType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

