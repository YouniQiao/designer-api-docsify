# PrefetchOptions

Defines the PrefetchOptions class.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-webview-class PrefetchOptions--><!--Device-webview-class PrefetchOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

Constructor for PrefetchOptions.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-PrefetchOptions-constructor()--><!--Device-PrefetchOptions-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ignoreCacheControlNoStore

```TypeScript
ignoreCacheControlNoStore: boolean
```

Set whether to ignore Cache-Control: no-store‌. &lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt; This setting controls whether prefetch operations bypass the HTTP Cache-Control: no-store directive. Important‌: Default behavior (false) aligns with HTTP security standards. Overriding (true) requires explicit risk assessment for non-sensitive resources.

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean--><!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## minTimeBetweenPrefetchesMs

```TypeScript
minTimeBetweenPrefetchesMs: number
```

‌Set prefetch page interval limit. &lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt; The value should be an integer.Unit: ms. Default 500ms (ensures only one successful prefetch within 500ms). The interval throttles prefetch frequency to balance performance and resource usage.

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: number--><!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

