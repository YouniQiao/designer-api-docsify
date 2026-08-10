# DepthComponentCompleteCallback (System API)

```TypeScript
declare type DepthComponentCompleteCallback = (event: DepthComponentCompleteEvent) => void
```

背景资源加载成功的回调函数。使用callback异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type DepthComponentCompleteCallback = (event: DepthComponentCompleteEvent) => void--><!--Device-unnamed-declare type DepthComponentCompleteCallback = (event: DepthComponentCompleteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [DepthComponentCompleteEvent](../arkts-apis/arkts-arkui-depthcomponent-depthcomponentcompleteevent-i-sys.md) | Yes | 背景资源加载成功的事件信息。 |

