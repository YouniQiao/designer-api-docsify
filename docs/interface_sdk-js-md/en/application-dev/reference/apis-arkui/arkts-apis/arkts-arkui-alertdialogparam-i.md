# AlertDialogParam

警告弹窗的样式。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface AlertDialogParam--><!--Device-unnamed-declare interface AlertDialogParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancel

```TypeScript
cancel?: VoidCallback
```

点击遮障层关闭dialog时的回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-cancel?: VoidCallback--><!--Device-AlertDialogParam-cancel?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

弹窗在竖直方向上的对齐方式。

默认值：DialogAlignment.Default 

**说明：**

若在UIExtension中设置showInSubWindow为true，弹窗将基于UIExtension的宿主窗口对齐。

**Type:** [DialogAlignment](arkts-arkui-alertdialog-dialogalignment-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-alignment?: DialogAlignment--><!--Device-AlertDialogParam-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

点击遮障层时，是否关闭弹窗。值为true表示关闭弹窗，值为false表示不关闭弹窗。

默认值：true

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-autoCancel?: boolean--><!--Device-AlertDialogParam-autoCancel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

弹窗背板模糊材质。

默认值：从API版本26.0.0开始，为BlurStyle.NONE，API版本26.0.0之前，为BlurStyle.COMPONENT_ULTRA_THICK。

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-backgroundBlurStyle?: BlurStyle--><!--Device-AlertDialogParam-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。

**Type:** [BackgroundBlurStyleOptions](arkts-arkui-common-backgroundblurstyleoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AlertDialogParam-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-AlertDialogParam-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

弹窗背板颜色。

默认值：Color.Transparent

**说明：**

backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-backgroundColor?: ResourceColor--><!--Device-AlertDialogParam-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

背景效果参数。当设置系统材质systemMaterial时，backgroundEffect不生效。默认值请参考BackgroundEffectOptions类型说明。

**Type:** [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AlertDialogParam-backgroundEffect?: BackgroundEffectOptions--><!--Device-AlertDialogParam-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors
```

设置弹窗背板的边框颜色。当设置系统材质systemMaterial时，borderColor不生效。

默认值：Color.Black

如果使用borderColor属性，需要和borderWidth属性一起使用。

**说明：**

当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md) \| EdgeColors \| LocalizedEdgeColors

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors--><!--Device-AlertDialogParam-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: BorderStyle | EdgeStyles
```

设置弹窗背板的边框样式。

默认值：BorderStyle.Solid

如果使用borderStyle属性，需要和borderWidth属性一起使用。

**Type:** [BorderStyle](arkts-arkui-enums-borderstyle-e.md) \| EdgeStyles

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-borderStyle?: BorderStyle | EdgeStyles--><!--Device-AlertDialogParam-borderStyle?: BorderStyle | EdgeStyles-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths
```

可分别设置4个边框宽度。当设置系统材质systemMaterial时，borderWidth不生效。

默认值：0

百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。

当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。

**说明：**

当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| EdgeWidths \| LocalizedEdgeWidths

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths--><!--Device-AlertDialogParam-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses
```

设置背板的圆角半径。

可分别设置4个圆角的半径。

默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }

圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。 

百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。

**说明：**

当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| LocalizedBorderRadiuses

**Default:** { topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-AlertDialogParam-cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

是否响应悬停态，值为true时，响应悬停态，值为false时，不响应悬停态。

默认值：false，默认不响应。

**说明：**

PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true时，可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。

**Type:** boolean

**Default:** false

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AlertDialogParam-enableHoverMode?: boolean--><!--Device-AlertDialogParam-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gridCount

```TypeScript
gridCount?: number
```

弹窗容器宽度所占用栅格数。栅格数为弹窗宽度的相对单位，值越大弹窗越宽。

默认值：4 

取值范围：大于等于0的整数。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-gridCount?: number--><!--Device-AlertDialogParam-gridCount?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

设置弹窗背板的高度。

**说明：**

- 弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域）。  
- 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-height?: Dimension--><!--Device-AlertDialogParam-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

悬停态下弹窗默认展示区域。

默认值：HoverModeAreaType.BOTTOM_SCREEN。

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AlertDialogParam-hoverModeArea?: HoverModeAreaType--><!--Device-AlertDialogParam-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

设置页面内弹窗蒙层效果。

**说明：**

- 默认值：ImmersiveMode.DEFAULT   
- 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AlertDialogParam-immersiveMode?: ImmersiveMode--><!--Device-AlertDialogParam-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。值为true时，弹窗为模态窗口，有蒙层。值为false时，弹窗为非模态窗口，无蒙层。

默认值：true，此时弹窗有蒙层。

**Type:** boolean

**Default:** true

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-isModal?: boolean--><!--Device-AlertDialogParam-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

设置弹窗显示层级。

**说明：**

- 默认值：LevelMode.OVERLAY。  
- 当且仅当showInSubWindow属性设置为false时生效。

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AlertDialogParam-levelMode?: LevelMode--><!--Device-AlertDialogParam-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

设置弹窗显示的顺序。

**说明：**

- 默认值：LevelOrder.clamp(0)   
- 不支持动态刷新顺序。

**Type:** [LevelOrder](arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returns by LevelOrder.clamp(0)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogParam-levelOrder?: LevelOrder--><!--Device-AlertDialogParam-levelOrder?: LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: number
```

设置页面级弹窗需要显示的层级下的[getUniqueId](arkts-arkui-framenode-c.md#getuniqueid)。仅在levelMode属性设置为LevelMode.EMBEDDED时生效。

取值范围：大于等于0的数字。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AlertDialogParam-levelUniqueId?: number--><!--Device-AlertDialogParam-levelUniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

默认值：{ x: 0, y: 0, width: '100%', height: '100%' } 

**说明：**

showInSubWindow为true时，maskRect不生效。

**Type:** [Rectangle](arkts-arkui-common-rectangle-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-maskRect?: Rectangle--><!--Device-AlertDialogParam-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: ResourceStr
```

弹窗内容。

API version 20之前，弹窗内容的对齐方式为左对齐。

API version 20及之后，弹窗内容的对齐方式为居中对齐。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-message: ResourceStr--><!--Device-AlertDialogParam-message: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

弹窗相对alignment所在位置的偏移量。dx表示水平方向偏移，正值为向右偏移，负值为向左偏移；dy表示垂直方向偏移，正值为向下偏移，负值为向上偏移。

默认值：{ dx: 0 , dy: 0 }

**Type:** [Offset](arkts-arkui-componentutils-offset-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-offset?: Offset--><!--Device-AlertDialogParam-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: Callback<void>
```

弹窗弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。

4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AlertDialogParam-onDidAppear?: Callback<void>--><!--Device-AlertDialogParam-onDidAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: Callback<void>
```

弹窗消失后的事件回调。

**说明：**

正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AlertDialogParam-onDidDisappear?: Callback<void>--><!--Device-AlertDialogParam-onDidDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: Callback<void>
```

弹窗显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AlertDialogParam-onWillAppear?: Callback<void>--><!--Device-AlertDialogParam-onWillAppear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: Callback<void>
```

弹窗退出动效前的事件回调。

**说明：**

正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AlertDialogParam-onWillDisappear?: Callback<void>--><!--Device-AlertDialogParam-onWillDisappear?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissDialogAction>
```

交互式关闭回调函数。当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。

**说明：**

1.在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。典型场景如弹窗中存在未保存的表单数据时，拦截关闭并提示用户保存。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。

2.在onWillDismiss回调中，不能再做onWillDismiss拦截。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;DismissDialogAction&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-onWillDismiss?: Callback<DismissDialogAction>--><!--Device-AlertDialogParam-onWillDismiss?: Callback<DismissDialogAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

设置弹窗背板的阴影。 

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。

**Type:** [ShadowOptions](arkts-arkui-common-shadowoptions-i.md) \| ShadowStyle

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-shadow?: ShadowOptions | ShadowStyle--><!--Device-AlertDialogParam-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。

默认值：false，弹窗显示在应用内，而非独立子窗口。

**说明：**showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。

**Type:** boolean

**Default:** false

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-showInSubWindow?: boolean--><!--Device-AlertDialogParam-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
subtitle?: ResourceStr
```

弹窗副标题。

API version 20之前，弹窗副标题的对齐方式为左对齐。

API version 20及之后，弹窗副标题的对齐方式为居中对齐。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-subtitle?: ResourceStr--><!--Device-AlertDialogParam-subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

设置弹窗的系统材质。

**说明：**

- 默认值：[ImmersiveOptions](../../../reference/apis-arkui/arkts-apis-uimaterial.md#immersiveoptions)的style为  
ImmersiveStyle.ULTRA_THICK的  
[ImmersiveMaterial](../../../reference/apis-arkui/arkts-apis-uimaterial.md#immersivematerial)对象。设置undefined时与默认值保持一致。  
- 不同的材质具有不同的效果，该接口影响背景色[backgroundColor](arkts-arkui-common-commonmethod-i.md#backgroundcolor)、背景模糊  
[backgroundBlurStyle](arkts-arkui-common-commonmethod-i.md#backgroundblurstyle)、背景效果[backgroundEffect](arkts-arkui-common-commonmethod-i.md#backgroundeffect)、边框颜色  
[borderColor](arkts-arkui-common-commonmethod-i.md#bordercolor)、边框宽度[borderWidth](arkts-arkui-common-commonmethod-i.md#borderwidth)、阴影  
[shadow](arkts-arkui-common-commonmethod-i.md#shadow)，不建议与上述接口一起使用。

**Type:** [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AlertDialogParam-systemMaterial?: SystemUiMaterial--><!--Device-AlertDialogParam-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: TextStyle
```

设置弹窗message内容的文本样式。

**Type:** [TextStyle](arkts-arkui-styledstring-textstyle-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-textStyle?: TextStyle--><!--Device-AlertDialogParam-textStyle?: TextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

弹窗标题。

API version 20之前，弹窗标题的对齐方式为左对齐。

API version 20及之后，弹窗标题的对齐方式为居中对齐。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParam-title?: ResourceStr--><!--Device-AlertDialogParam-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

设置弹窗显示和退出的过渡效果。

**说明：**

1.如果不设置，则使用默认的显示/退出动效。

2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。

3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。

**Type:** [TransitionEffect](arkts-arkui-common-transitioneffect-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-transition?: TransitionEffect--><!--Device-AlertDialogParam-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

设置弹窗背板的宽度。

**说明：**

- 弹窗宽度默认最大值：400vp。  
- 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlertDialogParam-width?: Dimension--><!--Device-AlertDialogParam-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

