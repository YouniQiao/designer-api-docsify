# SourceOpenCallback

```TypeScript
type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long
```

由应用实现此回调函数，应用需处理传入的资源打开请求，并返回所打开资源对应的唯一句柄。

> **注意：**
> 
> 客户端在处理完请求后应立刻返回。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long--><!--Device-unnamed-type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [MediaSourceLoadingRequest](arkts-media-multimedia-media-mediasourceloadingrequest-i.md) | Yes | 打开请求参数，包含请求资源的具体信息和数据推送方式。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 当前资源打开请求的句柄。大于0表示请求成功，小于或等于0表示请求失败。<br/> - request对象对应句柄唯一。 |

