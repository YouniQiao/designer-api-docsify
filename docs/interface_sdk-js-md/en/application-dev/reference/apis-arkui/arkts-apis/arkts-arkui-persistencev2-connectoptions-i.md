# ConnectOptions

globalConnect参数类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ConnectOptions<T extends object>--><!--Device-unnamed-export declare interface ConnectOptions<T extends object>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultCreator

```TypeScript
defaultCreator?: StorageDefaultCreator<T>
```

默认数据的构造器，默认值为undefined，建议传递，如果globalConnect是第一次连接key，不传会报错。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptions-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## areaMode

```TypeScript
areaMode?: contextConstant.AreaMode
```

加密级别：EL1-EL5，详见[加密级别](../../../application-models/application-context-stage.md#获取和修改加密分区)，不传时默认为EL2，不同加密级别对应不同的加密分区，即不同的存储路径。

**Type:** contextConstant.AreaMode

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-areaMode?: contextConstant.AreaMode--><!--Device-ConnectOptions-areaMode?: contextConstant.AreaMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultSubCreators

```TypeScript
defaultSubCreators?: StorageDefaultSubCreators
```

保存对象类型及其默认构造器的Map。用于恢复内层对象数据。默认值为undefined。

**Type:** [StorageDefaultSubCreators](arkts-arkui-storagedefaultsubcreators-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-defaultSubCreators?: StorageDefaultSubCreators--><!--Device-ConnectOptions-defaultSubCreators?: StorageDefaultSubCreators-End-->

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

<!--Device-ConnectOptions-enableAutoSave?: boolean--><!--Device-ConnectOptions-enableAutoSave?: boolean-End-->

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

<!--Device-ConnectOptions-fromJson?: FromJSONType<T>--><!--Device-ConnectOptions-fromJson?: FromJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

传入的key，不传则使用type的名字作为key。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-key?: string--><!--Device-ConnectOptions-key?: string-End-->

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

<!--Device-ConnectOptions-toJson?: ToJSONType<T>--><!--Device-ConnectOptions-toJson?: ToJSONType<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: Class
```

指定的类型。

**Type:** [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectOptions-type: Class--><!--Device-ConnectOptions-type: Class-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

