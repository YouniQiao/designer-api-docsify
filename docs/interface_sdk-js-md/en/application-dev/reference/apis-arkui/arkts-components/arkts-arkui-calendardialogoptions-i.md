# CalendarDialogOptions

日历选择器弹窗选项。

继承自[CalendarOptions](arkts-arkui-calendaroptions-i.md)。

> **说明：**
> 
> 在应用窗口缩小过程中，弹窗的宽度会被不断压缩，当缩小到一定程度时会导致其内容无法完整显示，保证CalendarPickerDialog内容能够完整显示的最小
> 窗口宽度为386vp。

**Inheritance/Implementation:** CalendarDialogOptions extends [CalendarOptions](arkts-arkui-calendaroptions-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface CalendarDialogOptions extends CalendarOptions--><!--Device-unnamed-declare interface CalendarDialogOptions extends CalendarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel?: VoidCallback
```

点击弹窗中的“取消”按钮时触发该回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarDialogOptions-onCancel?: VoidCallback--><!--Device-CalendarDialogOptions-onCancel?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

弹窗弹出后的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。
> 
> 2. 在onDidAppear内设置改变显示效果的回调事件，再次调用show时生效。
> 
> 3. 快速连续触发弹出与关闭时，存在onWillDisappear在onDidAppear前生效。
> 
> 4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。

> **选取指导：**
> 
> - onWillAppear：适合在弹窗显示前准备数据、重置状态。
> - onDidAppear：适合在弹窗完全显示后执行动画、发起网络请求、设置焦点等需要弹窗可见才能进行的操作。
> - onWillDisappear：适合在弹窗消失前保存数据、清理资源、取消网络请求。
> - onDidDisappear：适合在弹窗完全消失后执行清理工作、重置状态、恢复其他UI。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-onDidAppear?: VoidCallback--><!--Device-CalendarDialogOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

弹窗消失后的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-onDidDisappear?: VoidCallback--><!--Device-CalendarDialogOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

弹窗显示动效前的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。
> 
> 2. 在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-onWillAppear?: VoidCallback--><!--Device-CalendarDialogOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

弹窗退出动效前的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。
> 
> 2. 快速连续触发弹出与关闭时，存在onWillDisappear在onDidAppear前生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-onWillDisappear?: VoidCallback--><!--Device-CalendarDialogOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## acceptButtonStyle

```TypeScript
acceptButtonStyle?: PickerDialogButtonStyle
```

设置确认按钮显示样式、重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

> **说明：**
> 
> 1. acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。
> 
> 2. 按钮高度默认40vp，在关怀模式-大字体场景下高度不变。即使按钮样式设置为圆角矩形
> [ROUNDED_RECTANGLE](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#rounded_rectangle)，在关怀模式-大字体场景下按钮形状仍呈现为胶囊型按钮
> [Capsule](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#capsule)的样式。

**Type:** [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle--><!--Device-CalendarDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

弹窗背板模糊材质。

> 默认值：BlurStyle.COMPONENT_ULTRA_THICK

> **说明：**
> 
> 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则背景颜色显示效果
> 不符合预期。设置backgroundEffect后将覆盖本属性效果。

**Type:** [BlurStyle](arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CalendarDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

背景模糊效果参数，用于自定义弹窗背景模糊的显示样式，支持配置颜色模式、自适应颜色、缩放比例等属性，实现不同的背景模糊视觉效果。默认值请参考BackgroundBlurStyleOptions。

> **说明：**
> 
> 未设置时沿用backgroundBlurStyle的默认效果（BlurStyle.COMPONENT_ULTRA_THICK）。

**Type:** [BackgroundBlurStyleOptions](../arkts-apis/arkts-arkui-common-backgroundblurstyleoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CalendarDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-CalendarDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

弹窗背板颜色。

> 默认值：Color.Transparent

> **说明：**
> 
> 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则背景颜色显示效果不符合预期。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-backgroundColor?: ResourceColor--><!--Device-CalendarDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

背景效果参数，用于自定义弹窗背景的显示效果，支持配置模糊半径、饱和度、亮度、颜色等属性，实现不同的背景视觉效果。默认值请参考[BackgroundEffectOptions](../arkts-apis/arkts-arkui-common-backgroundeffectoptions-i.md/arkts-arkui-common-backgroundeffectoptions-i.md)。

> **说明：**
> 
> 未设置时不生效，此时弹窗背景模糊效果由backgroundBlurStyle决定；设置后将覆盖backgroundBlurStyle的效果。从API版本26.0.0开始，
> 设置systemMaterial后backgroundEffect与backgroundBlurStyle均不生效。

**Type:** [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CalendarDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-CalendarDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelButtonStyle

```TypeScript
cancelButtonStyle?: PickerDialogButtonStyle
```

设置取消按钮显示样式、重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

> **说明：**
> 
> 1. acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。
> 
> 2. 按钮高度默认40vp，在关怀模式-大字体场景下高度不变。即使按钮样式设置为圆角矩形
> [ROUNDED_RECTANGLE](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#rounded_rectangle)，在关怀模式-大字体场景下按钮形状仍呈现为胶囊型按钮
> [Capsule](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#capsule)的样式。

**Type:** [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle--><!--Device-CalendarDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

设置弹窗是否响应悬停态，适用于折叠屏等支持悬停模式的设备。

- true：弹窗响应悬停态，在折叠屏悬停模式下会自适应调整布局区域，提供更好的多任务体验。  
- false：弹窗不响应悬停态，在悬停模式下保持默认布局。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CalendarDialogOptions-enableHoverMode?: boolean--><!--Device-CalendarDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

设置悬停态下弹窗的默认展示区域，仅在enableHoverMode为true时生效。不同的区域值对应弹窗在折叠屏悬停模式下的不同布局位置（如BOTTOM_SCREEN表示弹窗展示在下半屏区域，TOP_SCREEN表示弹窗展示在上半屏区域）。

> 默认值：HoverModeAreaType.BOTTOM_SCREEN

**Type:** [HoverModeAreaType](arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CalendarDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-CalendarDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## markToday

```TypeScript
markToday?: boolean
```

设置日历选择器弹窗中系统当前日期是否保持高亮显示。

- true：系统当前日期在日历选择器弹窗内保持高亮显示。  
- false：系统当前日期在日历选择器弹窗内不保持高亮显示。

> 默认值：false

**Type:** boolean

**Default:** false

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CalendarDialogOptions-markToday?: boolean--><!--Device-CalendarDialogOptions-markToday?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAccept

```TypeScript
onAccept?: Callback<Date>
```

点击弹窗中的“确定”按钮时触发该回调。

回调函数的参数表示选中的日期值。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Date&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarDialogOptions-onAccept?: Callback<Date>--><!--Device-CalendarDialogOptions-onAccept?: Callback<Date>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<Date>
```

选择弹窗中日期使当前选中项改变时触发该回调。

回调函数的参数表示选中的日期值。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Date&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarDialogOptions-onChange?: Callback<Date>--><!--Device-CalendarDialogOptions-onChange?: Callback<Date>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

设置弹窗背板的阴影。

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。

**Type:** [ShadowOptions](../arkts-apis/arkts-arkui-common-shadowoptions-i.md) \| ShadowStyle

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CalendarDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-CalendarDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

设置弹窗的系统材质。

> **说明：**
> 
> - 默认值：[ImmersiveOptions](ImmersiveOptions)的style为ImmersiveStyle.ULTRA_THICK的
> [ImmersiveMaterial](ImmersiveMaterial)对象。设置undefined时与默认值保持一致。
> - 不同的材质具有不同的视觉效果，包括背景透明度、模糊程度、阴影样式等方面的差异，该接口影响背景色
> [backgroundColor](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundcolor)、背景模糊
> [backgroundBlurStyle](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundblurstyle)
> 、背景效果[backgroundEffect](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundeffect)、边框颜色
> [borderColor](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#bordercolor)、边框宽度[borderWidth](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#borderwidth)、阴影
> [shadow](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#shadow)，当设置系统材质时，上述接口不生效。

**Type:** [SystemUiMaterial](../arkts-apis/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CalendarDialogOptions-systemMaterial?: SystemUiMaterial--><!--Device-CalendarDialogOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

