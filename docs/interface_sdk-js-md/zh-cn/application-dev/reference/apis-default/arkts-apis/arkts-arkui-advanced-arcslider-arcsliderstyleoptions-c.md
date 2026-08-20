# ArcSliderStyleOptions

配置弧形Slider的样式信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ArcSliderStyleOptions--><!--Device-unnamed-export declare class ArcSliderStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options?: ArcSliderStyleOptionsConstructorOptions)
```

ArcSliderStyleOptions的构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderStyleOptions-constructor(options?: ArcSliderStyleOptionsConstructorOptions)--><!--Device-ArcSliderStyleOptions-constructor(options?: ArcSliderStyleOptionsConstructorOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderStyleOptionsConstructorOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptionsconstructoroptions-i.md) | 否 | ArcSliderStyleOptions的构造信息。 |

## activeTrackThickness

```TypeScript
@Trace
  activeTrackThickness?: double
```

放大状态下弧形Slider的描边粗细，单位：vp。

默认值：24

取值范围：[24, 36]，异常值按默认值处理。

**类型：** double

**默认值：** 24

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderStyleOptions-@Trace  activeTrackThickness?: double--><!--Device-ArcSliderStyleOptions-@Trace  activeTrackThickness?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## selectedColor

```TypeScript
@Trace
  selectedColor?: string
```

设置描边高亮色。

默认值：#FF5EA1FF

**类型：** string

**默认值：** #FF5EA1FF

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderStyleOptions-@Trace  selectedColor?: string--><!--Device-ArcSliderStyleOptions-@Trace  selectedColor?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## trackBlur

```TypeScript
@Trace
  trackBlur?: double
```

设置描边背景模糊值，单位：vp。

默认值：20

设置小于0的值时，按照默认值处理。

**类型：** double

**默认值：** 20

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderStyleOptions-@Trace  trackBlur?: double--><!--Device-ArcSliderStyleOptions-@Trace  trackBlur?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## trackColor

```TypeScript
@Trace
  trackColor?: string
```

设置描边背景色。

默认值：#33FFFFFF

**类型：** string

**默认值：** #33FFFFFF

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderStyleOptions-@Trace  trackColor?: string--><!--Device-ArcSliderStyleOptions-@Trace  trackColor?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## trackThickness

```TypeScript
@Trace
  trackThickness?: double
```

正常状态下弧形Slider的描边粗细，单位：vp。

默认值：5

取值范围：[5, 16]，异常值按默认值处理。

**类型：** double

**默认值：** 5

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderStyleOptions-@Trace  trackThickness?: double--><!--Device-ArcSliderStyleOptions-@Trace  trackThickness?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

