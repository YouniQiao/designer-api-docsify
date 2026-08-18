# OfflineResourceMap

Define offline resource's content and info.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webview-interface OfflineResourceMap--><!--Device-webview-interface OfflineResourceMap-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## resource

```TypeScript
resource: Uint8Array
```

Arraybuffer of resource. Size must less than 10Mb and cannot be empty.

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OfflineResourceMap-resource: Uint8Array--><!--Device-OfflineResourceMap-resource: Uint8Array-End-->

**System capability:** SystemCapability.Web.Webview.Core

## responseHeaders

```TypeScript
responseHeaders: Array<WebHeader>
```

Response headers of resource.

**Type:** Array&lt;WebHeader&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OfflineResourceMap-responseHeaders: Array<WebHeader>--><!--Device-OfflineResourceMap-responseHeaders: Array<WebHeader>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## type

```TypeScript
type: OfflineResourceType
```

Resource type

**Type:** [OfflineResourceType](arkts-na-webview-offlineresourcetype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OfflineResourceMap-type: OfflineResourceType--><!--Device-OfflineResourceMap-type: OfflineResourceType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## urlList

```TypeScript
urlList: Array<string>
```

Url list of resource. Url of urlList must be HTTP/HTTPS protocol and no longer than 2048.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OfflineResourceMap-urlList: Array<string>--><!--Device-OfflineResourceMap-urlList: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

