# OnReleaseCallback

注册通用组件服务端Stub（桩）断开监听通知的回调函数类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export interface OnReleaseCallback--><!--Device-unnamed-export interface OnReleaseCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { Callee, Caller, OnReleaseCallback, OnRemoteStateChangeCallback, CalleeCallback } from 'kits/@kit.AbilityKit';
```

## [[Call]]

```TypeScript
(msg: string): void
```

定义OnRelease的回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OnReleaseCallback-(msg: string): void--><!--Device-OnReleaseCallback-(msg: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | string | Yes | 用于传递释放消息。 |

