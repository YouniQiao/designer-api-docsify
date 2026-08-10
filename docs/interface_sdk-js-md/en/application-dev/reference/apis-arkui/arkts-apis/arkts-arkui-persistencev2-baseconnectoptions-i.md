# BaseConnectOptions

connect参数类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface BaseConnectOptions<T extends object>--><!--Device-unnamed-export declare interface BaseConnectOptions<T extends object>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAutoSave

```TypeScript
enableAutoSave?: boolean
```

是否自动持久化存储数据，默认值为true。

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

转换JSON格式对象到存储对象的函数。

**Type:** [FromJSONType](../../apis-default/arkts-apis/arkts-fromjsontype-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseConnectOptions-fromJson?: FromJSONType<T>--><!--Device-BaseConnectOptions-fromJson?: FromJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toJson

```TypeScript
toJson?: ToJSONType<T>
```

转换存储对象到JSON格式对象的函数。

**Type:** [ToJSONType](../../apis-default/arkts-apis/arkts-tojsontype-t.md)&lt;T&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseConnectOptions-toJson?: ToJSONType<T>--><!--Device-BaseConnectOptions-toJson?: ToJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

