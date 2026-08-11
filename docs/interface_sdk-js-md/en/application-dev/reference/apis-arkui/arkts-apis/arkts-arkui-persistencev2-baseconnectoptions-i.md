# BaseConnectOptions

Additional connect options for PersistenceV2.connect API.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface BaseConnectOptions<T extends object>--><!--Device-unnamed-export declare interface BaseConnectOptions<T extends object>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAutoSave

```TypeScript
enableAutoSave?: boolean
```

Enable autosave feature. Default value is true.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseConnectOptions-enableAutoSave?: boolean--><!--Device-BaseConnectOptions-enableAutoSave?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromJson

```TypeScript
fromJson?: FromJSONType<T>
```

Customize deserialize callback.If fromJson is not set, then default deserialization method will be used.

**Type:** [FromJSONType](arkts-arkui-fromjsontype-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseConnectOptions-fromJson?: FromJSONType<T>--><!--Device-BaseConnectOptions-fromJson?: FromJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toJson

```TypeScript
toJson?: ToJSONType<T>
```

Customize serialize callback.If toJson is not set, then default serialization method will be used.

**Type:** [ToJSONType](arkts-arkui-tojsontype-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseConnectOptions-toJson?: ToJSONType<T>--><!--Device-BaseConnectOptions-toJson?: ToJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

