# Duplex

既可读又可写的流。双工流允许数据双向传输，即可读可写。 **Duplex**类继承自[Readable](arkts-arkts-stream-readableoptions-i.md#ReadableOptions)，支持**Readable**中的所有API。

**继承/实现关系：** Duplex extends [Readable](arkts-arkts-stream-readable-c.md#Readable)

**起始版本：** 23

**废弃版本：** -1

<!--Device-stream-class Duplex--><!--Device-stream-class Duplex-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

创建**Duplex**对象的构造函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-constructor()--><!--Device-Duplex-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## 示例

```TypeScript
let duplex = new stream.Duplex();
```

## cork

```TypeScript
cork(): boolean
```

强制将后续写入的数据缓存起来。调用此API可优化连续写入操作的性能。调用此API后，**writableCorked**的值加1。建议与[uncork()](arkts-arkts-stream-writable-c.md#uncork)配合使用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-cork(): boolean--><!--Device-Duplex-cork(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let duplexStream = new stream.Duplex();
let result = duplexStream.cork();
console.info("duplexStream cork result", result); // duplexStream cork result true
```

## doWrite

```TypeScript
doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void
```

数据写入API。需要由开发者实现此API，但不要直接调用。此API在写入数据时自动调用。使用异步回调返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void--><!--Device-Duplex-doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | string \| Uint8Array | 是 |
| encoding | string | 是 |
| callback | Function | 是 |

## 示例

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("duplexStream chunk is", chunk); // duplexStream chunk is data
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.write("data", "utf8");
```

## doWritev

```TypeScript
doWritev(chunks: string[] | Uint8Array[], callback: Function): void
```

批量数据写入API。需要由开发者实现此API，但不要直接调用。此API在写入数据时自动调用。使用异步回调返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-doWritev(chunks: string[] | Uint8Array[], callback: Function): void--><!--Device-Duplex-doWritev(chunks: string[] | Uint8Array[], callback: Function): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunks | string[] \| Uint8Array[] | 是 |
| callback | Function | 是 |

## 示例

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }

  doWritev(chunks: string[] | Uint8Array[], callback: Function) {
    console.info("duplexStream chunk", chunks[0]); // duplexStream chunk data1
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.cork();
duplexStream.write("data1", "utf8");
duplexStream.write("data2", "utf8");
duplexStream.uncork();
duplexStream.end();
```

## end

```TypeScript
end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable
```

结束双工流的写入过程。如果**writableCorked**的值大于0，则将其置为**0**，并输出缓冲区中的剩余数据。如果传入**chunk**参数，则将其视为最后一个数据块，根据当前执行上下文使用**write**或**doWrite** API写入。如果使用**doWrite**写入，**encoding**参数的有效性检查由**doWrite**决定。如果单独使用**end**（不使用**write**）且传入**chunk**参数，则数据通过**doWrite**写入。使用异步回调返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable--><!--Device-Duplex-end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | string \| Uint8Array | 否 |
| encoding | string | 否 |
| callback | Function | 否 |

**返回值：**

| 类型 |
| --- |
| [Writable](arkts-arkts-stream-writable-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200039](../errorcode-utils.md#10200039-dotransform接口未实现) |

## 示例

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Duplex chunk is", chunk); // Duplex chunk is test
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.end("test", "utf8", () => {
  console.info("Duplex is end"); // Duplex is end
});
```

## setDefaultEncoding

```TypeScript
setDefaultEncoding(encoding?: string): boolean
```

设置双工流的默认字符编码类型，确保在读取数据时正确解析字符。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-setDefaultEncoding(encoding?: string): boolean--><!--Device-Duplex-setDefaultEncoding(encoding?: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let duplexStream = new TestDuplex();
let result = duplexStream.setDefaultEncoding("utf8");
console.info("duplexStream is result", result); // duplexStream is result true
```

## uncork

```TypeScript
uncork(): boolean
```

释放cork状态，刷新缓冲区中的数据并写入目标位置。调用此API后，**writableCorked**的值减1。如果值变为**0**，则流不再处于cork状态；否则，流仍处于cork状态。建议与[cork()](arkts-arkts-stream-writable-c.md#cork)配合使用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-uncork(): boolean--><!--Device-Duplex-uncork(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let dataWritten = "";
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    dataWritten += chunk;
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.cork();
duplexStream.write("a");
duplexStream.write("b");
duplexStream.uncork();
console.info("Duplex test uncork", dataWritten); // Duplex test uncork ab
```

## write

```TypeScript
write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean
```

向流的缓冲区写入数据。使用异步回调返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Duplex-write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean--><!--Device-Duplex-write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | string \| Uint8Array | 否 |
| encoding | string | 否 |
| callback | Function | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200039](../errorcode-utils.md#10200039-dotransform接口未实现) |
| [10200037](../errorcode-utils.md#10200037-多次调用callback) |
| [10200036](../errorcode-utils.md#10200036-流已经结束仍进行写操作) |

## 示例

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("duplexStream chunk is", chunk); // duplexStream chunk is test
    callback();
  }
}

let duplexStream = new TestDuplex();
let result = duplexStream.write("test", "utf8");
console.info("duplexStream result", result); // duplexStream result true
```
