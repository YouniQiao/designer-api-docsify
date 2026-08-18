# CalleeCallback

```TypeScript
export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable
```

通用组件服务端注册消息通知的回调函数类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable--><!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| indata | rpc.MessageSequence | 是 |

**返回值：**

| 类型 |
| --- |
| rpc.Parcelable |
