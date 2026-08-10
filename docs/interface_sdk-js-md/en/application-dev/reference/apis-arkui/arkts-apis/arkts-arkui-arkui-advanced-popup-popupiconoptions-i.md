# PopupIconOptions

PopupIconOptions定义图标的属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PopupIconOptions--><!--Device-unnamed-export interface PopupIconOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Popup, PopupOptions, PopupButtonOptions, PopupIconOptions, PopupTextOptions } from 'kits/@kit.ArkUI';
```

## borderRadius

```TypeScript
borderRadius?: Length | BorderRadiuses
```

设置图标圆角。

默认值：`\$r('sys.float.ohos_id_corner_radius_default_s')`

**Type:** [Length](arkts-arkui-length-t.md) \| BorderRadiuses

**Default:** $r('sys.float.ohos_id_corner_radius_default_s')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupIconOptions-borderRadius?: Length | BorderRadiuses--><!--Device-PopupIconOptions-borderRadius?: Length | BorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fillColor

```TypeScript
fillColor?: ResourceColor
```

设置图标填充颜色。仅针对svg图源生效。 

默认不改变图标颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupIconOptions-fillColor?: ResourceColor--><!--Device-PopupIconOptions-fillColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

设置图标高度。

默认值：32VP

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 32.0_vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupIconOptions-height?: Dimension--><!--Device-PopupIconOptions-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

设置图标内容。

**ArkTS模式：** 该接口仅适用于ArkTS-Sta。

**ArkTS-Sta起始版本：** 23

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupIconOptions-image?: ResourceStr--><!--Device-PopupIconOptions-image?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

设置图标宽度。

默认值：32VP

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 32.0_vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupIconOptions-width?: Dimension--><!--Device-PopupIconOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

