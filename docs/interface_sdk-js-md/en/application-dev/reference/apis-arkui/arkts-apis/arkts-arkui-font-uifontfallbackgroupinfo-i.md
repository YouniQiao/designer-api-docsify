# UIFontFallbackGroupInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-font-interface UIFontFallbackGroupInfo--><!--Device-font-interface UIFontFallbackGroupInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## fallback

```TypeScript
fallback: Array<UIFontFallbackInfo>
```

Fallback font list related.

**Type:** Array&lt;UIFontFallbackInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIFontFallbackGroupInfo-fallback: Array<UIFontFallbackInfo>--><!--Device-UIFontFallbackGroupInfo-fallback: Array<UIFontFallbackInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSetName

```TypeScript
fontSetName: string
```

Indicates which font set uses following list for fallback font if the font set name is "", it means that the following list can be fallback font for all font sets.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIFontFallbackGroupInfo-fontSetName: string--><!--Device-UIFontFallbackGroupInfo-fontSetName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

