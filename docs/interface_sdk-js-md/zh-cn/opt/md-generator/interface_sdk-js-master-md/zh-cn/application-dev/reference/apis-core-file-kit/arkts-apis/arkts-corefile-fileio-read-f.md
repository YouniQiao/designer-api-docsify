# read

## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
  }
): Promise<ReadOut>
```

从文件读取数据，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer | 是 |
| options | {     offset?: number;     length?: number;     position?: number;   } | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;ReadOut&gt; |


## read

```TypeScript
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void
```

从文件读取数据，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | 是 |


## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options: {
    offset?: number;
    length?: number;
    position?: number;
  },
  callback: AsyncCallback<ReadOut>
): void
```

从文件读取数据，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer | 是 |
| options | {     offset?: number;     length?: number;     position?: number;   } | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | 是 |
