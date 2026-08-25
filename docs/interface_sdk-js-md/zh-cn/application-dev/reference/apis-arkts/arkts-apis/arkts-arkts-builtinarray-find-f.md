# find

## 导入模块

```TypeScript
```

## find

```TypeScript
export function find(self: FixedArray<boolean>, predicate: (value: boolean, index: int, array: FixedArray<boolean>)
    => boolean): Boolean | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;boolean & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: boolean, index: int, array: FixedArray & lt;boolean & gt;)     = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Boolean \| undefined |


## find

```TypeScript
export function find(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>) 
    => boolean): Byte | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;byte & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: byte, index: int, array: FixedArray & lt;byte & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Byte \| undefined |


## find

```TypeScript
export function find(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>) 
    => boolean): Short | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;short & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: short, index: int, array: FixedArray & lt;short & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Short \| undefined |


## find

```TypeScript
export function find(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>) 
    => boolean): Int | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;int & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: int, index: int, array: FixedArray & lt;int & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Int \| undefined |


## find

```TypeScript
export function find(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>) 
    => boolean): Long | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;long & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: long, index: int, array: FixedArray & lt;long & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Long \| undefined |


## find

```TypeScript
export function find(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>) 
    => boolean): Float | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;float & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: float, index: int, array: FixedArray & lt;float & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Float \| undefined |


## find

```TypeScript
export function find(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>) 
    => boolean): Double | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;double & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: double, index: int, array: FixedArray & lt;double & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Double \| undefined |


## find

```TypeScript
export function find(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>) 
    => boolean): Char | undefined
```

返回数组中第一个使predicate返回true的元素的值，若不存在则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;char & gt; | 是 |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | (value: char, index: int, array: FixedArray & lt;char & gt;)      = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Char \| undefined |
