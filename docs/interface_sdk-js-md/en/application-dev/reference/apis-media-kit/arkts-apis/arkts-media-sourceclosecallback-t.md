# SourceCloseCallback

```TypeScript
type SourceCloseCallback = (uuid: long) => void
```

由应用实现此回调函数，应用应释放相关资源。

> **注意：**
> 
> 客户端在处理完请求后应立刻返回。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-type SourceCloseCallback = (uuid: long) => void--><!--Device-unnamed-type SourceCloseCallback = (uuid: long) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 资源句柄的标识。 |

