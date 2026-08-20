# StaticMethod

表示类的静态方法。

**继承/实现关系：** StaticMethod extends [Method](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-method-i-sys.md)

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-reflect-class StaticMethod--><!--Device-reflect-class StaticMethod-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## equals

```TypeScript
equals(other: StaticMethod): boolean
```

比较当前静态方法对象是否与另一个对象相等。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-equals(other: StaticMethod): boolean--><!--Device-StaticMethod-equals(other: StaticMethod): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [StaticMethod](arkts-arkts-reflect-staticmethod-c.md) | 是 | 用于比较的另一个静态方法对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个对象指向同一方法则返回true，否则返回false。 |

## invoke

```TypeScript
invoke(args?: FixedArray<Any>): Any
```

调用方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-invoke(args?: FixedArray<Any>): Any--><!--Device-StaticMethod-invoke(args?: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | FixedArray&lt;Any&gt; | 否 | 方法参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 方法的返回值。对于`void`返回`undefined`。 |

## isAsyn

```TypeScript
isAsyn(): boolean
```

判断该静态方法是否为异步方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-isAsyn(): boolean--><!--Device-StaticMethod-isAsyn(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是异步方法则返回true，否则返回false。 |

## isGetter

```TypeScript
isGetter(): boolean
```

判断该静态方法是否为属性的getter访问器。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-isGetter(): boolean--><!--Device-StaticMethod-isGetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是getter访问器则返回true，否则返回false。 |

## isSetter

```TypeScript
isSetter(): boolean
```

判断该静态方法是否为属性的setter访问器。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-isSetter(): boolean--><!--Device-StaticMethod-isSetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是setter访问器则返回true，否则返回false。 |

