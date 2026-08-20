# AggregateError

AggregateError对象表示需要将多个错误包装为 单个错误时的错误。

**继承/实现关系：** AggregateError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AggregateError--><!--Device-unnamed-export class AggregateError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError
```

使用指定的错误信息和错误相关信息构造新的AggregateError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError--><!--Device-AggregateError-static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Iterable&lt;Error&gt; | 是 | 待聚合的错误。 |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) | 新创建的AggregateError实例。 |

## $_invoke

```TypeScript
static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError
```

使用指定的错误信息和错误相关信息构造新的AggregateError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError--><!--Device-AggregateError-static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Error[] | 是 | 待聚合的错误。 |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) | 新创建的AggregateError实例。 |

## constructor

```TypeScript
constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)
```

使用指定的错误集合、错误信息和错误相关信息构造新的AggregateError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)--><!--Device-AggregateError-constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Iterable&lt;Error&gt; | 是 | 待聚合的错误。 |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

## constructor

```TypeScript
constructor(errors: Error[], message?: string, options?: ErrorOptions)
```

使用指定的错误集合、错误信息和错误相关信息构造新的AggregateError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-constructor(errors: Error[], message?: string, options?: ErrorOptions)--><!--Device-AggregateError-constructor(errors: Error[], message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Error[] | 是 | 待聚合的错误。 |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

## errors

```TypeScript
errors: Array<Error>
```

定义聚合错误的数组。

**类型：** Array&lt;Error&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-errors: Array<Error>--><!--Device-AggregateError-errors: Array<Error>-End-->

**系统能力：** SystemCapability.Utils.Lang

