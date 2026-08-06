# FilterProcessStateType (System API)

Enumerates the types of process states to filter. It can be used with  
[AppStateFilter]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to filter the process state types you want to listen for.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-appManager-export enum FilterProcessStateType--><!--Device-appManager-export enum FilterProcessStateType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## CREATE

```TypeScript
CREATE = 1 << 0
```

The process has just been created. It corresponds to the state whose value is **0** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-CREATE = 1 << 0--><!--Device-FilterProcessStateType-CREATE = 1 << 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## FOREGROUND

```TypeScript
FOREGROUND = 1 << 1
```

The process is running in the foreground. It corresponds to the state whose value is **2** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-FOREGROUND = 1 << 1--><!--Device-FilterProcessStateType-FOREGROUND = 1 << 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## BACKGROUND

```TypeScript
BACKGROUND = 1 << 2
```

The process is running in the background. It corresponds to the state whose value is **4** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-BACKGROUND = 1 << 2--><!--Device-FilterProcessStateType-BACKGROUND = 1 << 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## DESTROY

```TypeScript
DESTROY = 1 << 3
```

The process has terminated. It corresponds to the state whose value is **5** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-DESTROY = 1 << 3--><!--Device-FilterProcessStateType-DESTROY = 1 << 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

