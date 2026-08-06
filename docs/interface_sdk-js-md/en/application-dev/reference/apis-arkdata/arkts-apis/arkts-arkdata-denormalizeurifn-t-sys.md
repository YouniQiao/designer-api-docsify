# DenormalizeUriFn (System API)

```TypeScript
type DenormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void
```

Callback function called when converting the given normalized URI into a denormalized URI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type DenormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void--><!--Device-unnamed-type DenormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the uri to denormalize.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string&gt; | Yes | Returns the denormalized {@code uri} object if the denormalization is successful; returns the original {@code uri} passed to this method if there is nothing to do; returns {@code null} if the data identified by the original {@code uri} cannot be found in the current environment.  |

