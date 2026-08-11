# BackForwardCacheSupportedFeatures

This class is used to enable back forward cache supported features.

**Since:** 12

<!--Device-webview-class BackForwardCacheSupportedFeatures--><!--Device-webview-class BackForwardCacheSupportedFeatures-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

**Since:** 12

<!--Device-BackForwardCacheSupportedFeatures-constructor()--><!--Device-BackForwardCacheSupportedFeatures-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## mediaTakeOver

```TypeScript
mediaTakeOver: boolean
```

Whether cache the pages that use media take over.&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;When the value is set to **true**, you need to maintain the lifecycle of system components created for video elements to avoid resource leak.&lt;/p&gt;

Default is false;

**Type:** boolean

**Since:** 12

<!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean--><!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## nativeEmbed

```TypeScript
nativeEmbed: boolean
```

Whether cache the pages that use native embed.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;When the value is set to **true**, you need to maintain the lifecycle of system components created for the same-layer rendering elements to avoid resource leak.&lt;/p&gt;

Default is false;

**Type:** boolean

**Since:** 12

<!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean--><!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core
