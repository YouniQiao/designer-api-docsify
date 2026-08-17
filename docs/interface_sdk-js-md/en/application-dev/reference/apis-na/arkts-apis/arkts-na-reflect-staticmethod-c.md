# StaticMethod

Represents static method of class

**Inheritance/Implementation:** StaticMethod extends [Method](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-method-i-sys.md#method-system-api)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-reflect-class StaticMethod--><!--Device-reflect-class StaticMethod-End-->

**System capability:** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: StaticMethod): boolean
```

Compare whether the current Static Method object is equal to another object.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticMethod-equals(other: StaticMethod): boolean--><!--Device-StaticMethod-equals(other: StaticMethod): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [StaticMethod](arkts-na-reflect-staticmethod-c.md) | Yes | Another Static Method object used for comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If two objects point to the same method, return true; otherwise, return false. |

## invoke

```TypeScript
invoke(args?: FixedArray<Any>): Any
```

Invokes a method

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticMethod-invoke(args?: FixedArray<Any>): Any--><!--Device-StaticMethod-invoke(args?: FixedArray<Any>): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | FixedArray&lt;Any&gt; | No | method parameters |

**Return value:**

| Type | Description |
| --- | --- |
| Any | method return value. `undefined` for `void`. |

## isAsyn

```TypeScript
isAsyn(): boolean
```

Determine whether the static method is an asynchronous method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticMethod-isAsyn(): boolean--><!--Device-StaticMethod-isAsyn(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If it is an asynchronous method, return true; otherwise, return false. |

## isGetter

```TypeScript
isGetter(): boolean
```

Determine whether the static method is a getter visitor for a property.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticMethod-isGetter(): boolean--><!--Device-StaticMethod-isGetter(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If it is a getter visitor, return true; otherwise, return false. |

## isSetter

```TypeScript
isSetter(): boolean
```

Determine whether the static method is a setter visitor for a property.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticMethod-isSetter(): boolean--><!--Device-StaticMethod-isSetter(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If it is a setter visitor, return true; otherwise, return false. |

