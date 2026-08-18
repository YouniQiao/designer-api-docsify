# has

## 导入模块

```TypeScript
```

## has

```TypeScript
function has(obj: object, property: string): boolean
```

检查ArkTS对象是否包含某种属性，可用于[JSON.parse](arkts-arkts-json-parse-f.md#parse)解析JSON字符串之后。 has接口仅支持最外层为字典形式（即大括号而非中括号包围）的合法JSON串，传入非字典形式的对象时无法正确判断属性是否存在。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-json-function has(obj: object, property: string): boolean--><!--Device-json-function has(obj: object, property: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | object | 是 |
| property | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
