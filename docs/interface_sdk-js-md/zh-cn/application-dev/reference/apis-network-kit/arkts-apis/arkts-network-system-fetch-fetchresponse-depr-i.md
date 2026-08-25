# FetchResponse

**表2** responseType与success中data关系  
| responseType | [data](#data) | 说明 | | -------- | -------- | -------- | | 无 | string | 服务器返回的header中的type如果是text/\*或application/json、application/javascript、application/xml，值为文本内容。 | | text | string | 返回文本内容。 | | [json](../../apis-arkts/arkts-apis/arkts-util-json.md) | Object |

**起始版本：** 3

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
```

## code

```TypeScript
code: number
```

表示服务器的状态code。

**类型：** number

**起始版本：** 3

**系统能力：** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | object
```

返回数据类型由responseType确定，详见表 responseType与success中data关系。

**类型：** string \| object

**起始版本：** 3

**系统能力：** SystemCapability.Communication.NetStack

## headers

```TypeScript
headers: Object
```

表示服务器response的所有header。

**类型：** Object

**起始版本：** 3

**系统能力：** SystemCapability.Communication.NetStack
