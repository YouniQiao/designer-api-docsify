# OnTitleReceiveEvent

定义网页document标题更改时触发该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnTitleReceiveEvent--><!--Device-unnamed-declare interface OnTitleReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isRealTitle

```TypeScript
isRealTitle?: boolean
```

document标题来源，true表示来自网页的title标签，false表示该title是根据url自动生成。默认值：false

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-OnTitleReceiveEvent-isRealTitle?: boolean--><!--Device-OnTitleReceiveEvent-isRealTitle?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## title

```TypeScript
title: string
```

document标题内容。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnTitleReceiveEvent-title: string--><!--Device-OnTitleReceiveEvent-title: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

