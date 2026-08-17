# PersistentStorage

Defines the PersistentStorage interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class PersistentStorage--><!--Device-unnamed-export declare class PersistentStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteProp

```TypeScript
static deleteProp(key: string): void
```

Reverse of @see persistProp

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static deleteProp(key: string): void--><!--Device-PersistentStorage-static deleteProp(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | no longer persist the property named key |

## keys

```TypeScript
static keys(): Array<string>
```

Inform persisted AppStorage property names

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static keys(): Array<string>--><!--Device-PersistentStorage-static keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | array of AppStorage keys |

## persistProp

```TypeScript
static persistProp<T>(key: string, defaultValue: T, toJson?: ToJSONType<T>, fromJson?: FromJSONType<T>): boolean
```

Add property 'key' to AppStorage properties whose current value will be persistent. If AppStorage does not include this property it will be added and initializes with given value

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static persistProp<T>(key: string, defaultValue: T, toJson?: ToJSONType<T>, fromJson?: FromJSONType<T>): boolean--><!--Device-PersistentStorage-static persistProp<T>(key: string, defaultValue: T, toJson?: ToJSONType<T>, fromJson?: FromJSONType<T>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | property name |
| defaultValue | T | Yes | If AppStorage does not include this property it will be initialized with this value |
| toJson | [ToJSONType](arkts-na-tojsontype-t.md)&lt;T&gt; | No | serialization function |
| fromJson | [FromJSONType](arkts-na-fromjsontype-t.md)&lt;T&gt; | No | deserialization function |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## persistProps

```TypeScript
static persistProps(props: PersistPropsOptions<Any>[]): void
```

Persist given AppStorage properties with given names. If a property does not exist in AppStorage, add it and initialize it with given value works as @see persistProp for multiple properties.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static persistProps(props: PersistPropsOptions<Any>[]): void--><!--Device-PersistentStorage-static persistProps(props: PersistPropsOptions<Any>[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| props | [PersistPropsOptions](arkts-na-persistentstorage-persistpropsoptions-i.md)&lt;Any&gt;[] | Yes | persistent parameter |

