# InstanceMethod

Represents an instance method of a class or interface.

**继承/实现关系：** InstanceMethod extends [Method](Method)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-reflect-class InstanceMethod extends Method--><!--Device-reflect-class InstanceMethod extends Method-End-->

**系统能力：** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: InstanceMethod): boolean
```

Compares whether two instance methods are equal.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-equals(other: InstanceMethod): boolean--><!--Device-InstanceMethod-equals(other: InstanceMethod): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | Another instance method object used for comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the two methods are equal, otherwise returns false. |

## invoke

```TypeScript
invoke(thisObj: Object, args?: FixedArray<Any>): Any
```

Invokes this instance method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-invoke(thisObj: Object, args?: FixedArray<Any>): Any--><!--Device-InstanceMethod-invoke(thisObj: Object, args?: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thisObj | Object | 是 | The this object used when invoking the method. |
| args | FixedArray&lt;Any&gt; | 否 | args The argument array passed when invoking the method. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | The execution result of the method. |

## isAbstract

```TypeScript
isAbstract(): boolean
```

Checks if the method is an abstract method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isAbstract(): boolean--><!--Device-InstanceMethod-isAbstract(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the method is abstract, otherwise returns false. |

## isAsync

```TypeScript
isAsync(): boolean
```

Checks if the method is an async method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isAsync(): boolean--><!--Device-InstanceMethod-isAsync(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the method is async, otherwise returns false. |

## isFinal

```TypeScript
isFinal(): boolean
```

Checks if the method is a final method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isFinal(): boolean--><!--Device-InstanceMethod-isFinal(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the method is final, otherwise returns false. |

## isGetter

```TypeScript
isGetter(): boolean
```

Checks if the method is a getter method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isGetter(): boolean--><!--Device-InstanceMethod-isGetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the method is a getter, otherwise returns false. |

## isSetter

```TypeScript
isSetter(): boolean
```

Checks if the method is a setter method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isSetter(): boolean--><!--Device-InstanceMethod-isSetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the method is a setter, otherwise returns false. |

