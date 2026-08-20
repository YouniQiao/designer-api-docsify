# encodeURIComponent

## 导入模块

```TypeScript
```

## encodeURIComponent

```TypeScript
export function encodeURIComponent(uriComponent: string | double | boolean): string
```

encodeURIComponent()函数对URI进行编码， 将其中的某些字符各自替换为一个、两个、三个或四个 转义序列，这些转义序列表示该字符的UTF-8编码 （仅当字符由两个代理项字符组成时，才会是 四个转义序列）。与encodeURI()相比，该函数 编码的字符更多，包括属于URI语法 组成部分的字符。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function encodeURIComponent(uriComponent: string | double | boolean): string--><!--Device-unnamed-export function encodeURIComponent(uriComponent: string | double | boolean): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriComponent | string \| double \| boolean | 是 | 待编码为URI 组成部分的字符串（如路径、查询字符串、片段 等）。其他类型的值会被转换为字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 新字符串，表示编码为URI组成部分后的 uriComponent。 |

