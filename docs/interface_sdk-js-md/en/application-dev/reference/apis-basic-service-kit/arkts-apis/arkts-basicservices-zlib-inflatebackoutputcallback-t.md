# InflateBackOutputCallback

```TypeScript
type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: int) => int
```

用户提供的输出数据会被写入回调函数中。每当解压后的数据准备好进行输出时，zlib 就会调用此函数将缓冲区中的数据写入目标位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-zlib-type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: int) => int--><!--Device-zlib-type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: int) => int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outDesc | object | Yes | 用户定义数据对象。 |
| buf | ArrayBuffer | Yes | 用于存储要写入的数据。 |
| length | int | Yes | 写入输出缓冲区的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 输出缓冲区的字节数。 |

