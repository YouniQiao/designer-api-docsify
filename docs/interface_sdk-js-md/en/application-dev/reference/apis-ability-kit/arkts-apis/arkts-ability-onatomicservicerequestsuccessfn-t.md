# OnAtomicServiceRequestSuccessFn

```TypeScript
type OnAtomicServiceRequestSuccessFn = (appId: string) => void
```

打开原子化服务成功时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAtomicServiceRequestSuccessFn = (appId: string) => void--><!--Device-unnamed-type OnAtomicServiceRequestSuccessFn = (appId: string) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | 被拉起原子化服务的appId。 |

