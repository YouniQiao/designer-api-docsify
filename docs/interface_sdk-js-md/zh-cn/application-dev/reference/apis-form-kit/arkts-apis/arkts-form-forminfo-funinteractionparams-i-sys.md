# FunInteractionParams（系统接口）

The fun interaction form params.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-formInfo-interface FunInteractionParams--><!--Device-formInfo-interface FunInteractionParams-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## abilityName

```TypeScript
abilityName?: string
```

The ability name of the fun interaction form.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FunInteractionParams-abilityName?: string--><!--Device-FunInteractionParams-abilityName?: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## keepStateDuration

```TypeScript
keepStateDuration?: int
```

duration of the fun interaction form will be paused if not operate.Unit: milliseconds, The value must be an integer within [0,60000]. Default value: 10000.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FunInteractionParams-keepStateDuration?: int--><!--Device-FunInteractionParams-keepStateDuration?: int-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## subBundleName

```TypeScript
subBundleName: string
```

The sub bundle name used by game engine.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FunInteractionParams-subBundleName: string--><!--Device-FunInteractionParams-subBundleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## targetBundleName

```TypeScript
targetBundleName: string
```

The bundle name used by game engine.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FunInteractionParams-targetBundleName: string--><!--Device-FunInteractionParams-targetBundleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

