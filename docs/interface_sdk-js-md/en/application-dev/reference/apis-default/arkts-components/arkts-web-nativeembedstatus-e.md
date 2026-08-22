# NativeEmbedStatus

Defines the lifecycle of the same-layer tag. When the same-layer tag exists on the loaded page, CREATE is triggered. When the same-layer tag is moved or is enlarged, **UPDATE **is triggered. When the page exits, DESTROY is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare enum NativeEmbedStatus--><!--Device-unnamed-export declare enum NativeEmbedStatus-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CREATE

```TypeScript
CREATE = 0
```

The same-layer tag is created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-NativeEmbedStatus-CREATE = 0--><!--Device-NativeEmbedStatus-CREATE = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## UPDATE

```TypeScript
UPDATE = 1
```

The same-layer tag is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-NativeEmbedStatus-UPDATE = 1--><!--Device-NativeEmbedStatus-UPDATE = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## DESTROY

```TypeScript
DESTROY = 2
```

The same-layer tag is destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-NativeEmbedStatus-DESTROY = 2--><!--Device-NativeEmbedStatus-DESTROY = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ENTER_BFCACHE

```TypeScript
ENTER_BFCACHE = 3
```

The same-layer tag enters the BFCache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-NativeEmbedStatus-ENTER_BFCACHE = 3--><!--Device-NativeEmbedStatus-ENTER_BFCACHE = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## LEAVE_BFCACHE

```TypeScript
LEAVE_BFCACHE = 4
```

The same-layer tag leaves the BFCache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-NativeEmbedStatus-LEAVE_BFCACHE = 4--><!--Device-NativeEmbedStatus-LEAVE_BFCACHE = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

