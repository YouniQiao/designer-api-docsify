# Function

函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Function--><!--Device-unnamed-export interface Function-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## unsafeCall

```TypeScript
unsafeCall(...r: FixedArray<Any>): Any
```

使用指定的参数调用该函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Function-unsafeCall(...r: FixedArray<Any>): Any--><!--Device-Function-unsafeCall(...r: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | FixedArray&lt;Any&gt; | 是 | 参数列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 调用结果。 |

