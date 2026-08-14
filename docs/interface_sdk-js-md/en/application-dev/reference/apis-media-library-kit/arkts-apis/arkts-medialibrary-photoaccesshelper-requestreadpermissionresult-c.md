# RequestReadPermissionResult

Request read permission result

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-photoAccessHelper-export class RequestReadPermissionResult--><!--Device-photoAccessHelper-export class RequestReadPermissionResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'photoAccessHelper';
```

## authorizedUris

```TypeScript
authorizedUris?: Array<string>
```

URIs that have been created and granted the save permission.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RequestReadPermissionResult-authorizedUris?: Array<string>--><!--Device-RequestReadPermissionResult-authorizedUris?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## invalidUris

```TypeScript
invalidUris?: Array<string>
```

URIs that may be deleted, hidden, or renamed.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RequestReadPermissionResult-invalidUris?: Array<string>--><!--Device-RequestReadPermissionResult-invalidUris?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

