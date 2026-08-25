# startAbility

## 导入模块

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## startAbility

```TypeScript
function startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void
```

启动新的Ability。使用callback异步回调。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（FA模型）](../../../application-models/component-startup-rules-fa.md)。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## startAbility

```TypeScript
function startAbility(parameter: StartAbilityParameter): Promise<number>
```

启动新的Ability。使用Promise异步回调。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（FA模型）](../../../application-models/component-startup-rules-fa.md)。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
