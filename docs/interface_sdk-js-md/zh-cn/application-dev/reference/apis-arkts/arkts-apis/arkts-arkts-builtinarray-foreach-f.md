# forEach

## 导入模块

```TypeScript
```

## forEach

```TypeScript
export function forEach(self: FixedArray<boolean>, callbackfn: (value: boolean, index: int, array: FixedArray<boolean>)
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<boolean>, callbackfn: (value: boolean, index: int, array: FixedArray<boolean>)    => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<boolean>, callbackfn: (value: boolean, index: int, array: FixedArray<boolean>)    => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: boolean, index: int, array: FixedArray&lt;boolean&gt;)     =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<byte>, callbackfn: (value: byte, index: int, array: FixedArray<byte>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<byte>, callbackfn: (value: byte, index: int, array: FixedArray<byte>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<byte>, callbackfn: (value: byte, index: int, array: FixedArray<byte>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: byte, index: int, array: FixedArray&lt;byte&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<short>, callbackfn: (value: short, index: int, array: FixedArray<short>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<short>, callbackfn: (value: short, index: int, array: FixedArray<short>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<short>, callbackfn: (value: short, index: int, array: FixedArray<short>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: short, index: int, array: FixedArray&lt;short&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<int>, callbackfn: (value: int, index: int, array: FixedArray<int>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<int>, callbackfn: (value: int, index: int, array: FixedArray<int>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<int>, callbackfn: (value: int, index: int, array: FixedArray<int>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: int, index: int, array: FixedArray&lt;int&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<long>, callbackfn: (value: long, index: int, array: FixedArray<long>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<long>, callbackfn: (value: long, index: int, array: FixedArray<long>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<long>, callbackfn: (value: long, index: int, array: FixedArray<long>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: long, index: int, array: FixedArray&lt;long&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<float>, callbackfn: (value: float, index: int, array: FixedArray<float>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<float>, callbackfn: (value: float, index: int, array: FixedArray<float>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<float>, callbackfn: (value: float, index: int, array: FixedArray<float>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: float, index: int, array: FixedArray&lt;float&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<double>, callbackfn: (value: double, index: int, array: FixedArray<double>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<double>, callbackfn: (value: double, index: int, array: FixedArray<double>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<double>, callbackfn: (value: double, index: int, array: FixedArray<double>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: double, index: int, array: FixedArray&lt;double&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |


## forEach

```TypeScript
export function forEach(self: FixedArray<char>, callbackfn: (value: char, index: int, array: FixedArray<char>) 
    => void): void
```

对数组中的每个元素执行指定的操作。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function forEach(self: FixedArray<char>, callbackfn: (value: char, index: int, array: FixedArray<char>)     => void): void--><!--Device-unnamed-export function forEach(self: FixedArray<char>, callbackfn: (value: char, index: int, array: FixedArray<char>)     => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`forEach`操作的数组。 |
| callbackfn | (value: char, index: int, array: FixedArray&lt;char&gt;)      =&gt; void | 是 | 最多接受三个参数的函数。forEach会对稀疏数组中的每个元素 调用一次该函数。 |

