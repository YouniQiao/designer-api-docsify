# choose

## 导入模块

```TypeScript
```

## choose

```TypeScript
declare function choose(types?: string[]): Promise<string>
```

通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | string[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
let types: Array<string> = [];
document.choose(types);
```

```TypeScript
let uri: string = "";
document.choose((err: TypeError, uri: string) => {
  //do something with uri
});
```

```TypeScript
let types: Array<string> = [];
let uri: string = "";
document.choose(types, (err: TypeError, uri: string) => {
  //do something with uri
});
```


## choose

```TypeScript
declare function choose(callback: AsyncCallback<string>): void
```

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

参见 [choose](#choose)


## choose

```TypeScript
declare function choose(types: string[], callback: AsyncCallback<string>): void
```

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

参见 [choose](#choose)
