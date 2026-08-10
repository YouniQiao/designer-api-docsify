# OnSearchResultReceiveEvent

定义通知调用方网页页内查找的结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnSearchResultReceiveEvent--><!--Device-unnamed-declare interface OnSearchResultReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## activeMatchOrdinal

```TypeScript
activeMatchOrdinal: number
```

当前匹配的查找项的序号（从0开始）。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSearchResultReceiveEvent-activeMatchOrdinal: number--><!--Device-OnSearchResultReceiveEvent-activeMatchOrdinal: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isDoneCounting

```TypeScript
isDoneCounting: boolean
```

当次页内查找操作是否结束。该方法可能会回调多次，直到isDoneCounting为true为止。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSearchResultReceiveEvent-isDoneCounting: boolean--><!--Device-OnSearchResultReceiveEvent-isDoneCounting: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## numberOfMatches

```TypeScript
numberOfMatches: number
```

所有匹配到的关键词的个数。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSearchResultReceiveEvent-numberOfMatches: number--><!--Device-OnSearchResultReceiveEvent-numberOfMatches: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

