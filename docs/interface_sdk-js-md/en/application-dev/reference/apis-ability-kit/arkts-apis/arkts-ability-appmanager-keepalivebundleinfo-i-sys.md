# KeepAliveBundleInfo (System API)

Describes the keep-alive application information, which can be obtained by calling  
[getKeepAliveBundles]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or  
[getKeepAliveAppServiceExtensions]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-appManager-export interface KeepAliveBundleInfo--><!--Device-appManager-export interface KeepAliveBundleInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## allowUserToCancel

```TypeScript
allowUserToCancel?: boolean
```

Whether the user can cancel the keep-alive status. **true** if yes, **false** otherwise.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-allowUserToCancel?: boolean--><!--Device-KeepAliveBundleInfo-allowUserToCancel?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-bundleName: string--><!--Device-KeepAliveBundleInfo-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## setter

```TypeScript
setter: KeepAliveSetter
```

Type of the party that sets to keep the application alive.

**Type:** KeepAliveSetter

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-setter: KeepAliveSetter--><!--Device-KeepAliveBundleInfo-setter: KeepAliveSetter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## setterUserId

```TypeScript
setterUserId?: int
```

ID of the user who keeps the application alive.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-setterUserId?: int--><!--Device-KeepAliveBundleInfo-setterUserId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## type

```TypeScript
type: KeepAliveAppType
```

Type of the application to be kept alive.

**Type:** KeepAliveAppType

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-type: KeepAliveAppType--><!--Device-KeepAliveBundleInfo-type: KeepAliveAppType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

