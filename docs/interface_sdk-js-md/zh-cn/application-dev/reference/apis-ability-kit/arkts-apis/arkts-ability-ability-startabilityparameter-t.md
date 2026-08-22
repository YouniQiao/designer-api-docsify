# StartAbilityParameter

```TypeScript
export type StartAbilityParameter = _StartAbilityParameter
```

StartAbilityParameter二级模块。

**起始版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ability-export type StartAbilityParameter = _StartAbilityParameter--><!--Device-ability-export type StartAbilityParameter = _StartAbilityParameter-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**属性类型：** _StartAbilityParameter

**示例**

ArkTS-Dyn示例：

```TypeScript
import { ability } from '@kit.AbilityKit';

let dataAbilityHelper: ability.DataAbilityHelper;
let pacMap: ability.PacMap;
let dataAbilityOperation: ability.DataAbilityOperation;
let dataAbilityResult: ability.DataAbilityResult;
let abilityResult: ability.AbilityResult;
let connectOptions: ability.ConnectOptions;  
let startAbilityParameter: ability.StartAbilityParameter;
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { ability } from '@kit.AbilityKit';

let pacMap: ability.PacMap;
```

