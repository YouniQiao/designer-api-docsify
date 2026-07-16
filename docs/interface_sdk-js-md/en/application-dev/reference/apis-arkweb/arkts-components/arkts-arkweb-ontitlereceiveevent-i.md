# OnTitleReceiveEvent

Defines the triggered function when the title of the main application document changes.

**Since:** 12

<!--Device-unnamed-declare interface OnTitleReceiveEvent--><!--Device-unnamed-declare interface OnTitleReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isRealTitle

```TypeScript
isRealTitle?: boolean
```

Mark the source of the title. If it is true, the title is derived from the H5 title element;If it is false, it is calculated from the URL. By default, it is calculated from the URL.

**Type:** boolean

**Since:** 20

<!--Device-OnTitleReceiveEvent-isRealTitle?: boolean--><!--Device-OnTitleReceiveEvent-isRealTitle?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## title

```TypeScript
title: string
```

The title of the page.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnTitleReceiveEvent-title: string--><!--Device-OnTitleReceiveEvent-title: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

