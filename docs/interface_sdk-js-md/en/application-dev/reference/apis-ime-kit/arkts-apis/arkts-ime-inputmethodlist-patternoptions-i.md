# PatternOptions

Define pattern options of keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface PatternOptions--><!--Device-unnamed-export interface PatternOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { InputMethodListDialog } from 'InputMethodListDialog';
import { PatternOptions } from 'PatternOptions';
import { Pattern } from 'Pattern';
```

## action

```TypeScript
action: (index: int) => void
```

Mandatory. Callback invoked when the pattern option changes.

**Type:** (index: int) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PatternOptions-action: (index: int) => void--><!--Device-PatternOptions-action: (index: int) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## defaultSelected

```TypeScript
defaultSelected?: int
```

Optional. Default selected pattern.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PatternOptions-defaultSelected?: int--><!--Device-PatternOptions-defaultSelected?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## patterns

```TypeScript
patterns: Array<Pattern>
```

Mandatory. Resource of the pattern option.

**Type:** Array&lt;[Pattern](arkts-ime-inputmethodlist-pattern-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PatternOptions-patterns: Array<Pattern>--><!--Device-PatternOptions-patterns: Array<Pattern>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

