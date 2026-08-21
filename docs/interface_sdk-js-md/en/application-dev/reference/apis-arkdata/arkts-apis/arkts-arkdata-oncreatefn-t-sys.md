# OnCreateFn (System API)

```TypeScript
type OnCreateFn = (want: Want, callback: AsyncCallback<void>) => void
```

Callback function called when a datashare extension ability is started for initialization.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnCreateFn = (want: Want, callback: AsyncCallback<void>) => void--><!--Device-unnamed-type OnCreateFn = (want: Want, callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-appabilitywant-want-c.md) | Yes | Indicates connection information about the datashare extension ability. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | callback function, no return value. |

