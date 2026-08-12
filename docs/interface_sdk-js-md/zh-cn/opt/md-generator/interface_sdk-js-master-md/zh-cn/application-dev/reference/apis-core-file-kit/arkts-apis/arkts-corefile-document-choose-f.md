# choose

## choose

```TypeScript
declare function choose(types?: string[]): Promise<string>
```

通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。

**起始版本：** 6

**废弃版本：** 9

<!--Device-unnamed-declare function choose(types?: string[]): Promise<string>--><!--Device-unnamed-declare function choose(types?: string[]): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | string[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |


## choose

```TypeScript
declare function choose(callback: AsyncCallback<string>): void
```

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**起始版本：** 6

**废弃版本：** 9

<!--Device-unnamed-declare function choose(callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function choose(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |


## choose

```TypeScript
declare function choose(types: string[], callback: AsyncCallback<string>): void
```

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**起始版本：** 6

**废弃版本：** 9

<!--Device-unnamed-declare function choose(types: string[], callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function choose(types: string[], callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |
