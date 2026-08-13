# InflateBackOutputCallback

```TypeScript
type InflateBackOutputCallback = (outDesc: RecordData, buf: ArrayBuffer, length: int) => int
```

The output data provided by the user is written into the callback function. Whenever decompressed data is ready for output, zlib calls this function to write the data from the buffer to the target location.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-type InflateBackOutputCallback = (outDesc: RecordData, buf: ArrayBuffer, length: int) => int--><!--Device-zlib-type InflateBackOutputCallback = (outDesc: RecordData, buf: ArrayBuffer, length: int) => int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outDesc | [RecordData](arkts-basicservices-recorddata-t.md) | Yes | Object passed to output function. Object dependency requirement implementation. |
| buf | ArrayBuffer | Yes | Used to store data to be written. |
| length | int | Yes | Write the length of the output buffer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Return the number of bytes output. |

