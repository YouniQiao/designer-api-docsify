# DenormalizeUriFn (System API)

```TypeScript
type DenormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void
```

Callback function called when converting the given normalized URI into a denormalized URI.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type DenormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void--><!--Device-unnamed-type DenormalizeUriFn = (uri: string, callback: AsyncCallback<string>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |
