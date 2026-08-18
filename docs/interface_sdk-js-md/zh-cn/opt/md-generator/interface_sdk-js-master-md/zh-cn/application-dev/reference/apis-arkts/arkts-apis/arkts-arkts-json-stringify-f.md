# stringify

## 导入模块

```TypeScript
```

## stringify

```TypeScript
function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string
```

该方法将一个ArkTS对象或数组转换为JSON字符串，支持线性容器的转换，不支持非线性容器（传入非线性容器时无法正确序列化）。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-json-function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string--><!--Device-json-function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |
| replacer | (number \| string)[] \| null | 否 |
| space | string \| number | 否 |

**返回值：**

| 类型 |
| --- |
| string |


## stringify

```TypeScript
function stringify(value: Object, replacer?: Transformer, space?: string | number): string
```

该方法将一个ArkTS对象或数组转换为JSON字符串，支持线性容器的转换，不支持非线性容器。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-json-function stringify(value: Object, replacer?: Transformer, space?: string | number): string--><!--Device-json-function stringify(value: Object, replacer?: Transformer, space?: string | number): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |
| replacer | [Transformer](arkts-arkts-ason-transformer-t.md) | 否 |
| space | string \| number | 否 |

**返回值：**

| 类型 |
| --- |
| string |
