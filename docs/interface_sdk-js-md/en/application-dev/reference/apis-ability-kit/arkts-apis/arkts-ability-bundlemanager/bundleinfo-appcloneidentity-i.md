# AppCloneIdentity

Describes the identity information of an application clone.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AppCloneIdentity--><!--Device-unnamed-export interface AppCloneIdentity-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## appIndex

```TypeScript
readonly appIndex: int
```

Clone index information of the app package. The value is an integer ranging from [0-5],where 0 indicates the main app and 1-5 indicate clone apps.

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AppCloneIdentity-readonly appIndex: int--><!--Device-AppCloneIdentity-readonly appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## bundleName

```TypeScript
readonly bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AppCloneIdentity-readonly bundleName: string--><!--Device-AppCloneIdentity-readonly bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

