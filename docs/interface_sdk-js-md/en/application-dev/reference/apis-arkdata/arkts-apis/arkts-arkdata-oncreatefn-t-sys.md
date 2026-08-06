# OnCreateFn (System API)

```TypeScript
type OnCreateFn = (want: Want, callback: AsyncCallback<void>) => void
```

Callback function called when a datashare extension ability is started for initialization.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnCreateFn = (want: Want, callback: AsyncCallback<void>) => void--><!--Device-unnamed-type OnCreateFn = (want: Want, callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates connection information about the datashare extension ability.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | callback function, no return value.  |

