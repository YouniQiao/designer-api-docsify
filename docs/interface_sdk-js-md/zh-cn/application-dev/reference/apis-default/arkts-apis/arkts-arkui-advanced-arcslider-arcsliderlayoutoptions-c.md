# ArcSliderLayoutOptions

配置弧形Slider的布局信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ArcSliderLayoutOptions--><!--Device-unnamed-export declare class ArcSliderLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options?: ArcSliderLayoutOptionsConstructorOptions)
```

ArcSliderLayoutOptions的构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderLayoutOptions-constructor(options?: ArcSliderLayoutOptionsConstructorOptions)--><!--Device-ArcSliderLayoutOptions-constructor(options?: ArcSliderLayoutOptionsConstructorOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderLayoutOptionsConstructorOptions](arkts-arkui-advanced-arcslider-arcsliderlayoutoptionsconstructoroptions-i.md) | 否 | ArcSliderLayoutOptions的构造信息。 |

## position

```TypeScript
@Trace
  position?: ArcSliderPosition
```

弧形Slider的屏幕显示位置。

默认值：ArcSliderPosition.RIGHT

**类型：** [ArcSliderPosition](arkts-arkui-advanced-arcslider-arcsliderposition-e.md)

**默认值：** ArcSliderPosition.RIGHT

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderLayoutOptions-@Trace  position?: ArcSliderPosition--><!--Device-ArcSliderLayoutOptions-@Trace  position?: ArcSliderPosition-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## reverse

```TypeScript
@Trace
  reverse?: boolean
```

设置弧形Slider取值范围是否反向。

默认值：true。表示从下往上滑动。

**类型：** boolean

**默认值：** true

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-ArcSliderLayoutOptions-@Trace  reverse?: boolean--><!--Device-ArcSliderLayoutOptions-@Trace  reverse?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

