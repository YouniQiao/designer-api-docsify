# AbilityFirstFrameStateObserver（系统接口）

定义了Ability首帧绘制完成事件监听对象，可以作为 [on](arkts-ability-appmanager-on-f-sys.md#onabilityfirstframestate) 的入参，用于监听Ability首帧绘制完成事件。

**起始版本：** 12

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## onAbilityFirstFrameDrawn

```TypeScript
onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void
```

Ability首帧绘制完成时触发的回调函数。

**起始版本：** 12

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [AbilityFirstFrameStateData](arkts-ability-abilityfirstframestatedata-i-sys.md) | 是 |
