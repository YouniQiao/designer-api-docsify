# GetLiveFormStatusCallback (System API)

```TypeScript
type GetLiveFormStatusCallback = () => Record<string, string>
```

Get live form status info callback

**Since:** 20

<!--Device-formInfo-type GetLiveFormStatusCallback = () => Record<string, string>--><!--Device-formInfo-type GetLiveFormStatusCallback = () => Record<string, string>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Record&lt;string, string&gt; | form status info, the key is formId, value is one of "INACTIVE" "PAUSE" "ACTIVE". |
