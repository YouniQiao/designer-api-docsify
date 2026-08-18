# readText

## 导入模块

```TypeScript
```

## readText

```TypeScript
declare function readText(
  filePath: string,
  options?: ReadTextOptions
): Promise<string>
```

基于文本方式读取文件（即直接读取文件的文本内容），使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function readText(  filePath: string,  options?: ReadTextOptions): Promise<string>--><!--Device-unnamed-declare function readText(  filePath: string,  options?: ReadTextOptions): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |


## readText

```TypeScript
declare function readText(filePath: string, callback: AsyncCallback<string>): void
```

基于文本方式读取文件内容，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function readText(filePath: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(filePath: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |


## readText

```TypeScript
declare function readText(
  filePath: string,
  options: ReadTextOptions,
  callback: AsyncCallback<string>
): void
```

基于文本方式读取文件内容，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function readText(  filePath: string,  options: ReadTextOptions,  callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function readText(  filePath: string,  options: ReadTextOptions,  callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900019 |
| 13900024 |
| 13900025 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900041 |
| 13900010 |
| 13900042 |
