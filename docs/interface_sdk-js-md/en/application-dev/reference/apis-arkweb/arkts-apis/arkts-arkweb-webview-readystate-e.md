# ReadyState

播放器的缓存状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-enum ReadyState--><!--Device-webview-enum ReadyState-End-->

**System capability:** SystemCapability.Web.Webview.Core

## HAVE_NOTHING

```TypeScript
HAVE_NOTHING = 0
```

没有缓存。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadyState-HAVE_NOTHING = 0--><!--Device-ReadyState-HAVE_NOTHING = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## HAVE_METADATA

```TypeScript
HAVE_METADATA = 1
```

只缓存了媒体元数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadyState-HAVE_METADATA = 1--><!--Device-ReadyState-HAVE_METADATA = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## HAVE_CURRENT_DATA

```TypeScript
HAVE_CURRENT_DATA = 2
```

只缓存到当前的播放进度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadyState-HAVE_CURRENT_DATA = 2--><!--Device-ReadyState-HAVE_CURRENT_DATA = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## HAVE_FUTURE_DATA

```TypeScript
HAVE_FUTURE_DATA = 3
```

缓存时长超过了当前的播放进度, 但是仍有可能导致卡顿。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadyState-HAVE_FUTURE_DATA = 3--><!--Device-ReadyState-HAVE_FUTURE_DATA = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## HAVE_ENOUGH_DATA

```TypeScript
HAVE_ENOUGH_DATA = 4
```

缓存了足够的数据，保证播放流畅。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadyState-HAVE_ENOUGH_DATA = 4--><!--Device-ReadyState-HAVE_ENOUGH_DATA = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

