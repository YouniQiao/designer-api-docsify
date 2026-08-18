# offFreeze

## 导入模块

```TypeScript
```

## offFreeze

```TypeScript
function offFreeze(observer?: FreezeObserver): void
```

注销冻屏事件观测器。 此函数只能在主线程中调用。

**起始版本：** 24

<!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void--><!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |
