# UIFontConfig

```TypeScript
interface UIFontConfig
```

UI font configuration of the system.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from '@kit.ArkUI';
```

## fallbackGroups

```TypeScript
fallbackGroups: Array<UIFontFallbackGroupInfo>
```

List of system fallback font groups, used to specify the fallback fonts to use when the primary font does not support certain characters.

**Type:** Array&lt;[UIFontFallbackGroupInfo](arkts-arkui-font-uifontfallbackgroupinfo-i.md)&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontDir

```TypeScript
fontDir: Array<string>
```

List of paths where the system font files are located. Each array element is an absolute system path.

**Type:** Array&lt;string&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## generic

```TypeScript
generic: Array<UIFontGenericInfo>
```

List of generic font families supported by the system.

**Type:** Array&lt;[UIFontGenericInfo](arkts-arkui-font-uifontgenericinfo-i.md)&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
