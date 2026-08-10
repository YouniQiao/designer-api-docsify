# CutoutInfo

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-display-interface CutoutInfo--><!--Device-display-interface CutoutInfo-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## boundingRects

```TypeScript
readonly boundingRects: Array<Rect>
```

挖孔、刘海等区域的边界矩形。如果没有挖孔、刘海等区域，数组返回为空。

**Type:** Array&lt;Rect&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CutoutInfo-readonly boundingRects: Array<Rect>--><!--Device-CutoutInfo-readonly boundingRects: Array<Rect>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## waterfallDisplayAreaRects

```TypeScript
readonly waterfallDisplayAreaRects: WaterfallDisplayAreaRects
```

瀑布屏曲面部分显示区域。

**Type:** [WaterfallDisplayAreaRects](arkts-arkui-display-waterfalldisplayarearects-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CutoutInfo-readonly waterfallDisplayAreaRects: WaterfallDisplayAreaRects--><!--Device-CutoutInfo-readonly waterfallDisplayAreaRects: WaterfallDisplayAreaRects-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

