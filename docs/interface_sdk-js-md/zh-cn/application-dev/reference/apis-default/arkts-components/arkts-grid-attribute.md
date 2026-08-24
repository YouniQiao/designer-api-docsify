# GridAttribute

除支持通用属性和滚动组件通用属性外，还支持 以下属性：

> **说明：**&gt;
> Grid组件使用通用属性clip&lt;sup&gt;12+&lt;/sup&gt;和通用属性
> clip&lt;sup&gt;18+&lt;/sup&gt;时默认值都为true。&gt;
> 设置Grid的padding后，如果子组件部分位于Grid内容区且部分位于padding区域内，则会显示；如果子组件完全位于padding区域内，则不会显示。如下图所示，GridItem1显示，而GridItem2不显示。&gt;
> 

**继承/实现关系：** GridAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface GridAttribute--><!--Device-unnamed-export declare interface GridAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
alignItems(alignment: GridItemAlignment | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-alignItems(alignment: GridItemAlignment | undefined): this--><!--Device-GridAttribute-alignItems(alignment: GridItemAlignment | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignment | [GridItemAlignment](arkts-grid-griditemalignment-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<GridAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-attributeModifier(modifier: AttributeModifier<GridAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-GridAttribute-attributeModifier(modifier: AttributeModifier<GridAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GridAttribute](arkts-grid-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cachedCount

```TypeScript
cachedCount(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-cachedCount(value: int | undefined): this--><!--Device-GridAttribute-cachedCount(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cachedCount

```TypeScript
cachedCount(count: int | undefined, show: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-cachedCount(count: int | undefined, show: boolean | undefined): this--><!--Device-GridAttribute-cachedCount(count: int | undefined, show: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | int \| undefined | 是 |  |
| show | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cellLength

```TypeScript
cellLength(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-cellLength(value: double | undefined): this--><!--Device-GridAttribute-cellLength(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnsGap

```TypeScript
columnsGap(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-columnsGap(value: Length | undefined): this--><!--Device-GridAttribute-columnsGap(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## columnsTemplate

```TypeScript
columnsTemplate(value: string | ItemFillPolicy | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-columnsTemplate(value: string | ItemFillPolicy | undefined): this--><!--Device-GridAttribute-columnsTemplate(value: string | ItemFillPolicy | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| [ItemFillPolicy](../../apis-arkui/arkts-apis/arkts-arkui-itemfillpolicy-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## edgeEffect

```TypeScript
edgeEffect(value: EdgeEffect | undefined, options?: EdgeEffectOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-edgeEffect(value: EdgeEffect | undefined, options?: EdgeEffectOptions): this--><!--Device-GridAttribute-edgeEffect(value: EdgeEffect | undefined, options?: EdgeEffectOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EdgeEffect](../../apis-arkui/arkts-apis/arkts-arkui-edgeeffect-e.md) \| undefined | 是 |  |
| options | [EdgeEffectOptions](../../apis-arkui/arkts-components/arkts-arkui-edgeeffectoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## editMode

```TypeScript
editMode(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-editMode(value: boolean | undefined): this--><!--Device-GridAttribute-editMode(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## editModeOptions

```TypeScript
editModeOptions(options?: EditModeOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-editModeOptions(options?: EditModeOptions): this--><!--Device-GridAttribute-editModeOptions(options?: EditModeOptions): this-End-->

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

<!--Device-GridAttribute-enableEditMode(enabled: boolean | Bindable<boolean> | undefined): this--><!--Device-GridAttribute-enableEditMode(enabled: boolean | Bindable<boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-enableScrollInteraction(value: boolean | undefined): this--><!--Device-GridAttribute-enableScrollInteraction(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## focusWrapMode

```TypeScript
focusWrapMode(mode: FocusWrapMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-focusWrapMode(mode: FocusWrapMode | undefined): this--><!--Device-GridAttribute-focusWrapMode(mode: FocusWrapMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [FocusWrapMode](../../apis-arkui/arkts-apis/arkts-arkui-focuswrapmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## friction

```TypeScript
friction(value: double | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-friction(value: double | Resource | undefined): this--><!--Device-GridAttribute-friction(value: double | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## layoutDirection

```TypeScript
layoutDirection(value: GridDirection | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-layoutDirection(value: GridDirection | undefined): this--><!--Device-GridAttribute-layoutDirection(value: GridDirection | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GridDirection](arkts-grid-griddirection-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## maxCount

```TypeScript
maxCount(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-maxCount(value: int | undefined): this--><!--Device-GridAttribute-maxCount(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## minCount

```TypeScript
minCount(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-minCount(value: int | undefined): this--><!--Device-GridAttribute-minCount(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## multiSelectable

```TypeScript
multiSelectable(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-multiSelectable(value: boolean | undefined): this--><!--Device-GridAttribute-multiSelectable(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-nestedScroll(value: NestedScrollOptions | undefined): this--><!--Device-GridAttribute-nestedScroll(value: NestedScrollOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDidScroll

```TypeScript
onDidScroll(handler: OnScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-onDidScroll(handler: OnScrollCallback | undefined): this--><!--Device-GridAttribute-onDidScroll(handler: OnScrollCallback | undefined): this-End-->

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

<!--Device-GridAttribute-onEditModeChange(callback: Callback<boolean> | undefined): this--><!--Device-GridAttribute-onEditModeChange(callback: Callback<boolean> | undefined): this-End-->

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

<!--Device-GridAttribute-onItemDragEnter(event: ((event: ItemDragInfo) => void) | undefined): this--><!--Device-GridAttribute-onItemDragEnter(event: ((event: ItemDragInfo) => void) | undefined): this-End-->

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

<!--Device-GridAttribute-onItemDragLeave(event: ((event: ItemDragInfo, itemIndex: int) => void) | undefined): this--><!--Device-GridAttribute-onItemDragLeave(event: ((event: ItemDragInfo, itemIndex: int) => void) | undefined): this-End-->

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

<!--Device-GridAttribute-onItemDragMove(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int) => void) | undefined): this--><!--Device-GridAttribute-onItemDragMove(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int) => void) | undefined): this-End-->

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

<!--Device-GridAttribute-onItemDragStart(event: OnItemDragStartCallback | undefined): this--><!--Device-GridAttribute-onItemDragStart(event: OnItemDragStartCallback | undefined): this-End-->

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

<!--Device-GridAttribute-onItemDrop(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) => void) | undefined): this--><!--Device-GridAttribute-onItemDrop(event: ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((event: ItemDragInfo, itemIndex: int, insertIndex: int, isSuccess: boolean) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollBarUpdate

```TypeScript
onScrollBarUpdate(event: ((index: int, offset: double) => ComputedBarAttribute) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-onScrollBarUpdate(event: ((index: int, offset: double) => ComputedBarAttribute) | undefined): this--><!--Device-GridAttribute-onScrollBarUpdate(event: ((index: int, offset: double) => ComputedBarAttribute) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((index: int, offset: double) =&gt; ComputedBarAttribute) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this--><!--Device-GridAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollframebegincallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollIndex

```TypeScript
onScrollIndex(event: ((first: int, last: int) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-onScrollIndex(event: ((first: int, last: int) => void) | undefined): this--><!--Device-GridAttribute-onScrollIndex(event: ((first: int, last: int) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | ((first: int, last: int) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWillScroll

```TypeScript
onWillScroll(handler: OnWillScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-onWillScroll(handler: OnWillScrollCallback | undefined): this--><!--Device-GridAttribute-onWillScroll(handler: OnWillScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnWillScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onwillscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowsGap

```TypeScript
rowsGap(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-rowsGap(value: Length | undefined): this--><!--Device-GridAttribute-rowsGap(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rowsTemplate

```TypeScript
rowsTemplate(value: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-rowsTemplate(value: string | undefined): this--><!--Device-GridAttribute-rowsTemplate(value: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBar

```TypeScript
scrollBar(value: BarState | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-scrollBar(value: BarState | undefined): this--><!--Device-GridAttribute-scrollBar(value: BarState | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](../../apis-arkui/arkts-apis/arkts-arkui-barstate-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarColor

```TypeScript
scrollBarColor(color: Color | int | string | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-scrollBarColor(color: Color | int | string | Resource | undefined): this--><!--Device-GridAttribute-scrollBarColor(color: Color | int | string | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| int \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarWidth

```TypeScript
scrollBarWidth(value: double | string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-scrollBarWidth(value: double | string | undefined): this--><!--Device-GridAttribute-scrollBarWidth(value: double | string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarWidth

```TypeScript
scrollBarWidth(value: Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-scrollBarWidth(value: Resource | undefined): this--><!--Device-GridAttribute-scrollBarWidth(value: Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setGridOptions

```TypeScript
setGridOptions(scroller?: Scroller, layoutOptions?: GridLayoutOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-setGridOptions(scroller?: Scroller, layoutOptions?: GridLayoutOptions): this--><!--Device-GridAttribute-setGridOptions(scroller?: Scroller, layoutOptions?: GridLayoutOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller](../../apis-arkui/arkts-components/arkts-arkui-scroller-c.md) | 否 |  |
| layoutOptions | [GridLayoutOptions](arkts-grid-gridlayoutoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## supportAnimation

```TypeScript
supportAnimation(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-supportAnimation(value: boolean | undefined): this--><!--Device-GridAttribute-supportAnimation(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## supportEmptyBranchInLazyLoading

```TypeScript
supportEmptyBranchInLazyLoading(supported: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GridAttribute-supportEmptyBranchInLazyLoading(supported: boolean | undefined): this--><!--Device-GridAttribute-supportEmptyBranchInLazyLoading(supported: boolean | undefined): this-End-->

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

<!--Device-GridAttribute-syncLoad(enable: boolean | undefined): this--><!--Device-GridAttribute-syncLoad(enable: boolean | undefined): this-End-->

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

动态设置Grid组件的属性方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridAttribute-default--><!--Device-GridAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

