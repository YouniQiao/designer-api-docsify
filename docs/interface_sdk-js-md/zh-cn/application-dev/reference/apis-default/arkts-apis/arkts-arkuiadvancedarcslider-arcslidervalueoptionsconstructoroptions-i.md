# ArcSliderValueOptionsConstructorOptions

ArcSliderValueOptions的构造信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface ArcSliderValueOptionsConstructorOptions--><!--Device-unnamed-export interface ArcSliderValueOptionsConstructorOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
```

## max

```TypeScript
max?: double
```

设置最大值。

默认值：100

**说明：**

当出现异常情况min &gt;= max时，min取默认值0，max取默认值100。

progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。

**类型：** double

**默认值：** 100

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderValueOptionsConstructorOptions-max?: double--><!--Device-ArcSliderValueOptionsConstructorOptions-max?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## min

```TypeScript
min?: double
```

设置最小值。

默认值：0

**类型：** double

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderValueOptionsConstructorOptions-min?: double--><!--Device-ArcSliderValueOptionsConstructorOptions-min?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## progress

```TypeScript
progress?: double
```

设置当前进度值。

默认值：与参数min的取值一致。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderValueOptionsConstructorOptions-progress?: double--><!--Device-ArcSliderValueOptionsConstructorOptions-progress?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

