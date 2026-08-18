# iteratorForEach

## Modules to Import

```TypeScript
```

## iteratorForEach

```TypeScript
export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void
```

Iterates over an iterator and executes the specified callback function for each element

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void--><!--Device-unnamed-export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | Iterator&lt;V&gt; | Yes | The iterator to iterate over |
| fn | (x: V) =&gt; void | Yes | The callback function to execute for each element of the iterator |

