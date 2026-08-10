# NativeEmbedStatus

定义同层标签生命周期，当加载页面中有同层标签会触发CREATE，同层标签移动或者放大会触发UPDATE，退出页面会触发DESTROY。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum NativeEmbedStatus--><!--Device-unnamed-declare enum NativeEmbedStatus-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CREATE

```TypeScript
CREATE = 0
```

同层标签创建。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NativeEmbedStatus-CREATE = 0--><!--Device-NativeEmbedStatus-CREATE = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## UPDATE

```TypeScript
UPDATE = 1
```

同层标签更新。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NativeEmbedStatus-UPDATE = 1--><!--Device-NativeEmbedStatus-UPDATE = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## DESTROY

```TypeScript
DESTROY = 2
```

同层标签销毁。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NativeEmbedStatus-DESTROY = 2--><!--Device-NativeEmbedStatus-DESTROY = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ENTER_BFCACHE

```TypeScript
ENTER_BFCACHE = 3
```

同层标签进入BFCache。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeEmbedStatus-ENTER_BFCACHE = 3--><!--Device-NativeEmbedStatus-ENTER_BFCACHE = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## LEAVE_BFCACHE

```TypeScript
LEAVE_BFCACHE = 4
```

同层标签离开BFCache。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeEmbedStatus-LEAVE_BFCACHE = 4--><!--Device-NativeEmbedStatus-LEAVE_BFCACHE = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

