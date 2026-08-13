# GlobalObserver

```TypeScript
export type GlobalObserver = (reason: GlobalError) => void
```

定义异常监听，可以作为 [errorManager.on('globalErrorOccurred')](arkts-ability-errormanager-onerror-f.md#on_error) 和 [errorManager.on('globalUnhandledRejectionDetected')](arkts-ability-errormanager-onerror-f.md#on_error) 的入参监听当前应用主线程事件处理事件。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-errorManager-export type GlobalObserver = (reason: GlobalError) => void--><!--Device-errorManager-export type GlobalObserver = (reason: GlobalError) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | [GlobalError](arkts-ability-errormanager-globalerror-i.md) | 是 |
