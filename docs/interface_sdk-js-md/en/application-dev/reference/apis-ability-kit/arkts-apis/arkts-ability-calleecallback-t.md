# CalleeCallback

```TypeScript
export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable
```

通用组件服务端注册消息通知的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable--><!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indata | rpc.MessageSequence | Yes | 发送需传递的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| rpc.Parcelable | 返回的数据对象。 |

