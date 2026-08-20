# ConnectOptions

Define ConnectOptions class.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface ConnectOptions--><!--Device-unnamed-export declare interface ConnectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## areaMode

```TypeScript
areaMode?: contextConstant.AreaMode
```

Define encrypted partition for data storage. if not passed in, the default value is El2.

**Type:** contextConstant.AreaMode

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-areaMode?: contextConstant.AreaMode--><!--Device-ConnectOptions-areaMode?: contextConstant.AreaMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultCreator

```TypeScript
defaultCreator?: StorageDefaultCreator<T>
```

Define the function generating the default value. If defaultCreator is not set, then existing data will be retrieved, or return undefined.

**Type:** [StorageDefaultCreator](arkts-storagedefaultcreator-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptions-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultSubCreators

```TypeScript
defaultSubCreators?: StorageDefaultSubCreators
```

Map that contains Class and its default creator. It is used to restore inner object. The default value is undefined.

**Type:** [StorageDefaultSubCreators](arkts-storagedefaultsubcreators-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-defaultSubCreators?: StorageDefaultSubCreators--><!--Device-ConnectOptions-defaultSubCreators?: StorageDefaultSubCreators-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAutoSave

```TypeScript
enableAutoSave?: boolean
```

Enable autosave feature. Default value is true.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-enableAutoSave?: boolean--><!--Device-ConnectOptions-enableAutoSave?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromJson

```TypeScript
fromJson?: FromJSONType<T>
```

Customize deserialize callback. If fromJson is not set, then default deserialization method will be used.

**Type:** [FromJSONType](../../apis-arkui/arkts-apis/arkts-arkui-fromjsontype-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-fromJson?: FromJSONType<T>--><!--Device-ConnectOptions-fromJson?: FromJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

Defines alias name for the key. If key is not set, type will be used to find matching data. key should not be more than 1024 characters, or undefined will be returned.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-key?: string--><!--Device-ConnectOptions-key?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toJson

```TypeScript
toJson?: ToJSONType<T>
```

Customize serialize callback. If toJson is not set, then default serialization method will be used.

**Type:** [ToJSONType](../../apis-arkui/arkts-apis/arkts-arkui-tojsontype-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-toJson?: ToJSONType<T>--><!--Device-ConnectOptions-toJson?: ToJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: Class
```

Define class constructor

**Type:** [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-type: Class--><!--Device-ConnectOptions-type: Class-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

