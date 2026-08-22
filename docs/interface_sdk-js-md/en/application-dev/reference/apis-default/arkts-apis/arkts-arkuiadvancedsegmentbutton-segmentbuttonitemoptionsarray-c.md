# SegmentButtonItemOptionsArray

The class for SegmentButton item options array.

**Inheritance/Implementation:** SegmentButtonItemOptionsArray extends Array<SegmentButtonItemOptions>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare class SegmentButtonItemOptionsArray--><!--Device-unnamed-declare class SegmentButtonItemOptionsArray-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(elements: SegmentButtonItemTuple)
```

The constructor used to create a SegmentButtonItemOptionsArray object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-constructor(elements: SegmentButtonItemTuple)--><!--Device-SegmentButtonItemOptionsArray-constructor(elements: SegmentButtonItemTuple)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](arkts-segmentbuttonitemtuple-t.md) | Yes | The SegmentButton items. |

## create

```TypeScript
static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray
```

The function used to create a SegmentButtonItemOptionsArray object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray--><!--Device-SegmentButtonItemOptionsArray-static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](arkts-segmentbuttonitemtuple-t.md) | Yes | The SegmentButton items. |

**Return value:**

| Type | Description |
| --- | --- |
| [SegmentButtonItemOptionsArray](arkts-arkuiadvancedsegmentbutton-segmentbuttonitemoptionsarray-c.md) | Returns the a new SegmentButtonItemOptionsArray object. |

## pop

```TypeScript
pop(): SegmentButtonItemOptions | undefined
```

Removes the last element from SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-pop(): SegmentButtonItemOptions | undefined--><!--Device-SegmentButtonItemOptionsArray-pop(): SegmentButtonItemOptions | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SegmentButtonItemOptions](arkts-arkuiadvancedsegmentbutton-segmentbuttonitemoptions-c.md) \| undefined | Returns the removed element. |

## push

```TypeScript
push(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int
```

Appends new elements to the end of SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-push(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int--><!--Device-SegmentButtonItemOptionsArray-push(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the new length of SegmentButtonItemOptionsArray. |

## push

```TypeScript
push(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
  ): int
```

Appends new elements to the end of SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |
| item2 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the new length of SegmentButtonItemOptionsArray. |

## push

```TypeScript
push(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
  ): int
```

Appends new elements to the end of SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-push(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |
| item2 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |
| item3 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the new length of SegmentButtonItemOptionsArray. |

## shift

```TypeScript
shift(): SegmentButtonItemOptions | undefined
```

Removes the first element from SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-shift(): SegmentButtonItemOptions | undefined--><!--Device-SegmentButtonItemOptionsArray-shift(): SegmentButtonItemOptions | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SegmentButtonItemOptions](arkts-arkuiadvancedsegmentbutton-segmentbuttonitemoptions-c.md) \| undefined | Returns the removed element. |

## splice

```TypeScript
splice(start: int, deleteCount: int, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]
```

Changes the elements of SegmentButtonItemOptionsArray by removing or replacing existing elements and/or adding new elements in place.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-splice(start: int, deleteCount: int, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]--><!--Device-SegmentButtonItemOptionsArray-splice(start: int, deleteCount: int, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | The zero-based location in the array from which to start removing elements. <br>The value should be an integer. |
| deleteCount | int | Yes | The number of elements to remove. <br>The value should be an integer. |
| items | [SegmentButtonItemOptions](arkts-arkuiadvancedsegmentbutton-segmentbuttonitemoptions-c.md)[] | Yes | Elements to insert into the array in place of the deleted elements. |

**Return value:**

| Type | Description |
| --- | --- |
| [SegmentButtonItemOptions](arkts-arkuiadvancedsegmentbutton-segmentbuttonitemoptions-c.md)[] | Returns a SegmentButtonItemOptions array containing the deleted elements. |

## unshift

```TypeScript
unshift(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int
```

Appends new elements to the start of SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-unshift(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int--><!--Device-SegmentButtonItemOptionsArray-unshift(item: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the new length of SegmentButtonItemOptionsArray. |

## unshift

```TypeScript
unshift(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,

  ): int
```

Appends new elements to the start of SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |
| item2 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the new length of SegmentButtonItemOptionsArray. |

## unshift

```TypeScript
unshift(
    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,
  ): int
```

Appends new elements to the start of SegmentButtonItemOptionsArray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int--><!--Device-SegmentButtonItemOptionsArray-unshift(    item1: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item2: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,    item3: SegmentButtonTextItem | SegmentButtonIconItem | SegmentButtonIconTextItem,  ): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item1 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |
| item2 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |
| item3 | [SegmentButtonTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttontextitem-i.md) \| [SegmentButtonIconItem](arkts-arkuiadvancedsegmentbutton-segmentbuttoniconitem-i.md) \| [SegmentButtonIconTextItem](arkts-arkuiadvancedsegmentbutton-segmentbuttonicontextitem-i.md) | Yes | New element to add to SegmentButtonItemOptionsArray. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the new length of SegmentButtonItemOptionsArray. |

