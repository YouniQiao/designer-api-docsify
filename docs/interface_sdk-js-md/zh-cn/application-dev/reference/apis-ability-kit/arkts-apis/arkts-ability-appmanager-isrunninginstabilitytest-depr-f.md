# isRunningInStabilityTest

## 导入模块

```TypeScript
```

## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void
```

查询当前系统是否处于稳定性测试场景。使用callback异步回调。

> **说明：**&gt;
> 稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md)

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(): Promise<boolean>
```

查询当前系统是否处于稳定性测试场景。使用Promise异步回调。

> **说明：**&gt;
> 稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md)

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
