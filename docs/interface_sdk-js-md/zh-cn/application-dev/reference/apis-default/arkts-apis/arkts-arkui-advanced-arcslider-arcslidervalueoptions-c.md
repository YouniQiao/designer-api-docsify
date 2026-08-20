# ArcSliderValueOptions

配置弧形Slider的数值信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ArcSliderValueOptions--><!--Device-unnamed-export declare class ArcSliderValueOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options?: ArcSliderValueOptionsConstructorOptions)
```

ArcSliderValueOptions的构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderValueOptions-constructor(options?: ArcSliderValueOptionsConstructorOptions)--><!--Device-ArcSliderValueOptions-constructor(options?: ArcSliderValueOptionsConstructorOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderValueOptionsConstructorOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcslidervalueoptionsconstructoroptions-i.md) | 否 | ArcSliderValueOptions的构造信息。 |

## max

```TypeScript
@Trace
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

<!--Device-ArcSliderValueOptions-@Trace  max?: double--><!--Device-ArcSliderValueOptions-@Trace  max?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## min

```TypeScript
@Trace
  min?: double
```

设置最小值。

默认值：0

**类型：** double

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderValueOptions-@Trace  min?: double--><!--Device-ArcSliderValueOptions-@Trace  min?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## progress

```TypeScript
@Trace
  progress?: double
```

设置当前进度值。

默认值：与参数min的取值一致。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderValueOptions-@Trace  progress?: double--><!--Device-ArcSliderValueOptions-@Trace  progress?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

