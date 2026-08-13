# OnRequestFailureFn

```TypeScript
export type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void
```

拉起指定类型的Ability组件失败时的回调函数类型。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void--><!--Device-unnamed-export type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| failureCode | [AbilityStartFailureCode](arkts-ability-app-ability-completionhandlerforabilitystartcallback-abilitystartfailurecode-e.md) | 是 |
| failureMessage | string | 是 |
