# copyTo

## 导入模块

```TypeScript
```

## copyTo

```TypeScript
export function copyTo(src: FixedArray<boolean>, dst: FixedArray<boolean>, dstStart: int, srcStart: int, srcEnd: int)
    : void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<boolean>, dst: FixedArray<boolean>, dstStart: int, srcStart: int, srcEnd: int)    : void--><!--Device-unnamed-export function copyTo(src: FixedArray<boolean>, dst: FixedArray<boolean>, dstStart: int, srcStart: int, srcEnd: int)    : void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;boolean&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;boolean&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<byte>, dst: FixedArray<byte>, dstStart: int, srcStart: int, srcEnd: int): void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<byte>, dst: FixedArray<byte>, dstStart: int, srcStart: int, srcEnd: int): void--><!--Device-unnamed-export function copyTo(src: FixedArray<byte>, dst: FixedArray<byte>, dstStart: int, srcStart: int, srcEnd: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;byte&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;byte&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<short>, dst: FixedArray<short>, dstStart: int, srcStart: int, srcEnd: int): void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<short>, dst: FixedArray<short>, dstStart: int, srcStart: int, srcEnd: int): void--><!--Device-unnamed-export function copyTo(src: FixedArray<short>, dst: FixedArray<short>, dstStart: int, srcStart: int, srcEnd: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;short&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;short&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<int>, dst: FixedArray<int>, dstStart: int, srcStart: int, srcEnd: int): void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<int>, dst: FixedArray<int>, dstStart: int, srcStart: int, srcEnd: int): void--><!--Device-unnamed-export function copyTo(src: FixedArray<int>, dst: FixedArray<int>, dstStart: int, srcStart: int, srcEnd: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;int&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;int&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<long>, dst: FixedArray<long>, dstStart: int, srcStart: int, srcEnd: int): void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<long>, dst: FixedArray<long>, dstStart: int, srcStart: int, srcEnd: int): void--><!--Device-unnamed-export function copyTo(src: FixedArray<long>, dst: FixedArray<long>, dstStart: int, srcStart: int, srcEnd: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;long&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;long&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<float>, dst: FixedArray<float>, dstStart: int, srcStart: int, srcEnd: int):
    void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<float>, dst: FixedArray<float>, dstStart: int, srcStart: int, srcEnd: int):    void--><!--Device-unnamed-export function copyTo(src: FixedArray<float>, dst: FixedArray<float>, dstStart: int, srcStart: int, srcEnd: int):    void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;float&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;float&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<double>, dst: FixedArray<double>, dstStart: int, srcStart: int, srcEnd: int):
    void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<double>, dst: FixedArray<double>, dstStart: int, srcStart: int, srcEnd: int):    void--><!--Device-unnamed-export function copyTo(src: FixedArray<double>, dst: FixedArray<double>, dstStart: int, srcStart: int, srcEnd: int):    void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;double&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;double&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<char>, dst: FixedArray<char>, dstStart: int, srcStart: int, srcEnd: int): void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<char>, dst: FixedArray<char>, dstStart: int, srcStart: int, srcEnd: int): void--><!--Device-unnamed-export function copyTo(src: FixedArray<char>, dst: FixedArray<char>, dstStart: int, srcStart: int, srcEnd: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;char&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;char&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |


## copyTo

```TypeScript
export function copyTo(src: FixedArray<Any>, dst: FixedArray<Any>, dstStart: int, srcStart: int, srcEnd: int): void
```

按传入的索引将src数组复制到dst中。 dst必须有足够的空间，否则可能发生越界。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function copyTo(src: FixedArray<Any>, dst: FixedArray<Any>, dstStart: int, srcStart: int, srcEnd: int): void--><!--Device-unnamed-export function copyTo(src: FixedArray<Any>, dst: FixedArray<Any>, dstStart: int, srcStart: int, srcEnd: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | FixedArray&lt;Any&gt; | 是 | 复制的源数组。 |
| dst | FixedArray&lt;Any&gt; | 是 | 复制的目标数组。 |
| dstStart | int | 是 | 在dst中开始写入的索引。 <br>取值约束：应为整数。 |
| srcStart | int | 是 | 在src中开始复制的索引。 <br>取值约束：应为整数。 |
| srcEnd | int | 是 | 在src中停止复制的索引（不包含），即不复制src[srcEnd]。 <br>取值约束：应为整数。 |

