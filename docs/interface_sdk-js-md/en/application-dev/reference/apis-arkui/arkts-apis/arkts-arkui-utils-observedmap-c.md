# ObservedMap

继承自Map&lt;K, V&gt;，为可观察API操作的Map对象。详见  
[ObservedArray/ObservedMap/ObservedSet/ObservedDate：具有观察能力的Built-in类型](../../../ui/state-management-static/arkts-static-new-observed-built-in-types.md)。

**Inheritance/Implementation:** ObservedMap extends [Map<K, V>](../../apis-arkts/arkts-apis/arkts-arkts-collections-map-c.md/arkts-arkts-collections-map-c.md#set)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ObservedMap<K, V> extends Map<K, V>--><!--Device-unnamed-export declare class ObservedMap<K, V> extends Map<K, V>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor()
```

无参构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedMap-public constructor()--><!--Device-ObservedMap-public constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor(initialCapacity: int)
```

使用指定的容量创建ObservedMap实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedMap-public constructor(initialCapacity: int)--><!--Device-ObservedMap-public constructor(initialCapacity: int)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| initialCapacity | int | Yes | 指定的初始容量。 |

## constructor

```TypeScript
public constructor(entries: [K, V][])
```

使用键值对数组创建ObservedMap实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedMap-public constructor(entries: [K, V][])--><!--Device-ObservedMap-public constructor(entries: [K, V][])-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entries | [K, V][] | Yes | 初始键值对数组。 |

## constructor

```TypeScript
public constructor(map: Map<K, V>)
```

使用已有Map对象创建ObservedMap实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedMap-public constructor(map: Map<K, V>)--><!--Device-ObservedMap-public constructor(map: Map<K, V>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | Map&lt;K, V&gt; | Yes | 初始Map对象。 |

