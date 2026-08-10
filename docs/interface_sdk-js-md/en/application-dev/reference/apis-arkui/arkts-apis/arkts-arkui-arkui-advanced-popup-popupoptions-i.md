# PopupOptions

PopupOptions定义Popup的具体样式参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PopupOptions--><!--Device-unnamed-export interface PopupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Popup, PopupOptions, PopupButtonOptions, PopupIconOptions, PopupTextOptions } from 'kits/@kit.ArkUI';
```

## buttons

```TypeScript
buttons?: [
    PopupButtonOptions | undefined,
    PopupButtonOptions | undefined
  ]
```

设置popup操作按钮，按钮最多设置两个。 

默认不显示按钮。

**Type:** [     PopupButtonOptions \| undefined,     PopupButtonOptions \| undefined   ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-buttons?: [    PopupButtonOptions | undefined,    PopupButtonOptions | undefined  ]--><!--Device-PopupOptions-buttons?: [    PopupButtonOptions | undefined,    PopupButtonOptions | undefined  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: Direction
```

布局方向。

默认值：Direction.Auto

**Type:** [Direction](arkts-arkui-direction-e.md)

**Default:** Direction.Auto

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-direction?: Direction--><!--Device-PopupOptions-direction?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: PopupIconOptions
```

设置popup图标。

**说明：**

当width和height设置异常值或0时不显示。

默认不显示图标。

**Type:** [PopupIconOptions](arkts-arkui-arkui-advanced-popup-popupiconoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-icon?: PopupIconOptions--><!--Device-PopupOptions-icon?: PopupIconOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxWidth

```TypeScript
maxWidth?: Dimension
```

设置popup的最大宽度，通过此接口popup可以自定义宽度显示。

**说明：**

1. 在使用引用资源类型时，规定其参数类型要与属性方法本身类型一致。2. maxWidth是数字类型，支持float和integer，例如`\$r('app.float.maxWidth')`、`\$r('app.integer.maxWidth')`。3. 当类型为Resource时，如果未设置单位，默认单位为px。

默认值：400vp

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 400.0_vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-maxWidth?: Dimension--><!--Device-PopupOptions-maxWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message?: PopupTextOptions
```

设置popup内容文本。

**说明：**

message不支持设置fontWeight。 

默认不显示内容文本。

**ArkTS模式：** 该接口仅适用于ArkTS-Sta。

**ArkTS-Sta起始版本：** 23

**Type:** [PopupTextOptions](arkts-arkui-arkui-advanced-popup-popuptextoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-message?: PopupTextOptions--><!--Device-PopupOptions-message?: PopupTextOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClose

```TypeScript
onClose?: VoidCallback
```

设置popup关闭按钮回调函数。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onClose?: VoidCallback--><!--Device-PopupOptions-onClose?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showClose

```TypeScript
showClose?: boolean | Resource
```

设置popup关闭按钮。

true：显示关闭按钮；false：不显示关闭按钮。

Resource：显示对应的图标。

默认值：true

**Type:** boolean \| Resource

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-showClose?: boolean | Resource--><!--Device-PopupOptions-showClose?: boolean | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: PopupTextOptions
```

设置popup标题文本。 

默认不显示标题文本。

**Type:** [PopupTextOptions](arkts-arkui-arkui-advanced-popup-popuptextoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-title?: PopupTextOptions--><!--Device-PopupOptions-title?: PopupTextOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

