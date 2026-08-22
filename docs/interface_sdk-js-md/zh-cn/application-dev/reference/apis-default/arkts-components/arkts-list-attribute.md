# ListAttribute

除支持通用属性和[滚动组件通用属性](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#属性)外，还支持 以下属性：

> **说明：**
> 
> List组件通用属性clip的默认值为true。

**继承/实现关系：** ListAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface ListAttribute--><!--Device-unnamed-export declare interface ListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignListItem

```TypeScript
alignListItem(value: ListItemAlign | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-alignListItem(value: ListItemAlign | undefined): this--><!--Device-ListAttribute-alignListItem(value: ListItemAlign | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListItemAlign](arkts-list-listitemalign-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ListAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-attributeModifier(modifier: AttributeModifier<ListAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ListAttribute-attributeModifier(modifier: AttributeModifier<ListAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ListAttribute](arkts-list-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## backPressBehavior

```TypeScript
backPressBehavior(behavior: ListBackPressBehavior | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-backPressBehavior(behavior: ListBackPressBehavior | undefined): this--><!--Device-ListAttribute-backPressBehavior(behavior: ListBackPressBehavior | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| behavior | [ListBackPressBehavior](arkts-list-listbackpressbehavior-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cachedCount

```TypeScript
cachedCount(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-cachedCount(value: int | undefined): this--><!--Device-ListAttribute-cachedCount(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cachedCount

```TypeScript
cachedCount(count: int | CacheCountInfo | undefined, show: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-cachedCount(count: int | CacheCountInfo | undefined, show: boolean | undefined): this--><!--Device-ListAttribute-cachedCount(count: int | CacheCountInfo | undefined, show: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | int \| [CacheCountInfo](../../apis-arkui/arkts-apis/arkts-arkui-cachecountinfo-i.md) \| undefined | 是 |  |
| show | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## chainAnimation

```TypeScript
chainAnimation(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-chainAnimation(value: boolean | undefined): this--><!--Device-ListAttribute-chainAnimation(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## chainAnimationOptions

```TypeScript
chainAnimationOptions(value: ChainAnimationOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-chainAnimationOptions(value: ChainAnimationOptions | undefined): this--><!--Device-ListAttribute-chainAnimationOptions(value: ChainAnimationOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ChainAnimationOptions](arkts-list-chainanimationoptions-i-sys.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## childrenMainSize

```TypeScript
childrenMainSize(value: ChildrenMainSize | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-childrenMainSize(value: ChildrenMainSize | undefined): this--><!--Device-ListAttribute-childrenMainSize(value: ChildrenMainSize | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ChildrenMainSize](../../apis-arkui/arkts-components/arkts-arkui-childrenmainsize-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentEndOffset

```TypeScript
contentEndOffset(offset: double | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-contentEndOffset(offset: double | Resource | undefined): this--><!--Device-ListAttribute-contentEndOffset(offset: double | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | double \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentStartOffset

```TypeScript
contentStartOffset(offset: double | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-contentStartOffset(offset: double | Resource | undefined): this--><!--Device-ListAttribute-contentStartOffset(offset: double | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | double \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## divider

```TypeScript
divider(value: ListDividerOptions | null | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-divider(value: ListDividerOptions | null | undefined): this--><!--Device-ListAttribute-divider(value: ListDividerOptions | null | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListDividerOptions](arkts-list-listdivideroptions-i.md) \| null \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## editModeOptions

```TypeScript
editModeOptions(options?: EditModeOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-editModeOptions(options?: EditModeOptions): this--><!--Device-ListAttribute-editModeOptions(options?: EditModeOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EditModeOptions](../../apis-arkui/arkts-components/arkts-arkui-editmodeoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableEditMode

```TypeScript
enableEditMode(enabled: boolean | Bindable<boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-enableEditMode(enabled: boolean | Bindable<boolean> | undefined): this--><!--Device-ListAttribute-enableEditMode(enabled: boolean | Bindable<boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## focusWrapMode

```TypeScript
focusWrapMode(mode: FocusWrapMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-focusWrapMode(mode: FocusWrapMode | undefined): this--><!--Device-ListAttribute-focusWrapMode(mode: FocusWrapMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [FocusWrapMode](../../apis-arkui/arkts-apis/arkts-arkui-focuswrapmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## lanes

```TypeScript
lanes(value: int | LengthConstrain | ItemFillPolicy | undefined, gutter?: Dimension | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-lanes(value: int | LengthConstrain | ItemFillPolicy | undefined, gutter?: Dimension | undefined): this--><!--Device-ListAttribute-lanes(value: int | LengthConstrain | ItemFillPolicy | undefined, gutter?: Dimension | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| [LengthConstrain](../../apis-arkui/arkts-apis/arkts-arkui-lengthconstrain-t.md) \| [ItemFillPolicy](../../apis-arkui/arkts-apis/arkts-arkui-itemfillpolicy-i.md) \| undefined | 是 |  |
| gutter | [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## listDirection

```TypeScript
listDirection(value: Axis | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-listDirection(value: Axis | undefined): this--><!--Device-ListAttribute-listDirection(value: Axis | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Axis](../../apis-arkui/arkts-apis/arkts-arkui-axis-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## maintainVisibleContentPosition

```TypeScript
maintainVisibleContentPosition(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-maintainVisibleContentPosition(enabled: boolean | undefined): this--><!--Device-ListAttribute-maintainVisibleContentPosition(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## multiSelectable

```TypeScript
multiSelectable(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-multiSelectable(value: boolean | undefined): this--><!--Device-ListAttribute-multiSelectable(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDidScroll

```TypeScript
onDidScroll(handler: OnScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onDidScroll(handler: OnScrollCallback | undefined): this--><!--Device-ListAttribute-onDidScroll(handler: OnScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onEditModeChange

```TypeScript
onEditModeChange(callback: Callback<boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onEditModeChange(callback: Callback<boolean> | undefined): this--><!--Device-ListAttribute-onEditModeChange(callback: Callback<boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onItemDragEnter

```TypeScript
onItemDragEnter(event: ((event: ItemDragInfo) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onItemDragEnter(event: ((event: ItemDragInfo) => void) | undefined): this--><!--Device-ListAttribute-onItemDragEnter(event: ((event: ItemDragInfo) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((event: ItemDragInfo) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onItemDragLeave

```TypeScript
onItemDragLeave(event: ((event: ItemDragInfo, itemIndex: int) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onItemDragLeave(event: ((event: ItemDragInfo, itemIndex: int) => void) | undefined): this--><!--Device-ListAttribute-onItemDragLeave(event: ((event: ItemDragInfo, itemIndex: int) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onItemDragMove

```TypeScript
onItemDragMove(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onItemDragMove(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int) => void) | undefined): this--><!--Device-ListAttribute-onItemDragMove(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int, insertIndex: int) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onItemDragStart

```TypeScript
onItemDragStart(event: OnItemDragStartCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onItemDragStart(event: OnItemDragStartCallback | undefined): this--><!--Device-ListAttribute-onItemDragStart(event: OnItemDragStartCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnItemDragStartCallback](../../apis-arkui/arkts-components/arkts-arkui-onitemdragstartcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onItemDrop

```TypeScript
onItemDrop(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onItemDrop(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) => void) | undefined): this--><!--Device-ListAttribute-onItemDrop(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onItemMove

```TypeScript
onItemMove(event: ((from: int, to: int) => boolean) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onItemMove(event: ((from: int, to: int) => boolean) | undefined): this--><!--Device-ListAttribute-onItemMove(event: ((from: int, to: int) => boolean) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((from: int, to: int) =&gt; boolean) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this--><!--Device-ListAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollframebegincallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollIndex

```TypeScript
onScrollIndex(event: ((start: int, end: int, center: int) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onScrollIndex(event: ((start: int, end: int, center: int) => void) | undefined): this--><!--Device-ListAttribute-onScrollIndex(event: ((start: int, end: int, center: int) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((start: int, end: int, center: int) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollVisibleContentChange

```TypeScript
onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback | undefined): this--><!--Device-ListAttribute-onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnScrollVisibleContentChangeCallback](arkts-onscrollvisiblecontentchangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWillScroll

```TypeScript
onWillScroll(handler: OnWillScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-onWillScroll(handler: OnWillScrollCallback | undefined): this--><!--Device-ListAttribute-onWillScroll(handler: OnWillScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnWillScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onwillscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollSnapAlign

```TypeScript
scrollSnapAlign(value: ScrollSnapAlign | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-scrollSnapAlign(value: ScrollSnapAlign | undefined): this--><!--Device-ListAttribute-scrollSnapAlign(value: ScrollSnapAlign | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollSnapAlign](arkts-list-scrollsnapalign-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollSnapAnimationSpeed

```TypeScript
scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed | undefined): this--><!--Device-ListAttribute-scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | [ScrollSnapAnimationSpeed](arkts-list-scrollsnapanimationspeed-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setListOptions

```TypeScript
setListOptions(options?: ListOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-setListOptions(options?: ListOptions): this--><!--Device-ListAttribute-setListOptions(options?: ListOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ListOptions](arkts-list-listoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## stackFromEnd

```TypeScript
stackFromEnd(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-stackFromEnd(enabled: boolean | undefined): this--><!--Device-ListAttribute-stackFromEnd(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## sticky

```TypeScript
sticky(value: StickyStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-sticky(value: StickyStyle | undefined): this--><!--Device-ListAttribute-sticky(value: StickyStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [StickyStyle](arkts-list-stickystyle-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## supportEmptyBranchInLazyLoading

```TypeScript
supportEmptyBranchInLazyLoading(supported: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-supportEmptyBranchInLazyLoading(supported: boolean | undefined): this--><!--Device-ListAttribute-supportEmptyBranchInLazyLoading(supported: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## syncLoad

```TypeScript
syncLoad(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ListAttribute-syncLoad(enable: boolean | undefined): this--><!--Device-ListAttribute-syncLoad(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置List组件的属性方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListAttribute-default--><!--Device-ListAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

