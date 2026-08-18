# InflateBackOutputCallback

```TypeScript
type InflateBackOutputCallback = (outDesc: RecordData, buf: ArrayBuffer, length: number) => number
```

The output data provided by the user is written into the callback function. Whenever decompressed data is ready for output, zlib calls this function to write the data from the buffer to the target location.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-type InflateBackOutputCallback = (outDesc: RecordData, buf: ArrayBuffer, length: int) => int--><!--Device-zlib-type InflateBackOutputCallback = (outDesc: RecordData, buf: ArrayBuffer, length: int) => int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outDesc | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md) | Yes |
| buf | ArrayBuffer | Yes |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
