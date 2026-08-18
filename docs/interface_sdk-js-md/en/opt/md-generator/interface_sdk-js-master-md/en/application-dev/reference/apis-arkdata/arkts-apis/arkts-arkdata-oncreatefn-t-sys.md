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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
