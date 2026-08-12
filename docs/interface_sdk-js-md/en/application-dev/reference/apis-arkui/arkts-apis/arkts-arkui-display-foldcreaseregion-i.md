# FoldCreaseRegion

Describes the crease region of a foldable device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-display-interface FoldCreaseRegion--><!--Device-display-interface FoldCreaseRegion-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## creaseRects

```TypeScript
readonly creaseRects: Array<Rect>
```

Crease region.

**Type:** Array&lt;Rect&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldCreaseRegion-readonly creaseRects: Array<Rect>--><!--Device-FoldCreaseRegion-readonly creaseRects: Array<Rect>-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayId

```TypeScript
readonly displayId: long
```

ID of the display where the crease is located.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldCreaseRegion-readonly displayId: long--><!--Device-FoldCreaseRegion-readonly displayId: long-End-->

**System capability:** SystemCapability.Window.SessionManager

