# PersistPropsOptions

Defining PersistPropsOptions interface

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface PersistPropsOptions--><!--Device-unnamed-export declare interface PersistPropsOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultValue

```TypeScript
defaultValue: T
```

If AppStorage does not include this property it will be initialized with this value

**Type:** T

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-defaultValue: T--><!--Device-PersistPropsOptions-defaultValue: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromJson

```TypeScript
fromJson?: FromJSONType<T>
```

Used to deserialize data

**Type:** [FromJSONType](arkts-na-fromjsontype-t.md)&lt;T&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-fromJson?: FromJSONType<T>--><!--Device-PersistPropsOptions-fromJson?: FromJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key: string
```

Property name

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-key: string--><!--Device-PersistPropsOptions-key: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toJson

```TypeScript
toJson?: ToJSONType<T>
```

Used to serialize data

**Type:** [ToJSONType](arkts-na-tojsontype-t.md)&lt;T&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-toJson?: ToJSONType<T>--><!--Device-PersistPropsOptions-toJson?: ToJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

