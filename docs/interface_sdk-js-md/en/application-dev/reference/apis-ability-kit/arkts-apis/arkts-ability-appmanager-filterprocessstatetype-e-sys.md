# FilterProcessStateType (System API)

表示要监听的进程状态，该类型为枚举。可配合[AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md)过滤想要监听的进程状态。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-appManager-export enum FilterProcessStateType--><!--Device-appManager-export enum FilterProcessStateType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## CREATE

```TypeScript
CREATE = 1 << 0
```

进程刚创建完成，对应[ProcessData](../../../reference/apis-ability-kit/js-apis-inner-application-processData.md#属性)中state取值为0的状态。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-CREATE = 1 << 0--><!--Device-FilterProcessStateType-CREATE = 1 << 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## FOREGROUND

```TypeScript
FOREGROUND = 1 << 1
```

进程处于前台，对应[ProcessData](../../../reference/apis-ability-kit/js-apis-inner-application-processData.md#属性)中state取值为2的状态。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-FOREGROUND = 1 << 1--><!--Device-FilterProcessStateType-FOREGROUND = 1 << 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## BACKGROUND

```TypeScript
BACKGROUND = 1 << 2
```

进程处于后台，对应[ProcessData](../../../reference/apis-ability-kit/js-apis-inner-application-processData.md#属性)中state取值为4的状态。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-BACKGROUND = 1 << 2--><!--Device-FilterProcessStateType-BACKGROUND = 1 << 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## DESTROY

```TypeScript
DESTROY = 1 << 3
```

进程已终止，对应[ProcessData](../../../reference/apis-ability-kit/js-apis-inner-application-processData.md#属性)中state取值为5的状态。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterProcessStateType-DESTROY = 1 << 3--><!--Device-FilterProcessStateType-DESTROY = 1 << 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

