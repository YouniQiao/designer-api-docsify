# ChangeData (System API)

Defines the return value of the listener callback.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** [ChangeData](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md#ChangeData)

<!--Device-userFileManager-interface ChangeData--><!--Device-userFileManager-interface ChangeData-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from 'userFileManager';
```

## subUris

```TypeScript
subUris: Array<string>
```

URIs of the changed files in the album. The value may be undefined. Check whether the value is undefined before using it.

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

<!--Device-ChangeData-subUris: Array<string>--><!--Device-ChangeData-subUris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## type

```TypeScript
type: NotifyType
```

Notification type.

**Type:** NotifyType

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** [type](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md#type)

<!--Device-ChangeData-type: NotifyType--><!--Device-ChangeData-type: NotifyType-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## uris

```TypeScript
uris: Array<string>
```

Array of all file asset or album URIs with the same [NotifyType](arkts-corefile-userfilemanager-notifytype-e-sys.md#NotifyType-(System-API)).

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** [uris](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md#uris)

<!--Device-ChangeData-uris: Array<string>--><!--Device-ChangeData-uris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

