# ObservedSet

继承自Set&lt;K&gt;，为可观察API操作的Set对象。详见  
[ObservedArray/ObservedMap/ObservedSet/ObservedDate：具有观察能力的Built-in类型](../../../ui/state-management-static/arkts-static-new-observed-built-in-types.md)。

**Inheritance/Implementation:** ObservedSet extends [Set<K>](Set<K>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ObservedSet<K> extends Set<K>--><!--Device-unnamed-export declare class ObservedSet<K> extends Set<K>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor()
```

无参构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedSet-public constructor()--><!--Device-ObservedSet-public constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor(bucketsCount: int)
```

使用指定的容量创建ObservedSet实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedSet-public constructor(bucketsCount: int)--><!--Device-ObservedSet-public constructor(bucketsCount: int)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bucketsCount | int | Yes | 指定的初始容量。 |

## constructor

```TypeScript
public constructor(values: K[])
```

使用元素数组创建ObservedSet实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedSet-public constructor(values: K[])--><!--Device-ObservedSet-public constructor(values: K[])-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | K[] | Yes | 初始元素数组。 |

## constructor

```TypeScript
public constructor(set: Set<K>)
```

使用已有Set对象创建ObservedSet实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedSet-public constructor(set: Set<K>)--><!--Device-ObservedSet-public constructor(set: Set<K>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| set | Set&lt;K&gt; | Yes | 初始Set对象。 |

