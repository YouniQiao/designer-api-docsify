# ObservedArray

Observable Array base class.

**Inheritance/Implementation:** ObservedArray extends [Array<T>](Array<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ObservedArray<T> extends Array<T>--><!--Device-unnamed-export declare class ObservedArray<T> extends Array<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor()
```

No arg constructor for observable array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedArray-public constructor()--><!--Device-ObservedArray-public constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
public constructor(first: T, ...d: T[])
```

Elements constructor for observable array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedArray-public constructor(first: T, ...d: T[])--><!--Device-ObservedArray-public constructor(first: T, ...d: T[])-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | T | Yes | first element. |
| d | T[] | Yes | more elements. |

## constructor

```TypeScript
public constructor(arrayLen: int, initializer: ObservedArrayInitializer<T>)
```

Array length and initializer constructor for observable array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedArray-public constructor(arrayLen: int, initializer: ObservedArrayInitializer<T>)--><!--Device-ObservedArray-public constructor(arrayLen: int, initializer: ObservedArrayInitializer<T>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLen | int | Yes | initial array length |
| initializer | [ObservedArrayInitializer](arkts-arkui-observedarrayinitializer-t.md)&lt;T&gt; | Yes | element initializer. |

