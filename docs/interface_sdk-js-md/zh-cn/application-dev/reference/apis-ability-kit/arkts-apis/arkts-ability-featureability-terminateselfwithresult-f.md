# terminateSelfWithResult

## 导入模块

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## terminateSelfWithResult

```TypeScript
function terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
```

停止当前的Ability。使用callback异步回调。如果该Ability是通过调用 [startAbilityForResult](arkts-ability-featureability-startabilityforresult-f.md) 接口被拉起的，调用terminateSelfWithResult接口时会将结果返回给调用者，如果该Ability不是通过调用 [startAbilityForResult](arkts-ability-featureability-startabilityforresult-f.md) 接口被拉起的，调用terminateSelfWithResult接口时不会有结果返回给调用者。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## terminateSelfWithResult

```TypeScript
function terminateSelfWithResult(parameter: AbilityResult): Promise<void>
```

停止当前的Ability。使用Promise异步回调。如果该Ability是通过调用 [startAbilityForResult](arkts-ability-featureability-startabilityforresult-f.md) 接口被拉起的，调用terminateSelfWithResult接口时会将结果返回给调用者，如果该Ability不是通过调用 [startAbilityForResult](arkts-ability-featureability-startabilityforresult-f.md) 接口被拉起的，调用terminateSelfWithResult接口时不会有结果返回给调用者。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
