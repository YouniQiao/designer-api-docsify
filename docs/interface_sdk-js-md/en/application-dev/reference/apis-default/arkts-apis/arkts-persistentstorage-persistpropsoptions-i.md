# PersistPropsOptions

指定持久化属性及其默认值的键值对对象，作为[persistProps](../../apis-arkui/arkts-apis/arkts-arkui-persistpropsoptions-i.md/arkts-arkui-persistpropsoptions-i.md)参数传入。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PersistPropsOptions<T>--><!--Device-unnamed-export declare interface PersistPropsOptions<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromJson

```TypeScript
fromJson?: FromJSONType<T>
```

默认值为undefined。见[FromJsonType](arkts-fromjsontype-t.md)，用于反序列化。对于复杂类型（除boolean、int、double、long、string外），开发者必须实现该方法才能成功反序列化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-fromJson?: FromJSONType<T>--><!--Device-PersistPropsOptions-fromJson?: FromJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toJson

```TypeScript
toJson?: ToJSONType<T>
```

默认值为undefined。见[ToJsonType](arkts-tojsontype-t.md)，用于序列化。对于复杂类型（除boolean、int、double、long、string外），开发者必须实现该方法才能成功序列化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-toJson?: ToJSONType<T>--><!--Device-PersistPropsOptions-toJson?: ToJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultValue

```TypeScript
defaultValue: T
```

当在[PersistentStorage](../../apis-arkui/arkts-apis/arkts-arkui-persistentstorage-c.md/arkts-arkui-persistentstorage-c.md)和  
[AppStorage](../../../reference/apis-arkui/arkui-ts/ts-state-management-Static-copy.md#appstorage)中未查询到key时，使用defaultValue中。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-defaultValue: T--><!--Device-PersistPropsOptions-defaultValue: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key: string
```

属性名。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistPropsOptions-key: string--><!--Device-PersistPropsOptions-key: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

