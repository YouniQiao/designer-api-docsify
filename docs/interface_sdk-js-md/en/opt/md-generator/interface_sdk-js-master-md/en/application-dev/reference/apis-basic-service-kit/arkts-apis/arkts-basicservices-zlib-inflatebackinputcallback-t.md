# InflateBackInputCallback

```TypeScript
type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer
```

A callback function for reading input data provided by a user. When the decompression process requires more input data, zlib will call this function. This function should read data from the data source to the buffer.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer--><!--Device-zlib-type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inDesc | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |
