# ChildrenMainSize

Indicates children main size.

**Since:** 12

<!--Device-unnamed-declare class ChildrenMainSize--><!--Device-unnamed-declare class ChildrenMainSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(childDefaultSize: number)
```

Creates an instance of ChildrenMainSize.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-constructor(childDefaultSize: number)--><!--Device-ChildrenMainSize-constructor(childDefaultSize: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [childDefaultSize](#childdefaultsize) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## splice

```TypeScript
splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void
```

Changes children main size by removing or replacing existing elements and/or adding new elements in place.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void--><!--Device-ChildrenMainSize-splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| deleteCount | number | No |
| childrenSize | Array&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## update

```TypeScript
update(index: number, childSize: number): void
```

Updates main size for specified child.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-update(index: number, childSize: number): void--><!--Device-ChildrenMainSize-update(index: number, childSize: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| childSize | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## childDefaultSize

```TypeScript
get childDefaultSize(): number
```

Get default size

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChildrenMainSize-get childDefaultSize(): number--><!--Device-ChildrenMainSize-get childDefaultSize(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
