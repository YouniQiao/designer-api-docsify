# terminateSelf

## 导入模块

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## terminateSelf

```TypeScript
function terminateSelf(callback: AsyncCallback<void>): void
```

停止当前的Ability。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## terminateSelf

```TypeScript
function terminateSelf(): Promise<void>
```

停止当前的Ability。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
