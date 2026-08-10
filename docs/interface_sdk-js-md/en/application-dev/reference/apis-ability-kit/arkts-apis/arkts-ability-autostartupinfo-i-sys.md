# AutoStartupInfo (System API)

定义开机自启动应用组件信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AutoStartupInfo--><!--Device-unnamed-export interface AutoStartupInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityName

```TypeScript
abilityName: string
```

应用程序的Ability名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-abilityName: string--><!--Device-AutoStartupInfo-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityTypeName

```TypeScript
abilityTypeName?: string
```

应用程序的Ability类型。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-abilityTypeName?: string--><!--Device-AutoStartupInfo-abilityTypeName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appCloneIndex

```TypeScript
appCloneIndex?: int
```

分身应用索引。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-appCloneIndex?: int--><!--Device-AutoStartupInfo-appCloneIndex?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

应用程序的Bundle名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-bundleName: string--><!--Device-AutoStartupInfo-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## canUserModify

```TypeScript
readonly canUserModify?: boolean
```

表示是否允许开发者修改此应用的开机自启动状态，true表示允许，false表示不允许。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-readonly canUserModify?: boolean--><!--Device-AutoStartupInfo-readonly canUserModify?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName?: string
```

应用程序的Module名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-moduleName?: string--><!--Device-AutoStartupInfo-moduleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## setterUserId

```TypeScript
readonly setterUserId?: int
```

设置者的用户ID，记录了将当前应用设置为开机自启动的用户ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-readonly setterUserId?: int--><!--Device-AutoStartupInfo-readonly setterUserId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## userId

```TypeScript
readonly userId?: int
```

应用程序所属的用户ID，用于区分同一设备上不同用户账号下的应用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupInfo-readonly userId?: int--><!--Device-AutoStartupInfo-readonly userId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

