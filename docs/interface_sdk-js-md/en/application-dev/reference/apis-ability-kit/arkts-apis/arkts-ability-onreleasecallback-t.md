# OnReleaseCallback

```TypeScript
export type OnReleaseCallback = (msg: string) => void
```

注册通用组件服务端Stub（桩）断开监听通知的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnReleaseCallback = (msg: string) => void--><!--Device-unnamed-export type OnReleaseCallback = (msg: string) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | string | Yes | 用于传递释放消息。 |

