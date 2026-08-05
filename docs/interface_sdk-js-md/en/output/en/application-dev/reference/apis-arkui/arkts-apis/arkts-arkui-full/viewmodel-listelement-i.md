# ListElement

The \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ component provides a list container.

**Inheritance/Implementation:** ListElement extends [Element](viewmodel-element-i.md)

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

<!--Device-unnamed-export interface ListElement extends Element--><!--Device-unnamed-export interface ListElement extends Element-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## collapseGroup

```TypeScript
collapseGroup(param: {
    /**
     * groupid: ID of the group to collapse.
     * All groups are collapsed when groupid is not specified.
     *
     *****/
    groupid: string;
  }): void
```

Collapses a group.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-collapseGroup(param: {    /**     * groupid: ID of the group to collapse.     * All groups are collapsed when groupid is not specified.     *     *****/    groupid: string;  }): void--><!--Device-ListElement-collapseGroup(param: {    /**     * groupid: ID of the group to collapse.     * All groups are collapsed when groupid is not specified.     *     *****/    groupid: string;  }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | {     /**      * groupid: ID of the group to collapse.      * All groups are collapsed when groupid is not specified.      *      * @type { string }      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @famodelonly      * @since 4 dynamiconly      */     groupid: string;   } | Yes |  |

## currentOffset

```TypeScript
currentOffset(): CurrentOffsetResultValue
```

Returns the offset of the current scrolling. The return value type is Object.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-currentOffset(): CurrentOffsetResultValue--><!--Device-ListElement-currentOffset(): CurrentOffsetResultValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## expandGroup

```TypeScript
expandGroup(param: {
    /**
     * groupid: ID of the group to expand.
     * All groups are expanded when groupid is not specified.
     *
     *****/
    groupid: string;
  }): void
```

Expands a group.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-expandGroup(param: {    /**     * groupid: ID of the group to expand.     * All groups are expanded when groupid is not specified.     *     *****/    groupid: string;  }): void--><!--Device-ListElement-expandGroup(param: {    /**     * groupid: ID of the group to expand.     * All groups are expanded when groupid is not specified.     *     *****/    groupid: string;  }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | {     /**      * groupid: ID of the group to expand.      * All groups are expanded when groupid is not specified.      *      * @type { string }      * @syscap SystemCapability.ArkUI.ArkUI.Full      * @famodelonly      * @since 4 dynamiconly      */     groupid: string;   } | Yes |  |

## scrollArrow

```TypeScript
scrollArrow(params: { reverse: boolean; smooth: boolean }): void
```

If reverse is set to false (default value), the list scrolls towards the bottom for a certain distance. If there is no sufficient distance, the list scrolls to the bottom. If reverse is set to true, the list scrolls towards the top for a certain distance. If there is no sufficient distance, the list scrolls to the top. If smooth is set to false (default value), the list is directly scrolled. If smooth is set to true, the list is smoothly scrolled.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollArrow(params: { reverse: boolean; smooth: boolean }): void--><!--Device-ListElement-scrollArrow(params: { reverse: boolean; smooth: boolean }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | { reverse: boolean; smooth: boolean } | Yes |  |

## scrollBottom

```TypeScript
scrollBottom(param: { smooth: boolean }): void
```

If smooth is set to false (default value), the list is directly scrolled to the bottom. If smooth is set to true, the list is smoothly scrolled to the bottom.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollBottom(param: { smooth: boolean }): void--><!--Device-ListElement-scrollBottom(param: { smooth: boolean }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | { smooth: boolean } | Yes |  |

## scrollBy

```TypeScript
scrollBy(data: ScrollParam): void
```

Scrolls the list for a certain distance. This method applies only to smart TVs.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollBy(data: ScrollParam): void--><!--Device-ListElement-scrollBy(data: ScrollParam): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## scrollPage

```TypeScript
scrollPage(params: { reverse: boolean; smooth: boolean }): void
```

If reverse is set to false (default value), the next page is displayed. If there is no next page, the list scrolls to the bottom. If reverse is set to true, the previous page is displayed. If there is no previous page, the list scrolls to the top. If smooth is set to false (default value), the list is directly scrolled to another page. If smooth is set to true, the list is smoothly scrolled to another page.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollPage(params: { reverse: boolean; smooth: boolean }): void--><!--Device-ListElement-scrollPage(params: { reverse: boolean; smooth: boolean }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | { reverse: boolean; smooth: boolean } | Yes |  |

## scrollTo

```TypeScript
scrollTo(position: ListScrollToOptions): void
```

Scrolls the list to the position of the item at the specified index.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollTo(position: ListScrollToOptions): void--><!--Device-ListElement-scrollTo(position: ListScrollToOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## scrollTop

```TypeScript
scrollTop(param: { smooth: boolean }): void
```

If smooth is set to false (default value), the list is directly scrolled to the top. If smooth is set to true, the list is smoothly scrolled to the top.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollTop(param: { smooth: boolean }): void--><!--Device-ListElement-scrollTop(param: { smooth: boolean }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | { smooth: boolean } | Yes |  |

