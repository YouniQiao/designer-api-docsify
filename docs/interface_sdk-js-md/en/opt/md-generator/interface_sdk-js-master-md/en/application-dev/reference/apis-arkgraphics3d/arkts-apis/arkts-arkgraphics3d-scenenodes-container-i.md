# Container

Defines a scene object container.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface Container--><!--Device-unnamed-export interface Container-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## append

```TypeScript
append(item: T): void
```

Append an item to the container.

**Since:** 23

**Deprecated since:** -1

<!--Device-Container-append(item: T): void--><!--Device-Container-append(item: T): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | T | Yes |

## clear

```TypeScript
clear(): void
```

Clear all children.

**Since:** 23

**Deprecated since:** -1

<!--Device-Container-clear(): void--><!--Device-Container-clear(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## count

```TypeScript
count(): number
```

Obtains the number of nodes in the container.

**Since:** 23

**Deprecated since:** -1

<!--Device-Container-count(): int--><!--Device-Container-count(): int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## get

```TypeScript
get(index: number): T | null
```

Obtains a node of a given index. If no node is obtained, null is returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-Container-get(index: int): T | null--><!--Device-Container-get(index: int): T | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## insertAfter

```TypeScript
insertAfter(item: T, sibling: T | null): void
```

Insert an item.

**Since:** 23

**Deprecated since:** -1

<!--Device-Container-insertAfter(item: T, sibling: T | null): void--><!--Device-Container-insertAfter(item: T, sibling: T | null): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | T | Yes |
| sibling | T \| null | Yes |

## remove

```TypeScript
remove(item: T): void
```

Remove an item from Container's children.

**Since:** 23

**Deprecated since:** -1

<!--Device-Container-remove(item: T): void--><!--Device-Container-remove(item: T): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | T | Yes |
