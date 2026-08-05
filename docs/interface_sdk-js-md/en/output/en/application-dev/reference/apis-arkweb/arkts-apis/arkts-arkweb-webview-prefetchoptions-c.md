# PrefetchOptions

Defines the PrefetchOptions class.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-webview-class PrefetchOptions--><!--Device-webview-class PrefetchOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor for PrefetchOptions.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-PrefetchOptions-constructor()--><!--Device-PrefetchOptions-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ignoreCacheControlNoStore

```TypeScript
ignoreCacheControlNoStore: boolean
```

Set whether to ignore Cache-Control: no-store‌. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_API Note\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ This setting controls whether prefetch operations bypass the HTTP Cache-Control: no-store directive. Important‌: Default behavior (false) aligns with HTTP security standards. Overriding (true) requires explicit risk assessment for non-sensitive resources.

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean--><!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## minTimeBetweenPrefetchesMs

```TypeScript
minTimeBetweenPrefetchesMs: number
```

‌Set prefetch page interval limit. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_API Note\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ The value should be an integer.Unit: ms. Default 500ms (ensures only one successful prefetch within 500ms). The interval throttles prefetch frequency to balance performance and resource usage.

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: number--><!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

