# PopupV2InitInfo

定义PopupV2的具体样式参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface PopupV2InitInfo--><!--Device-unnamed-export interface PopupV2InitInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PopupV2Button, PopupV2, PopupV2InitInfo } from 'kits/@kit.ArkUI';
```

## buttons

```TypeScript
buttons?: [PopupV2Button | undefined, PopupV2Button | undefined]
```

设置PopupV2操作按钮，按钮最多设置两个。默认不显示按钮。

默认值：[{ text: '' }, { text: '' }]

**Type:** [PopupV2Button \| undefined, PopupV2Button \| undefined]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-buttons?: [PopupV2Button | undefined, PopupV2Button | undefined]--><!--Device-PopupV2InitInfo-buttons?: [PopupV2Button | undefined, PopupV2Button | undefined]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: Direction
```

布局方向。

默认值：Direction.Auto

**Type:** [Direction](arkts-arkui-direction-e.md)

**Default:** Direction.Auto

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-direction?: Direction--><!--Device-PopupV2InitInfo-direction?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

设置PopupV2图标。

**说明：** 默认值：''，不显示图标。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-icon?: ResourceStr--><!--Device-PopupV2InitInfo-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconModifier

```TypeScript
iconModifier?: ImageModifier
```

设置图标属性，如图标颜色、大小、边框等。

默认值：undefined，使用系统图标属性。

**Type:** [ImageModifier](../arkts-components/arkts-arkui-imagemodifier-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-iconModifier?: ImageModifier--><!--Device-PopupV2InitInfo-iconModifier?: ImageModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxWidth

```TypeScript
maxWidth?: Dimension
```

设置PopupV2的最大宽度，通过此接口PopupV2可以自定义宽度显示。

默认值：400vp

**说明：**

1. 在使用引用资源类型时，规定其参数类型要与属性方法本身类型一致。2. maxWidth是数字类型，支持float和整型，例如`\$r('app.float.maxWidth')`、`\$r('app.integer.maxWidth')`。3. 当类型为Resource时，如果未设置单位，默认单位为px。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 400.0_vp

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-maxWidth?: Dimension--><!--Device-PopupV2InitInfo-maxWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: ResourceStr
```

设置PopupV2内容文本。

**说明：** 默认值：''，不显示内容文本。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-message: ResourceStr--><!--Device-PopupV2InitInfo-message: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## messageModifier

```TypeScript
messageModifier?: TextModifier
```

设置内容文本属性，如设置内容文本颜色、字体大小、字重等。

默认值：undefined，使用系统内容文本属性。

**Type:** TextModifier

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-messageModifier?: TextModifier--><!--Device-PopupV2InitInfo-messageModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClose

```TypeScript
onClose?: VoidCallback
```

设置PopupV2关闭按钮回调函数。

默认不设置关闭按钮回调函数。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-onClose?: VoidCallback--><!--Device-PopupV2InitInfo-onClose?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showClose

```TypeScript
showClose?: boolean | Resource
```

设置PopupV2关闭按钮。true：显示关闭按钮；false：不显示关闭按钮。Resource类型：显示对应的图标。

默认值：true

**Type:** boolean \| Resource

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-showClose?: boolean | Resource--><!--Device-PopupV2InitInfo-showClose?: boolean | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

设置PopupV2标题文本。

**说明：** 默认值：''，不显示标题文本。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-title?: ResourceStr--><!--Device-PopupV2InitInfo-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleModifier

```TypeScript
titleModifier?: TextModifier
```

设置标题文本属性，如设置标题颜色、字体大小、字重等。

默认值：undefined，使用系统标题文本属性。

**Type:** TextModifier

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2InitInfo-titleModifier?: TextModifier--><!--Device-PopupV2InitInfo-titleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

