# Container

Defines a scene object container.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Container<T>--><!--Device-unnamed-export interface Container<T>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## append

```TypeScript
append(item: T): void
```

Append an item to the container.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Container-clear(): void--><!--Device-Container-clear(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## count

ArkTS-Dyn:
```TypeScript
count(): number
```

ArkTS-Sta:
```TypeScript
count(): int
```

Obtains the number of nodes in the container.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Container-count(): int--><!--Device-Container-count(): int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Number of nodes in the container. The value is a non-negative integer. |

## get

ArkTS-Dyn:
```TypeScript
get(index: number): T | null
```

ArkTS-Sta:
```TypeScript
get(index: int): T | null
```

Obtains a node of a given index. If no node is obtained, null is returned.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Container-get(index: int): T | null--><!--Device-Container-get(index: int): T | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Index of the node. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Object obtained. If no object is obtained, null is returned. |

## insertAfter

```TypeScript
insertAfter(item: T, sibling: T | null): void
```

Insert an item.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Container-remove(item: T): void--><!--Device-Container-remove(item: T): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | the item to be removed |

