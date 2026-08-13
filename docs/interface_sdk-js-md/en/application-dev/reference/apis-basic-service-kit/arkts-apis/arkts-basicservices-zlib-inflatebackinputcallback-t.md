# InflateBackInputCallback

```TypeScript
type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer
```

A callback function for reading input data provided by a user. When the decompression process requires more input data, zlib will call this function. This function should read data from the data source to the buffer.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer--><!--Device-zlib-type InflateBackInputCallback = (inDesc: RecordData) => ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inDesc | [RecordData](arkts-basicservices-recorddata-t.md) | Yes | A universal user-defined data object. The specific type and content depend on the actual application scenario, which can include configuration data, file handles, etc. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | Return the buffer successfully read by the data source through the input descriptor. |

