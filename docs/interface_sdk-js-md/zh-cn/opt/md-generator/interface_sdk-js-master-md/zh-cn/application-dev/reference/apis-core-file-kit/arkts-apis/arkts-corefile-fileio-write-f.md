# write

## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  }
): Promise<number>
```

将数据写入文件，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |


## write

```TypeScript
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

将数据写入文件，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  },
  callback: AsyncCallback<number>
): void
```

将数据写入文件，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer \| string | 是 |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
