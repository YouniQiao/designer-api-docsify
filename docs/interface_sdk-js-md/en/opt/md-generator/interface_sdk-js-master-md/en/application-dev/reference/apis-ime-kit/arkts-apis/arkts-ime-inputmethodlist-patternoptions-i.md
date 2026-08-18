# PatternOptions

Define pattern options of keyboard.

**Since:** 23

<!--Device-unnamed-export interface PatternOptions--><!--Device-unnamed-export interface PatternOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
```

## action

```TypeScript
action: (index: number) => void
```

Mandatory. Callback invoked when the pattern option changes.

**Type:** (index: number) =&gt; void

**Since:** 23

<!--Device-PatternOptions-action: (index: int) => void--><!--Device-PatternOptions-action: (index: int) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## defaultSelected

```TypeScript
defaultSelected?: number
```

Optional. Default selected pattern.

**Type:** number

**Since:** 23

<!--Device-PatternOptions-defaultSelected?: int--><!--Device-PatternOptions-defaultSelected?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## patterns

```TypeScript
patterns: Array<Pattern>
```

Mandatory. Resource of the pattern option.

**Type:** Array&lt;[Pattern](arkts-ime-inputmethodlist-pattern-i.md)&gt;

**Since:** 23

<!--Device-PatternOptions-patterns: Array<Pattern>--><!--Device-PatternOptions-patterns: Array<Pattern>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework
