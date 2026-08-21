# DateStyleOptions

DateStyleOptions定义了日期内联型Counter的属性和事件。

继承于[CommonOptions](arkts-arkuiadvancedcounter-commonoptions-c.md)。

**继承/实现关系：** DateStyleOptions extends [CommonOptions](arkts-arkuiadvancedcounter-commonoptions-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-declare class DateStyleOptions--><!--Device-unnamed-declare class DateStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## day

```TypeScript
day?: int
```

设置日期内联型初始日。 取值范围：[1, 31]。默认值：1 说明：每个月份的具体取值范围由该月份的实际天数决定。

**类型：** int

**默认值：** 1

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateStyleOptions-day?: int--><!--Device-DateStyleOptions-day?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month?: int
```

设置日期内联型初始月份。 取值范围：[1, 12]。默认值：1 超出取值范围按默认值处理。

**类型：** int

**默认值：** 1

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateStyleOptions-month?: int--><!--Device-DateStyleOptions-month?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onDateChange

```TypeScript
onDateChange?: OnDateCounterChangeCallback
```

当日期改变时，返回当前日期。 date：当前显示的日期值。 值为undefined时，不显示当前的日期值。

**类型：** [OnDateCounterChangeCallback](arkts-ondatecounterchangecallback-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateStyleOptions-onDateChange?: OnDateCounterChangeCallback--><!--Device-DateStyleOptions-onDateChange?: OnDateCounterChangeCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year?: int
```

设置日期内联型初始年份。 取值范围：[1, 5000]。默认值：1 超出取值范围按默认值处理。

**类型：** int

**默认值：** 1

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateStyleOptions-year?: int--><!--Device-DateStyleOptions-year?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

