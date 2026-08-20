# InstanceMethod

表示类或接口的实例方法。

**继承/实现关系：** InstanceMethod extends [Method](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-method-i-sys.md)

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-reflect-class InstanceMethod--><!--Device-reflect-class InstanceMethod-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## equals

```TypeScript
equals(other: InstanceMethod): boolean
```

比较两个实例方法是否相等。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-equals(other: InstanceMethod): boolean--><!--Device-InstanceMethod-equals(other: InstanceMethod): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | 用于比较的另一个实例方法对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个方法相等则返回true，否则返回false。 |

## invoke

```TypeScript
invoke(thisObj: Object, args?: FixedArray<Any>): Any
```

调用该实例方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-invoke(thisObj: Object, args?: FixedArray<Any>): Any--><!--Device-InstanceMethod-invoke(thisObj: Object, args?: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thisObj | Object | 是 | 调用该方法时使用的this对象。 |
| args | FixedArray&lt;Any&gt; | 否 | 调用该方法时传入的参数数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 该方法的执行结果。 |

## isAbstract

```TypeScript
isAbstract(): boolean
```

检查该方法是否为抽象方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isAbstract(): boolean--><!--Device-InstanceMethod-isAbstract(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该方法为抽象方法则返回true，否则返回false。 |

## isAsync

```TypeScript
isAsync(): boolean
```

检查该方法是否为async方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isAsync(): boolean--><!--Device-InstanceMethod-isAsync(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该方法为async则返回true，否则返回false。 |

## isFinal

```TypeScript
isFinal(): boolean
```

检查该方法是否为final方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isFinal(): boolean--><!--Device-InstanceMethod-isFinal(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该方法为final则返回true，否则返回false。 |

## isGetter

```TypeScript
isGetter(): boolean
```

检查该方法是否为getter方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isGetter(): boolean--><!--Device-InstanceMethod-isGetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该方法为getter则返回true，否则返回false。 |

## isSetter

```TypeScript
isSetter(): boolean
```

检查该方法是否为setter方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceMethod-isSetter(): boolean--><!--Device-InstanceMethod-isSetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该方法为setter则返回true，否则返回false。 |

