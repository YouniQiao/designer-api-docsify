# NotifySnapshotCallback（系统接口）

```TypeScript
type NotifySnapshotCallback = (deviceId: string, mission: int) => void
```

快照更改时的回调函数。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
