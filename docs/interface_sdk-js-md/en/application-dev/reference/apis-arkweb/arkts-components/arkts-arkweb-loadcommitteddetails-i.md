# LoadCommittedDetails

Defines the load committed details.

**Since:** 11

<!--Device-unnamed-declare interface LoadCommittedDetails--><!--Device-unnamed-declare interface LoadCommittedDetails-End-->

**System capability:** SystemCapability.Web.Webview.Core

## didReplaceEntry

```TypeScript
didReplaceEntry: boolean
```

True if the committed entry has replaced the existing one. Note that in case of subframes, the NavigationEntry and FrameNavigationEntry objects don't actually get replaced - they're reused, but with updated attributes.

**Type:** boolean

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LoadCommittedDetails-didReplaceEntry: boolean--><!--Device-LoadCommittedDetails-didReplaceEntry: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isMainFrame

```TypeScript
isMainFrame: boolean
```

Check whether the request is for getting the main frame.

**Type:** boolean

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LoadCommittedDetails-isMainFrame: boolean--><!--Device-LoadCommittedDetails-isMainFrame: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isSameDocument

```TypeScript
isSameDocument: boolean
```

Whether the navigation happened without changing document. Examples of same document navigations are:1. reference fragment navigations.2. pushState/replaceState.3. same page history navigation

**Type:** boolean

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LoadCommittedDetails-isSameDocument: boolean--><!--Device-LoadCommittedDetails-isSameDocument: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## navigationType

```TypeScript
navigationType: WebNavigationType
```

The type of the navigation.

**Type:** WebNavigationType

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LoadCommittedDetails-navigationType: WebNavigationType--><!--Device-LoadCommittedDetails-navigationType: WebNavigationType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

The url to navigate.

**Type:** string

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LoadCommittedDetails-url: string--><!--Device-LoadCommittedDetails-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

