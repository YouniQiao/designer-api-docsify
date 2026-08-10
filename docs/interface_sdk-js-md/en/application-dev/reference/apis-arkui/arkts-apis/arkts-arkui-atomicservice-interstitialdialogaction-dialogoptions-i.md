# DialogOptions

设置弹框特有的属性以及提供给用户自定义的点击触发动作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare interface DialogOptions--><!--Device-unnamed-export declare interface DialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IconStyle, TitlePosition, BottomOffset, InterstitialDialogAction } from 'kits/@kit.ArkUI';
```

## backgroundImage

```TypeScript
backgroundImage?: Resource
```

弹框背景图片。默认为纯色背景，颜色值为#EBEEF5。

**Type:** [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-backgroundImage?: Resource--><!--Device-DialogOptions-backgroundImage?: Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottomOffsetType

```TypeScript
bottomOffsetType?: BottomOffset
```

弹框距离底部偏移类型，需根据是否存在菜单栏选择对应值。默认值为BottomOffset.OFFSET_FOR_NONE。

**Type:** [BottomOffset](arkts-arkui-atomicservice-interstitialdialogaction-bottomoffset-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-bottomOffsetType?: BottomOffset--><!--Device-DialogOptions-bottomOffsetType?: BottomOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foregroundImage

```TypeScript
foregroundImage?: Resource
```

弹框前景图片。默认为空，即不显示前景图片。

**Type:** [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-foregroundImage?: Resource--><!--Device-DialogOptions-foregroundImage?: Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconStyle

```TypeScript
iconStyle?: IconStyle
```

关闭按钮图标的样式（亮调或者暗调）。默认值：IconStyle.LIGHT

**Type:** [IconStyle](arkts-arkui-atomicservice-interstitialdialogaction-iconstyle-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-iconStyle?: IconStyle--><!--Device-DialogOptions-iconStyle?: IconStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDialogClick

```TypeScript
onDialogClick?: Callback<void>
```

点击弹框任意位置后触发的用户自定义动作。默认调用closeDialog方法关闭弹框。说明：点击关闭按钮区域时仅触发onDialogClose，不触发本回调；若需同时触发，请在onDialogClose中显式调用本回调逻辑。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-onDialogClick?: Callback<void>--><!--Device-DialogOptions-onDialogClick?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDialogClose

```TypeScript
onDialogClose?: Callback<void>
```

点击关闭按钮后触发的用户自定义动作。默认调用closeDialog方法关闭弹框。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-onDialogClose?: Callback<void>--><!--Device-DialogOptions-onDialogClose?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
subtitle?: ResourceStr
```

弹框副标题文本。默认为空字符串。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-subtitle?: ResourceStr--><!--Device-DialogOptions-subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitleColor

```TypeScript
subtitleColor?: ResourceStr | Color
```

弹框副标题文本颜色。默认为\$r('sys.color.ohos_id_color_text_secondary_contrary')。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) \| Color

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-subtitleColor?: ResourceStr | Color--><!--Device-DialogOptions-subtitleColor?: ResourceStr | Color-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

弹框主标题文本。默认为空字符串。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-title?: ResourceStr--><!--Device-DialogOptions-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleColor

```TypeScript
titleColor?: ResourceStr | Color
```

弹框主标题文本颜色。默认为\$r('sys.color.ohos_id_color_text_primary_contrary')。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) \| Color

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-titleColor?: ResourceStr | Color--><!--Device-DialogOptions-titleColor?: ResourceStr | Color-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titlePosition

```TypeScript
titlePosition?: TitlePosition
```

主标题在弹框中的位置，在副标题的上方或者在副标题的下方。需设置subtitle属性后本参数才生效。默认值：TitlePosition.TOP

**Type:** [TitlePosition](arkts-arkui-atomicservice-interstitialdialogaction-titleposition-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-titlePosition?: TitlePosition--><!--Device-DialogOptions-titlePosition?: TitlePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uiContext

```TypeScript
uiContext: UIContext
```

UI上下文实例。

**Type:** [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DialogOptions-uiContext: UIContext--><!--Device-DialogOptions-uiContext: UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

