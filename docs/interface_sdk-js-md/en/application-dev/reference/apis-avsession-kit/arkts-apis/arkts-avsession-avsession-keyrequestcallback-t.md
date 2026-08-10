# KeyRequestCallback

```TypeScript
type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void
```

许可证请求事件的回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-avSession-type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void--><!--Device-avSession-type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assetId | string | Yes | 媒体ID。 |
| requestData | Uint8Array | Yes | 媒体许可证请求数据。 |

