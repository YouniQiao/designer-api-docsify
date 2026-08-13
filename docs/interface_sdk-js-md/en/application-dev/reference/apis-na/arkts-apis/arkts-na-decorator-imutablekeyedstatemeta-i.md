# IMutableKeyedStateMeta

Define mutable state meta interface with key.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface IMutableKeyedStateMeta--><!--Device-unnamed-export declare interface IMutableKeyedStateMeta-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addRef

```TypeScript
addRef(key: string): void
```

Collect the dependancy for UI component with state variable based on given key

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMutableKeyedStateMeta-addRef(key: string): void--><!--Device-IMutableKeyedStateMeta-addRef(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes |  |

## addRef

```TypeScript
addRef(index: int): void
```

Collect the dependancy for UI component with state variable based on given key

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMutableKeyedStateMeta-addRef(index: int): void--><!--Device-IMutableKeyedStateMeta-addRef(index: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

## fireChange

```TypeScript
fireChange(key: string): void
```

Notify UI component with given key to update when state variable is changed

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMutableKeyedStateMeta-fireChange(key: string): void--><!--Device-IMutableKeyedStateMeta-fireChange(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes |  |

## fireChange

```TypeScript
fireChange(index: int): void
```

Notify UI component with given key to update when state variable is changed

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMutableKeyedStateMeta-fireChange(index: int): void--><!--Device-IMutableKeyedStateMeta-fireChange(index: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

