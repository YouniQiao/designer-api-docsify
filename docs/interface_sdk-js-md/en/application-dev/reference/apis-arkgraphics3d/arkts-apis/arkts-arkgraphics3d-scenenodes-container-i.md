# Container

Defines a scene object container.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface Container--><!--Device-unnamed-export interface Container-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## append

```TypeScript
append(item: T): void
```

Append an item to the container.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Container-append(item: T): void--><!--Device-Container-append(item: T): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | the item append to the end of container |

## clear

```TypeScript
clear(): void
```

Clear all children.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Container-clear(): void--><!--Device-Container-clear(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## count

```TypeScript
count(): int
```

Obtains the number of nodes in the container.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Container-count(): int--><!--Device-Container-count(): int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| int | Number of nodes in the container. The value is a non-negative integer. |

## get

```TypeScript
get(index: int): T | null
```

Obtains a node of a given index. If no node is obtained, null is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Container-get(index: int): T | null--><!--Device-Container-get(index: int): T | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the node. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Object obtained. If no object is obtained, null is returned. |

## insertAfter

```TypeScript
insertAfter(item: T, sibling: T | null): void
```

Insert an item.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Container-insertAfter(item: T, sibling: T | null): void--><!--Device-Container-insertAfter(item: T, sibling: T | null): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | the item insert to the container |
| sibling | T \| null | Yes | insert after this item, insert to the head if sibling is null |

## remove

```TypeScript
remove(item: T): void
```

Remove an item from Container's children.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Container-remove(item: T): void--><!--Device-Container-remove(item: T): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | the item to be removed |

