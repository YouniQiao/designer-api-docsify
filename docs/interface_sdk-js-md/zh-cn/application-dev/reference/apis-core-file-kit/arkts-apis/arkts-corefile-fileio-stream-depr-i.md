# Stream

文件流，在调用Stream的方法前，需要先通过createStream()方法（同步或异步）来构建一个Stream实例。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [Stream](arkts-corefile-file-fs-stream-i.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## close

```TypeScript
close(): Promise<void>
```

关闭文件流，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [close](arkts-corefile-file-fs-stream-i.md#close)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

异步关闭文件流，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [close](arkts-corefile-file-fs-stream-i.md#close)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## closeSync

```TypeScript
closeSync(): void
```

同步关闭文件流。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [closeSync](arkts-corefile-file-fs-stream-i.md#closesync)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## flush

```TypeScript
flush(): Promise<void>
```

刷新文件流，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [flush](arkts-corefile-file-fs-stream-i.md#flush)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

异步刷新文件流，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [flush](arkts-corefile-file-fs-stream-i.md#flush)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## flushSync

```TypeScript
flushSync(): void
```

同步刷新文件流。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [flushSync](arkts-corefile-file-fs-stream-i.md#flushsync)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options?: {
      position?: number;
      offset?: number;
      length?: number;
    }
  ): Promise<ReadOut>
```

从流文件读取数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [read](arkts-corefile-file-fs-stream-i.md#read)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | {       position?: number;       offset?: number;       length?: number;     } | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReadOut](arkts-corefile-fileio-readout-depr-i.md)&gt; |

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void
```

read.

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [read](arkts-corefile-file-fs-stream-i.md#read)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReadOut](arkts-corefile-fileio-readout-depr-i.md)&gt; | 是 |

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options: {
      position?: number;
      offset?: number;
      length?: number;
    },
    callback: AsyncCallback<ReadOut>
  ): void
```

从流文件读取数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [read](arkts-corefile-file-fs-stream-i.md#read)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | {       position?: number;       offset?: number;       length?: number;     } | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReadOut](arkts-corefile-fileio-readout-depr-i.md)&gt; | 是 |

## readSync

```TypeScript
readSync(
    buffer: ArrayBuffer,
    options?: {
      position?: number;
      offset?: number;
      length?: number;
    }
  ): number
```

以同步方法从流文件读取数据。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readSync](arkts-corefile-file-fs-stream-i.md#readsync)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | {       position?: number;       offset?: number;       length?: number;     } | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options?: {
      offset?: number;
      length?: number;
      position?: number;
      encoding?: string;
    }
  ): Promise<number>
```

将数据写入流文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [write](arkts-corefile-file-fs-stream-i.md#write)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | {       offset?: number;       length?: number;       position?: number;       encoding?: string;     } | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [write](arkts-corefile-file-fs-stream-i.md#write)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## write

```TypeScript
write(
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

将数据写入流文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [write](arkts-corefile-file-fs-stream-i.md#write)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | {       offset?: number;       length?: number;       position?: number;       encoding?: string;     } | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## writeSync

```TypeScript
writeSync(
    buffer: ArrayBuffer | string,
    options?: {
      offset?: number;
      length?: number;
      position?: number;
      encoding?: string;
    }
  ): number
```

以同步方法将数据写入流文件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeSync](arkts-corefile-file-fs-stream-i.md#writesync)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | {       offset?: number;       length?: number;       position?: number;       encoding?: string;     } | 否 |

**返回值：**

| 类型 |
| --- |
| number |
