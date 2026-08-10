# LaunchAtomicServiceCallback (System API)

```TypeScript
export declare type LaunchAtomicServiceCallback = (appId: string, options?: AtomicServiceOptions) => void
```

拉起原子化服务触发的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare type LaunchAtomicServiceCallback = (appId: string, options?: AtomicServiceOptions) => void--><!--Device-unnamed-export declare type LaunchAtomicServiceCallback = (appId: string, options?: AtomicServiceOptions) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | 原子化服务的appId。 |
| options | [AtomicServiceOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-atomicserviceoptions-atomicserviceoptions-c.md) | No | 拉起原子化服务的参数。不填时使用默认参数拉起原子化服务。 |

