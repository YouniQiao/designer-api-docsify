# Constructor

Represents a class constructor.

**继承/实现关系：** Constructor extends [Method](Method)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-class Constructor extends Method--><!--Device-unnamed-class Constructor extends Method-End-->

**系统能力：** SystemCapability.Utils.Lang

## createInstance

```TypeScript
public createInstance(args?: FixedArray<Any>): Any
```

Creates a new instance of its belonging class using this constructor.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Constructor-public createInstance(args?: FixedArray<Any>): Any--><!--Device-Constructor-public createInstance(args?: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | FixedArray&lt;Any&gt; | 否 | args The argument list for the constructor. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | The newly created class instance. |

## equals

```TypeScript
public equals(other: Constructor): boolean
```

Compares whether the current constructor object is equal to another constructor object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Constructor-public equals(other: Constructor): boolean--><!--Device-Constructor-public equals(other: Constructor): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Constructor](arkts-arkts-reflectconstructor-constructor-c.md) | 是 | Another constructor object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the two constructor objects are equal, otherwise returns false. |

