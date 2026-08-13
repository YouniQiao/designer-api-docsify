# write

## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: WriteOptions
): Promise<number>
```

将数据写入文件，使用promise异步回调。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): Promise<number>--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |


## write

```TypeScript
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

将数据写入文件，使用callback异步回调。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |


## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options: WriteOptions,
  callback: AsyncCallback<number>
): void
```

将数据写入文件，使用callback异步回调。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: WriteOptions,  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: WriteOptions,  callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |
