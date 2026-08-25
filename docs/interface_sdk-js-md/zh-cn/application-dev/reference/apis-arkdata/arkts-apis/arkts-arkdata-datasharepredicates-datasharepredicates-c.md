# DataSharePredicates

提供用于不同实现不同查询方法的数据共享谓词。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

## 导入模块

```TypeScript
import { dataSharePredicates } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): DataSharePredicates
```

该接口用于将和条件添加到谓词中。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## beginWrap

```TypeScript
beginWrap(): DataSharePredicates
```

该接口用于向谓词添加左括号，相当于sql语句的“(”，必须和右括号一起使用。目前仅关系型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值在指定范围内的字段。包含两端边界值，为左闭右闭区间。目前仅关系型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## endWrap

```TypeScript
endWrap(): DataSharePredicates
```

该接口用于向谓词添加右括号，相当于sql语句的“)”，必须和左括号一起使用。目前仅关系型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值等于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值大于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值大于或等于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): DataSharePredicates
```

该接口用于配置谓词以匹配值在指定范围内的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值小于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值小于或等于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## like

```TypeScript
like(field: string, value: string): DataSharePredicates
```

该接口用于配置谓词以匹配指定通配符表达式的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## limit

```TypeScript
limit(total: number, offset: number): DataSharePredicates
```

该接口用于配置谓词以指定结果数和起始位置。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| total | number | 是 |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值超出指定范围的字段。不包含两端边界值，为左开右开区间。目前仅关系型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): DataSharePredicates
```

该接口用于配置谓词以匹配值不等于指定值的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): DataSharePredicates
```

该接口用于配置谓词以匹配值不在指定范围内的字段。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## or

```TypeScript
or(): DataSharePredicates
```

该接口用于将或条件添加到谓词中。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): DataSharePredicates
```

该接口用于配置谓词以匹配其值按升序排序的列。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): DataSharePredicates
```

该接口用于配置谓词以匹配其值按降序排序的列。目前仅关系型数据库及键值型数据库支持该谓词。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |
