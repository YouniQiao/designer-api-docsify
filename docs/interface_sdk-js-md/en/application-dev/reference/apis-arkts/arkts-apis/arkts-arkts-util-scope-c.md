# Scope

The Scope interface is used to describe the valid range of a field.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [ScopeHelper](arkts-arkts-util-scopehelper-c.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## clamp

```TypeScript
clamp(value: ScopeType): ScopeType
```

Limits a value to this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [clamp](arkts-arkts-util-scopehelper-c.md#clamp)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## constructor

```TypeScript
constructor(lowerObj: ScopeType, upperObj: ScopeType)
```

A constructor used to create a **Scope** object with the specified upper and lower limits.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** constructor

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

## contains

```TypeScript
contains(value: ScopeType): boolean
```

Checks whether a value is within this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [contains](arkts-arkts-util-lrucache-c.md#contains)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## contains

```TypeScript
contains(range: Scope): boolean
```

Checks whether a range is within this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [contains](arkts-arkts-util-lrucache-c.md#contains)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## expand

```TypeScript
expand(lowerObj: ScopeType, upperObj: ScopeType): Scope
```

Obtains the union set of this **Scope** and the given lower and upper limits.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** expand

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## expand

```TypeScript
expand(range: Scope): Scope
```

Obtains the union set of this **Scope** and the given **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** expand

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## expand

```TypeScript
expand(value: ScopeType): Scope
```

Obtains the union set of this **Scope** and the given value.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** expand

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## getLower

```TypeScript
getLower(): ScopeType
```

Obtains the lower limit of this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getLower](arkts-arkts-util-scopehelper-c.md#getlower)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## getUpper

```TypeScript
getUpper(): ScopeType
```

Obtains the upper limit of this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getUpper](arkts-arkts-util-scopehelper-c.md#getupper)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## intersect

```TypeScript
intersect(range: Scope): Scope
```

Obtains the intersection of this **Scope** and the given **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** intersect

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## intersect

```TypeScript
intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope
```

Obtains the intersection of this **Scope** and the given lower and upper limits.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** intersect

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## toString

```TypeScript
toString(): string
```

Obtains a string representation that contains this **Scope**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [toString](arkts-arkts-util-lrucache-c.md#tostring)

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |
