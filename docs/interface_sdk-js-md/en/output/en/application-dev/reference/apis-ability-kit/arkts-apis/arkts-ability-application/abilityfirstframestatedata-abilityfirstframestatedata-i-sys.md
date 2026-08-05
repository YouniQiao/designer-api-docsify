# AbilityFirstFrameStateData (System API)

The module defines the struct reported by the callback when the first frame of an ability is rendered. After registering the first frame rendering completion event of an ability by using [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ , you can obtain the reported struct through the [onAbilityFirstFrameDrawn]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ callback of [AbilityFirstFrameStateObserver]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityFirstFrameStateData--><!--Device-unnamed-export interface AbilityFirstFrameStateData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityName

```TypeScript
abilityName: string
```

The ability name.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-abilityName: string--><!--Device-AbilityFirstFrameStateData-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex: int
```

The index of DLP sandbox.

**Type:** int

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-appIndex: int--><!--Device-AbilityFirstFrameStateData-appIndex: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

The bundle name.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-bundleName: string--><!--Device-AbilityFirstFrameStateData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## isColdStart

```TypeScript
isColdStart: boolean
```

The entry ability of application is cold-start return true, others false.

**Type:** boolean

**Default:** false

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-isColdStart: boolean--><!--Device-AbilityFirstFrameStateData-isColdStart: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

The module name.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-moduleName: string--><!--Device-AbilityFirstFrameStateData-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

