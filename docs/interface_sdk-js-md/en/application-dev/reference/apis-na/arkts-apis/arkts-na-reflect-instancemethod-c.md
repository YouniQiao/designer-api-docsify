# InstanceMethod

Represents an instance method of a class or interface.

**Inheritance/Implementation:** InstanceMethod extends [Method](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-method-i-sys.md#method-system-api)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-reflect-class InstanceMethod--><!--Device-reflect-class InstanceMethod-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## equals

```TypeScript
equals(other: InstanceMethod): boolean
```

Compares whether two instance methods are equal.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-equals(other: InstanceMethod): boolean--><!--Device-InstanceMethod-equals(other: InstanceMethod): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [InstanceMethod](arkts-na-reflect-instancemethod-c.md) | Yes | Another instance method object used for comparison. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the two methods are equal, otherwise returns false. |

## invoke

```TypeScript
invoke(thisObj: Object, args?: FixedArray<Any>): Any
```

Invokes this instance method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-invoke(thisObj: Object, args?: FixedArray<Any>): Any--><!--Device-InstanceMethod-invoke(thisObj: Object, args?: FixedArray<Any>): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| thisObj | Object | Yes | The this object used when invoking the method. |
| args | FixedArray&lt;Any&gt; | No | args The argument array passed when invoking the method. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | The execution result of the method. |

## isAbstract

```TypeScript
isAbstract(): boolean
```

Checks if the method is an abstract method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-isAbstract(): boolean--><!--Device-InstanceMethod-isAbstract(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the method is abstract, otherwise returns false. |

## isAsync

```TypeScript
isAsync(): boolean
```

Checks if the method is an async method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-isAsync(): boolean--><!--Device-InstanceMethod-isAsync(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the method is async, otherwise returns false. |

## isFinal

```TypeScript
isFinal(): boolean
```

Checks if the method is a final method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-isFinal(): boolean--><!--Device-InstanceMethod-isFinal(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the method is final, otherwise returns false. |

## isGetter

```TypeScript
isGetter(): boolean
```

Checks if the method is a getter method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-isGetter(): boolean--><!--Device-InstanceMethod-isGetter(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the method is a getter, otherwise returns false. |

## isSetter

```TypeScript
isSetter(): boolean
```

Checks if the method is a setter method.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceMethod-isSetter(): boolean--><!--Device-InstanceMethod-isSetter(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the method is a setter, otherwise returns false. |

