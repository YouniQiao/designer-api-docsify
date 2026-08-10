# ScopeHelper

Provides APIs to define the valid range of a field. The constructor of this class creates comparable objects with lower and upper limits.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-class ScopeHelper<T extends ScopeComparable<T>>--><!--Device-util-class ScopeHelper<T extends ScopeComparable<T>>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## clamp

```TypeScript
clamp(value: T): T
```

Clamps a given value to the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-clamp(value: T): T--><!--Device-ScopeHelper-clamp(value: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | A ScopeType value |

**Return value:**

| Type | Description |
| --- | --- |
| T | Returns a ScopeType object that a given value is clamped to the current range. |

## constructor

```TypeScript
constructor(lowerObj: T, upperObj: T)
```

A constructor used to create a Scope instance with the lower and upper bounds specified.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-constructor(lowerObj: T, upperObj: T)--><!--Device-ScopeHelper-constructor(lowerObj: T, upperObj: T)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | T | Yes | A ScopeType value |
| upperObj | T | Yes | A ScopeType value |

## contains

```TypeScript
contains(value: T): boolean
```

Checks whether a given value is within the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-contains(value: T): boolean--><!--Device-ScopeHelper-contains(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | A ScopeType value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the value is within the current range return true,otherwise return false. |

## contains

```TypeScript
contains(range: ScopeHelper<T>): boolean
```

Checks whether a given range is within the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-contains(range: ScopeHelper<T>): boolean--><!--Device-ScopeHelper-contains(range: ScopeHelper<T>): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Yes | A Scope range |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the current range is within the given range return true,otherwise return false. |

## expand

```TypeScript
expand(lowerObj: T, upperObj: T): ScopeHelper<T>
```

Creates the smallest range that includes the current range and the given lower and upper bounds.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-expand(lowerObj: T, upperObj: T): ScopeHelper<T>--><!--Device-ScopeHelper-expand(lowerObj: T, upperObj: T): ScopeHelper<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | T | Yes | A ScopeType value |
| upperObj | T | Yes | A ScopeType value |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Returns the smallest range that includes the current range and the given lower and upper bounds. |

## expand

```TypeScript
expand(range: ScopeHelper<T>): ScopeHelper<T>
```

Creates the smallest range that includes the current range and a given range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-expand(range: ScopeHelper<T>): ScopeHelper<T>--><!--Device-ScopeHelper-expand(range: ScopeHelper<T>): ScopeHelper<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Yes | A Scope range object |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Returns the smallest range that includes the current range and a given range. |

## expand

```TypeScript
expand(value: T): ScopeHelper<T>
```

Creates the smallest range that includes the current range and a given value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-expand(value: T): ScopeHelper<T>--><!--Device-ScopeHelper-expand(value: T): ScopeHelper<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | A ScopeType value |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Returns the smallest range that includes the current range and a given value. |

## getLower

```TypeScript
getLower(): T
```

Obtains the lower bound of the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-getLower(): T--><!--Device-ScopeHelper-getLower(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | Returns the lower bound of the current range. |

## getUpper

```TypeScript
getUpper(): T
```

Obtains the upper bound of the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-getUpper(): T--><!--Device-ScopeHelper-getUpper(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | Returns the upper bound of the current range. |

## intersect

```TypeScript
intersect(range: ScopeHelper<T>): ScopeHelper<T>
```

Returns the intersection of a given range and the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-intersect(range: ScopeHelper<T>): ScopeHelper<T>--><!--Device-ScopeHelper-intersect(range: ScopeHelper<T>): ScopeHelper<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Yes | A Scope range object |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Returns the intersection of a given range and the current range. |

## intersect

```TypeScript
intersect(lowerObj: T, upperObj: T): ScopeHelper<T>
```

Returns the intersection of the current range and the range specified by the given lower and upper bounds.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-intersect(lowerObj: T, upperObj: T): ScopeHelper<T>--><!--Device-ScopeHelper-intersect(lowerObj: T, upperObj: T): ScopeHelper<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lowerObj | T | Yes | A ScopeType value |
| upperObj | T | Yes | A ScopeType value |

**Return value:**

| Type | Description |
| --- | --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md)&lt;T&gt; | Returns the intersection of the current range and the range specified by the given lower and upper bounds. |

## toString

```TypeScript
toString(): string
```

Obtains a string representation of the current range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScopeHelper-toString(): string--><!--Device-ScopeHelper-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns a string representation of the current range object. |

