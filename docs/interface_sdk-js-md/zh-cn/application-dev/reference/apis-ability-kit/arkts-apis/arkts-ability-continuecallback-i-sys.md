# ContinueCallback（系统接口）

表示跨设备迁移Mission完成后，返回迁移结果的回调函数。@interface ContinueCallback

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

## onContinueDone

```TypeScript
onContinueDone: OnContinueDoneCallback
```

Mission迁移完成后调用，回调参数result返回迁移结果。当目标设备成功接收并启动Mission后，系统会触发此回调通知源设备迁移结果。开发者应根据result参数判断迁移是否成功，并执行相应操作，如提示用户或进行重试。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。
