# QueryCustomContentEvent

```TypeScript
type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>
```

The query custom content event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>--><!--Device-avMusicTemplate-type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| queryType | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | query type  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CustomElement&gt; | (CustomElement) returned through promise  |

