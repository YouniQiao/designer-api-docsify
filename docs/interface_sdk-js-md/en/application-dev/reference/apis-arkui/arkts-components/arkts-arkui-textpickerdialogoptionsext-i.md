# TextPickerDialogOptionsExt

文本选择器弹窗的参数继承自[TextPickerOptions](arkts-arkui-textpickeroptions-i.md)。

**Inheritance/Implementation:** TextPickerDialogOptionsExt extends [TextPickerOptions](arkts-arkui-textpickeroptions-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface TextPickerDialogOptionsExt extends TextPickerOptions--><!--Device-unnamed-declare interface TextPickerDialogOptionsExt extends TextPickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel?: VoidCallback
```

点击弹窗中的“取消”按钮时触发该回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onCancel?: VoidCallback--><!--Device-TextPickerDialogOptionsExt-onCancel?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

弹窗弹出后的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：
> onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。
> 
> 2. 在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。
> 
> 3. 快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效，此时onDidAppear中的参数设置可能无法在当前弹窗生效。
> 
> 4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onDidAppear?: VoidCallback--><!--Device-TextPickerDialogOptionsExt-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

弹窗消失后的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：
> onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onDidDisappear?: VoidCallback--><!--Device-TextPickerDialogOptionsExt-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

弹窗显示动效前的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：
> onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。
> 
> 2. 在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onWillAppear?: VoidCallback--><!--Device-TextPickerDialogOptionsExt-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

弹窗退出动效前的事件回调。

> **说明：**
> 
> 1. 正常时序依次为：
> onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange/onScrollStop)>>onWillDisappear>>onDidDisappear。
> 
> 2. 快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onWillDisappear?: VoidCallback--><!--Device-TextPickerDialogOptionsExt-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## acceptButtonStyle

```TypeScript
acceptButtonStyle?: PickerDialogButtonStyle
```

设置确认按钮显示样式、重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

> **说明：**
> 
> 1. acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，
> 保持默认值false。
> 
> 2. 按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形
> [ROUNDED_RECTANGLE](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#rounded_rectangle)，呈现效果依然是胶囊型按钮[Capsule](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#capsule)。

**Type:** [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-acceptButtonStyle?: PickerDialogButtonStyle--><!--Device-TextPickerDialogOptionsExt-acceptButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

弹窗在竖直方向上的对齐方式。

默认值：DialogAlignment.Default

**Type:** [DialogAlignment](../arkts-apis/arkts-arkui-alertdialog-dialogalignment-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-alignment?: DialogAlignment--><!--Device-TextPickerDialogOptionsExt-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

弹窗背板模糊材质。

> 默认值：BlurStyle.COMPONENT_ULTRA_THICK

> **说明：**
> 
> 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，
> 否则显示的颜色将不符合预期效果。

**Type:** [BlurStyle](arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-backgroundBlurStyle?: BlurStyle--><!--Device-TextPickerDialogOptionsExt-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

背景模糊效果参数，用于自定义弹窗背景模糊的显示样式，支持配置颜色模式、自适应颜色、缩放比例等属性，实现不同的背景模糊视觉效果。

> **说明：**
> 
> 未设置时沿用backgroundBlurStyle的默认效果（BlurStyle.COMPONENT_ULTRA_THICK）；设置后将覆盖backgroundBlurStyle的效果。

**Type:** [BackgroundBlurStyleOptions](../arkts-apis/arkts-arkui-common-backgroundblurstyleoptions-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TextPickerDialogOptionsExt-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

弹窗背板颜色。

> 默认值：Color.Transparent

> **说明：**
> 
> 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-backgroundColor?: ResourceColor--><!--Device-TextPickerDialogOptionsExt-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

背景效果参数，用于自定义弹窗背景的显示效果，支持配置模糊半径、饱和度、亮度、颜色等属性，实现不同的背景视觉效果。

> **说明：**
> 
> 未设置时不生效，此时弹窗背景模糊效果由backgroundBlurStyle决定；设置后将覆盖backgroundBlurStyle的效果。从API版本26.0.0开始，
> 设置systemMaterial后backgroundEffect与backgroundBlurStyle均不生效。

**Type:** [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-backgroundEffect?: BackgroundEffectOptions--><!--Device-TextPickerDialogOptionsExt-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canLoop

```TypeScript
canLoop?: boolean
```

设置是否可循环滚动。

- true：可循环。  
- false：不可循环。

默认值：true

**Type:** boolean

**Default:** true

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-canLoop?: boolean--><!--Device-TextPickerDialogOptionsExt-canLoop?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelButtonStyle

```TypeScript
cancelButtonStyle?: PickerDialogButtonStyle
```

设置取消按钮显示样式、重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

> **说明：**
> 
> 1. acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，
> 保持默认值false。
> 
> 2. 按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形
> [ROUNDED_RECTANGLE](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#rounded_rectangle)，呈现效果依然是胶囊型按钮[Capsule](../arkts-apis/arkts-arkui-button-buttontype-e.md/arkts-arkui-button-buttontype-e.md#capsule)。

**Type:** [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-cancelButtonStyle?: PickerDialogButtonStyle--><!--Device-TextPickerDialogOptionsExt-cancelButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultPickerItemHeight

```TypeScript
defaultPickerItemHeight?: number | string
```

设置选择器中选项的高度。number类型取值范围：[0, +∞)，string类型仅支持number类型取值的字符串形式，例如"56"。

> 默认值：选中项56vp，非选中项36vp。设置该参数后，选中项与非选中项的高度均为所设置的值。

> **说明：**
> 
> 当defaultPickerItemHeight的值为负数时，使用默认值。

**Type:** number \| string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-defaultPickerItemHeight?: number | string--><!--Device-TextPickerDialogOptionsExt-defaultPickerItemHeight?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultTextStyle

```TypeScript
defaultTextStyle?: TextPickerTextStyle
```

设置关闭滑动过程中文本样式变化动效时的各个选项的文本样式，仅当disableTextStyleAnimation为true时生效。

默认值：与[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件默认值相同。

**Type:** [TextPickerTextStyle](arkts-arkui-textpickertextstyle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-defaultTextStyle?: TextPickerTextStyle--><!--Device-TextPickerDialogOptionsExt-defaultTextStyle?: TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableTextStyleAnimation

```TypeScript
disableTextStyleAnimation?: boolean
```

设置是否关闭滑动过程中文本样式变化的动效。

- true：关闭文本样式变化动效。  
- false：不关闭文本样式变化动效。

> 默认值：false

> **说明：**
> 
> 设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为defaultTextStyle属性设置的样式。如未设置defaultTextStyle，
> 则显示为[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件默认样式。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-disableTextStyleAnimation?: boolean--><!--Device-TextPickerDialogOptionsExt-disableTextStyleAnimation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearTextStyle

```TypeScript
disappearTextStyle?: TextPickerTextStyle
```

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。

> 默认值：
> 
> &lt;br&gt;{
> &lt;br&gt;color: '#ff182431',
> &lt;br&gt;font: {
> &lt;br&gt;size: '14fp',
> &lt;br&gt;weight: FontWeight.Regular
> &lt;br&gt;},
> &lt;br&gt;minFontSize: 0,
> &lt;br&gt;maxFontSize: 0,
> &lt;br&gt;overflow: TextOverflow.CLIP
> &lt;br&gt;}

**Type:** [TextPickerTextStyle](arkts-arkui-textpickertextstyle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-disappearTextStyle?: TextPickerTextStyle--><!--Device-TextPickerDialogOptionsExt-disappearTextStyle?: TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

设置是否开启触控反馈。

- true：开启触控反馈。  
- false：不开启触控反馈。

> 默认值：true

> **说明：**
> 
> 1. 设置为true后，其生效情况取决于系统的硬件是否支持。
> 2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：
> 
> "requestPermissions": [{"name": "ohos.permission.VIBRATE"}]

**Type:** boolean

**Default:** true

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-enableHapticFeedback?: boolean--><!--Device-TextPickerDialogOptionsExt-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

是否响应悬停态。

- true：响应悬停态。  
- false：不响应悬停态。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-enableHoverMode?: boolean--><!--Device-TextPickerDialogOptionsExt-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

设置悬停态下弹窗默认展示区域，仅在enableHoverMode为true时生效。

默认值：HoverModeAreaType.BOTTOM_SCREEN

**Type:** [HoverModeAreaType](arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-hoverModeArea?: HoverModeAreaType--><!--Device-TextPickerDialogOptionsExt-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

默认值：{ x: 0, y: 0, width: '100%', height: '100%' }

**Type:** [Rectangle](../arkts-apis/arkts-arkui-common-rectangle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-maskRect?: Rectangle--><!--Device-TextPickerDialogOptionsExt-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

弹窗相对alignment所在位置的偏移量。当需要微调弹窗位置时设置此参数，不设置时弹窗按alignment对齐位置显示。

默认值：{ dx: 0 , dy: 0 }

**Type:** [Offset](../arkts-apis/arkts-arkui-componentutils-offset-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-offset?: Offset--><!--Device-TextPickerDialogOptionsExt-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAccept

```TypeScript
onAccept?: Callback<TextPickerResult>
```

点击弹窗中的“确定”按钮时触发该回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TextPickerResult&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onAccept?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptionsExt-onAccept?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<TextPickerResult>
```

滑动弹窗中的选择器后，选项归位至选中项位置时，触发该回调，用于获取最终选择结果。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用onEnterSelectedArea接口。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TextPickerResult&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onChange?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptionsExt-onChange?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEnterSelectedArea

```TypeScript
onEnterSelectedArea?: Callback<TextPickerResult>
```

滑动过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。

> **说明：**
> 
> 在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此，
> 回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TextPickerResult&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onEnterSelectedArea?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptionsExt-onEnterSelectedArea?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onScrollStop

```TypeScript
onScrollStop?: Callback<TextPickerResult>
```

滑动弹窗中的选择器的选择列停止时，触发该回调，用于监听物理滑动停止事件。两者触发时机略有不同，onChange侧重于选项选中状态，onScrollStop侧重于滑动动作结束。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TextPickerResult&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-onScrollStop?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptionsExt-onScrollStop?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundStyle

```TypeScript
selectedBackgroundStyle?: PickerBackgroundStyle
```

设置选中项背景样式。

> 默认值：
> 
> &lt;br&gt;{
> &lt;br&gt;color: \$r('sys.color.comp_background_tertiary'),
> &lt;br&gt;borderRadius: \$r('sys.float.corner_radius_level12')
> &lt;br&gt;}

**Type:** [PickerBackgroundStyle](../arkts-apis/arkts-arkui-textpicker-pickerbackgroundstyle-i.md)

**Default:** { color: $r('sys.color.comp_background_tertiary'), borderRadius: $r('sys.float.corner_radius_level12') }

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-selectedBackgroundStyle?: PickerBackgroundStyle--><!--Device-TextPickerDialogOptionsExt-selectedBackgroundStyle?: PickerBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedTextStyle

```TypeScript
selectedTextStyle?: TextPickerTextStyle
```

设置选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。

> 默认值：
> 
> &lt;br&gt;{
> &lt;br&gt;color: '#ff007dff',
> &lt;br&gt;font: {
> &lt;br&gt;size: '20fp',
> &lt;br&gt;weight: FontWeight.Medium
> &lt;br&gt;},
> &lt;br&gt;minFontSize: 0,
> &lt;br&gt;maxFontSize: 0,
> &lt;br&gt;overflow: TextOverflow.CLIP
> &lt;br&gt;}

**Type:** [TextPickerTextStyle](arkts-arkui-textpickertextstyle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-selectedTextStyle?: TextPickerTextStyle--><!--Device-TextPickerDialogOptionsExt-selectedTextStyle?: TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

设置弹窗背板的阴影。

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM

**Type:** [ShadowOptions](../arkts-apis/arkts-arkui-common-shadowoptions-i.md) \| ShadowStyle

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-shadow?: ShadowOptions | ShadowStyle--><!--Device-TextPickerDialogOptionsExt-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

设置弹窗的系统材质。当需要使用系统预定义的材质效果以快速实现统一的视觉效果时设置此参数。

> **说明：**
> 
> - 默认值为ImmersiveOptions的style为ImmersiveStyle.ULTRA_THICK的ImmersiveMaterial对象，设置undefined时与默认值保持一致。
> 不同的材质具有不同的效果。
> - 该接口影响背景色[backgroundColor](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundcolor)、背景模糊
> [backgroundBlurStyle]
> {@link CommonMethod#backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions)}
> 、背景效果[backgroundEffect](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundeffect)、边框颜色
> [borderColor](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#bordercolor)、边框宽度[borderWidth](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#borderwidth)、阴影
> [shadow](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#shadow)，当设置系统材质时，上述接口不生效。

**Type:** [SystemUiMaterial](../arkts-apis/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextPickerDialogOptionsExt-systemMaterial?: SystemUiMaterial--><!--Device-TextPickerDialogOptionsExt-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: TextPickerTextStyle
```

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。

默认值：

&lt;br&gt;{&lt;br&gt;color: '#ff182431',&lt;br&gt;font: {&lt;br&gt;size: '16fp',&lt;br&gt;weight: FontWeight.Regular&lt;br&gt;},&lt;br&gt;minFontSize: 0,&lt;br&gt;maxFontSize: 0,&lt;br&gt;overflow: TextOverflow.CLIP&lt;br&gt;}

**Type:** [TextPickerTextStyle](arkts-arkui-textpickertextstyle-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptionsExt-textStyle?: TextPickerTextStyle--><!--Device-TextPickerDialogOptionsExt-textStyle?: TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

