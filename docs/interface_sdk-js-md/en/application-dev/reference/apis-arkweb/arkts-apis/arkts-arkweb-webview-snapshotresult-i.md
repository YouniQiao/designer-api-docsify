# SnapshotResult

Represents a full drawing result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-interface SnapshotResult--><!--Device-webview-interface SnapshotResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## id

```TypeScript
id?: string
```

Id of the snapshot.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SnapshotResult-id?: string--><!--Device-SnapshotResult-id?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## imagePixelMap

```TypeScript
imagePixelMap?: image.PixelMap
```

Full drawing result in image.PixelMap format.

**Type:** image.PixelMap

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SnapshotResult-imagePixelMap?: image.PixelMap--><!--Device-SnapshotResult-imagePixelMap?: image.PixelMap-End-->

**System capability:** SystemCapability.Web.Webview.Core

## size

```TypeScript
size?: SizeOptions
```

Actual size drawn on the web page.The value is of the number type, and the unit is vp.

**Type:** SizeOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SnapshotResult-size?: SizeOptions--><!--Device-SnapshotResult-size?: SizeOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## status

```TypeScript
status?: boolean
```

The status of the snapshot.The value can be true (normal) or false (failure). If the full drawing result fails to be obtained,the width and height of the returned size are both 0, and the map is empty.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SnapshotResult-status?: boolean--><!--Device-SnapshotResult-status?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

