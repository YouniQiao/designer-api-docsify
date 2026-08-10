# ObservedArray

继承自Array&lt;T&gt;，为可观察API操作的Array对象。详见  
[ObservedArray/ObservedMap/ObservedSet/ObservedDate：具有观察能力的Built-in类型](../../../ui/state-management-static/arkts-static-new-observed-built-in-types.md)。

**Inheritance/Implementation:** ObservedArray extends [Array<T>](Array<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ObservedArray<T> extends Array<T>--><!--Device-unnamed-export declare class ObservedArray<T> extends Array<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor()
```

无参构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedArray-public constructor()--><!--Device-ObservedArray-public constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor(first: T, ...d: T[])
```

使用元素列表初始化ObservedArray实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedArray-public constructor(first: T, ...d: T[])--><!--Device-ObservedArray-public constructor(first: T, ...d: T[])-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | T | Yes | 第一个元素。 |
| d | T[] | Yes | 其余元素组成的数组，默认为[]。 |

## constructor

```TypeScript
public constructor(arrayLen: int, initializer: ObservedArrayInitializer<T>)
```

使用指定的长度和初始化函数初始化ObservedArray实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedArray-public constructor(arrayLen: int, initializer: ObservedArrayInitializer<T>)--><!--Device-ObservedArray-public constructor(arrayLen: int, initializer: ObservedArrayInitializer<T>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLen | int | Yes | 数组初始长度。 |
| initializer | [ObservedArrayInitializer](arkts-arkui-observedarrayinitializer-t.md)&lt;T&gt; | Yes | 数组元素初始化函数。 |

