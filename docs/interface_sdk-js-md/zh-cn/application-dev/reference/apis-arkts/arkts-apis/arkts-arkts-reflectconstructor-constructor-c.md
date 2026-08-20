# Constructor

表示类的构造函数。

**继承/实现关系：** Constructor extends [Method](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-method-i-sys.md)

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-class Constructor--><!--Device-unnamed-class Constructor-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## createInstance

```TypeScript
public createInstance(args?: FixedArray<Any>): Any
```

使用该构造函数创建其所属类的新实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Constructor-public createInstance(args?: FixedArray<Any>): Any--><!--Device-Constructor-public createInstance(args?: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | FixedArray&lt;Any&gt; | 否 | 构造函数的参数列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 新创建的类实例。 |

## equals

```TypeScript
public equals(other: Constructor): boolean
```

比较当前构造函数对象是否与另一个构造函数对象相等。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Constructor-public equals(other: Constructor): boolean--><!--Device-Constructor-public equals(other: Constructor): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Constructor](arkts-arkts-reflectconstructor-constructor-c.md) | 是 | 待比较的另一个构造函数对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个构造函数对象相等则返回true，否则返回false。 |

