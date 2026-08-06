# OnSearchResultReceiveEvent

Defines function Triggered when the host application call searchAllAsync.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface OnSearchResultReceiveEvent--><!--Device-unnamed-export declare interface OnSearchResultReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## activeMatchOrdinal

```TypeScript
activeMatchOrdinal: int
```

The ordinal number of the currently matched lookup item (starting from 0).

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnSearchResultReceiveEvent-activeMatchOrdinal: int--><!--Device-OnSearchResultReceiveEvent-activeMatchOrdinal: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isDoneCounting

```TypeScript
isDoneCounting: boolean
```

Indicates whether the current in-page search operation is complete. The method may be called back multiple times until isDoneCounting is true.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnSearchResultReceiveEvent-isDoneCounting: boolean--><!--Device-OnSearchResultReceiveEvent-isDoneCounting: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## numberOfMatches

```TypeScript
numberOfMatches: int
```

The number of all matched keywords.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnSearchResultReceiveEvent-numberOfMatches: int--><!--Device-OnSearchResultReceiveEvent-numberOfMatches: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

