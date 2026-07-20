# OnSearchResultReceiveEvent

Defines function Triggered when the host application call searchAllAsync.

**Since:** 12

<!--Device-unnamed-declare interface OnSearchResultReceiveEvent--><!--Device-unnamed-declare interface OnSearchResultReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## activeMatchOrdinal

```TypeScript
activeMatchOrdinal: number
```

The ordinal number of the currently matched lookup item (starting from 0).

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSearchResultReceiveEvent-activeMatchOrdinal: number--><!--Device-OnSearchResultReceiveEvent-activeMatchOrdinal: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isDoneCounting

```TypeScript
isDoneCounting: boolean
```

Indicates whether the current in-page search operation is complete. The method may be called back multiple times until isDoneCounting is true.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSearchResultReceiveEvent-isDoneCounting: boolean--><!--Device-OnSearchResultReceiveEvent-isDoneCounting: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## numberOfMatches

```TypeScript
numberOfMatches: number
```

The number of all matched keywords.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSearchResultReceiveEvent-numberOfMatches: number--><!--Device-OnSearchResultReceiveEvent-numberOfMatches: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

