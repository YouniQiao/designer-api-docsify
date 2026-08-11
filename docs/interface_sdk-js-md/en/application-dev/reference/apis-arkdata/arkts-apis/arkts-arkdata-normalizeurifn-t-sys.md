# NormalizeUriFn (System API)

```TypeScript
type NormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void
```

Callback function called when converting the given URI into a normalized URI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type NormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void--><!--Device-unnamed-type NormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the uri to normalize. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Returns the normalized uri if the data share supports URI normalization. |

