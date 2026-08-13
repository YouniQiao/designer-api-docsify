# ReadStream

文件可读流，需要先通过fileIo.createReadStream方法来构建一个ReadStream实例。ReadStream继承自数据流基类stream.Readable。 ReadStream读到的数据为解码后的字符串，其编码格式当前仅支持'utf-8'。

**继承/实现关系：** ReadStream extends [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md#Readable)

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare class ReadStream--><!--Device-unnamed-declare class ReadStream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## close

```TypeScript
close(): void
```

关闭可读流。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ReadStream-close(): void--><!--Device-ReadStream-close(): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

## 示例

```TypeScript
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
rs.close();
```

## constructor

```TypeScript
constructor()
```

构造一个文件可读流.

**起始版本：** 12

**废弃版本：** -1

<!--Device-ReadStream-constructor()--><!--Device-ReadStream-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: number, whence?: WhenceType): number
```

调整可读流偏移指针位置。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ReadStream-seek(offset: number, whence?: WhenceType): number--><!--Device-ReadStream-seek(offset: number, whence?: WhenceType): number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900026 |
| 13900042 |

## 示例

```TypeScript
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
const curOff = rs.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`Succeeded in seeking, current offset is ${curOff}`);
rs.close();
```

## bytesRead

```TypeScript
readonly bytesRead: number
```

可读流已经读取的字节数。

**类型：** number

**起始版本：** 12

**废弃版本：** -1

<!--Device-ReadStream-readonly bytesRead: number--><!--Device-ReadStream-readonly bytesRead: number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

当前可读流对应的文件路径。

**类型：** string

**起始版本：** 12

**废弃版本：** -1

<!--Device-ReadStream-readonly path: string--><!--Device-ReadStream-readonly path: string-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO
