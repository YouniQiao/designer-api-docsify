# ChildrenMainSize

Indicates children main size.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ChildrenMainSize--><!--Device-unnamed-export declare class ChildrenMainSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(childDefaultSize: double)
```

Creates an instance of ChildrenMainSize.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildrenMainSize-constructor(childDefaultSize: double)--><!--Device-ChildrenMainSize-constructor(childDefaultSize: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| childDefaultSize | double | Yes | default main size, in vp. If the main axis is vertical, it indicates height. If the main axis is horizontal, it indicates width. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## splice

```TypeScript
splice(start: int, deleteCount?: int, childrenSize?: Array<double>): void
```

Changes children main size by removing or replacing existing elements and/or adding new elements in place.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildrenMainSize-splice(start: int, deleteCount?: int, childrenSize?: Array<double>): void--><!--Device-ChildrenMainSize-splice(start: int, deleteCount?: int, childrenSize?: Array<double>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | Zero-based index at which to start changing the children main size. |
| deleteCount | int | No | Indicating the number of children main size to remove from start. |
| childrenSize | Array&lt;double&gt; | No | Add the new children main size, beginning from start. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## update

```TypeScript
update(index: int, childSize: double): void
```

Updates main size for specified child.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildrenMainSize-update(index: int, childSize: double): void--><!--Device-ChildrenMainSize-update(index: int, childSize: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | index of child to be updated. |
| childSize | double | Yes | new section options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## childDefaultSize

```TypeScript
get childDefaultSize(): double
```

Get default size

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildrenMainSize-get childDefaultSize(): double--><!--Device-ChildrenMainSize-get childDefaultSize(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

