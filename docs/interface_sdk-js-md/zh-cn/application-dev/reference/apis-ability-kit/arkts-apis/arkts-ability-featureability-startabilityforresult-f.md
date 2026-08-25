# startAbilityForResult

## 导入模块

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## startAbilityForResult

```TypeScript
function startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>): void
```

启动一个Ability。使用callback异步回调。启动Ability后，存在如下几种情况：  
- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) 接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。  
- 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) 接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（FA模型）](../../../application-models/component-startup-rules-fa.md)。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 是 |


## startAbilityForResult

```TypeScript
function startAbilityForResult(parameter: StartAbilityParameter): Promise<AbilityResult>
```

启动一个Ability。使用Promise异步回调。启动Ability后，存在如下几种情况：  
- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) 接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。  
- 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) 接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（FA模型）](../../../application-models/component-startup-rules-fa.md)。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |
