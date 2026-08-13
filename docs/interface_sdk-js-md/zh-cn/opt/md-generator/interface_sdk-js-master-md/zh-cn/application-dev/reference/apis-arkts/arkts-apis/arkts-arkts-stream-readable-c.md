# Readable

可从中读取数据的流。可读流用于从源（如文件或网络套接字）读取数据。

**起始版本：** 23

**废弃版本：** -1

<!--Device-stream-class Readable--><!--Device-stream-class Readable-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

创建**Readable**对象的构造函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-constructor()--><!--Device-Readable-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## 示例

```TypeScript
let readableStream = new stream.Readable();
```

## constructor

```TypeScript
constructor(options: ReadableOptions)
```

创建**Readable**对象的构造函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-constructor(options: ReadableOptions)--><!--Device-Readable-constructor(options: ReadableOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ReadableOptions](arkts-arkts-stream-readableoptions-i.md) | 是 |

## 示例

```TypeScript
let option : stream.ReadableOptions = {
  encoding : "utf-8"
};
let readableStream = new stream.Readable(option);
```

## doInitialize

```TypeScript
doInitialize(callback: Function): void
```

需要由开发者实现此API。在可读流首次调用[on](arkts-arkts-stream-writable-c.md#on_string)时调用此API。使用异步回调返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-doInitialize(callback: Function): void--><!--Device-Readable-doInitialize(callback: Function): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Function | 是 |

## 示例

```TypeScript
class MyReadable extends stream.Readable {
  doInitialize(callback: Function) {
    super.doInitialize(callback);
    console.info("Readable doInitialize"); // Readable doInitialize
  }

  doRead(size: number) {
  }
}

let myReadable = new MyReadable();
myReadable.on("data", () => {
});
```

## doRead

```TypeScript
doRead(size: number): void
```

数据读取API，需在子类中实现。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-doRead(size: int): void--><!--Device-Readable-doRead(size: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    console.info("doRead called"); // doRead called
  }
}

let readableStream = new TestReadable();
readableStream.on("data", () => {
});
```

## isPaused

```TypeScript
isPaused(): boolean
```

检查可读流是否已暂停。流在调用[pause()](#pause)后暂停，在调用[resume()](#resume)后从暂停状态恢复。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-isPaused(): boolean--><!--Device-Readable-isPaused(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused false
readableStream.pause();
console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused true
```

## off_string

```TypeScript
off(event: string, callback?: Callback<emitter.EventData>): void
```

移除通过on注册的事件处理函数。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-off(event: string, callback?: Callback<emitter.EventData>): void--><!--Device-Readable-off(event: string, callback?: Callback<emitter.EventData>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' \| 'data' \| 'end' \| 'error' \| 'readable' \| 'pause' \|
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | 否 |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();

function read() {
  console.info("read() called");
}

readableStream.setEncoding("utf8");
readableStream.on("readable", read);
readableStream.off("readable");
readableStream.push("test");
// off注销对readable事件的监听后，read函数不会被调用，"read() called"也不会被打印
```

## off_string

```TypeScript
off(event: string, callback?: Function): void
```

取消事件消息。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-off(event: string, callback?: Function): void--><!--Device-Readable-off(event: string, callback?: Function): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| callback | Function | 否 |

## on_string

```TypeScript
on(event: string, callback: Callback<emitter.EventData>): void
```

注册事件处理函数来监听可读流上的不同事件。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-on(event: string, callback: Callback<emitter.EventData>): void--><!--Device-Readable-on(event: string, callback: Callback<emitter.EventData>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' \| 'data' \| 'end' \| 'error' \| 'readable' \| 'pause' \|
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | 是 |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    throw new Error("Simulated error");
  }
}

let readableStream = new TestReadable();
readableStream.push("test");
readableStream.on("error", () => {
  console.error("error event called"); // error event called
});
```

## on_string

```TypeScript
on(event: string, callback: Function): void
```

注册事件消息。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-on(event: string, callback: Function): void--><!--Device-Readable-on(event: string, callback: Function): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| callback | Function | 是 |

## pause

```TypeScript
pause(): Readable
```

暂停流动模式下的可读流。可以使用**isPaused**检查流是否已暂停。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-pause(): Readable--><!--Device-Readable-pause(): Readable-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.pause();
console.info("Readable test pause", readableStream.isPaused()); // Readable test pause true
```

## pipe

```TypeScript
pipe(destination: Writable, options?: Object): Writable
```

将一个可写流附加到可读流上，以实现数据的自动传输。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-pipe(destination: Writable, options?: Object): Writable--><!--Device-Readable-pipe(destination: Writable, options?: Object): Writable-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| destination | [Writable](arkts-arkts-stream-writable-c.md) | 是 |
| options | Object | 否 |

**返回值：**

| 类型 |
| --- |
| [Writable](arkts-arkts-stream-writable-c.md) |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    this.push("test");
    this.push(null);
  }
}

class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Readable test pipe", chunk); // Readable test pipe test
    callback();
  }
}

let readableStream = new TestReadable();
let writableStream = new TestWritable();
readableStream.pipe(writableStream);
```

## push

```TypeScript
push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean
```

将数据推入可读流的缓冲区。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean--><!--Device-Readable-push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | Uint8Array \| string \| undefined \| null | 是 | 读取的数据。 &lt;br&gt; API version22开始发生兼容性变更，在API version21及之前的版本其类型为：`Uint8Array \| string \|
| encoding | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
let testData = "Hello world";
readableStream.push(testData);
console.info("Readable push test", readableStream.readableLength); // Readable push test 11
```

## read

```TypeScript
read(size?: number): string | null
```

从可读流的缓冲区中读取数据，并返回读取的数据。如果没有读取到数据，则返回**null**。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-read(size?: number): string | null--><!--Device-Readable-read(size?: number): string | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [10200038](../errorcode-utils.md#10200038-doread接口未实现) |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.push("test");
readableStream.pause();
let dataChunk = readableStream.read();
console.info("Readable data is", dataChunk); // Readable data is test
```

## read

```TypeScript
read(size?: number): buffer.Buffer | string | null
```

从缓冲区中读取指定大小的数据。如果可用缓冲区足够，则返回指定大小的结果；否则，如果Readable已结束，则返回所有剩余的缓冲区。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-read(size?: int): buffer.Buffer | string | null--><!--Device-Readable-read(size?: int): buffer.Buffer | string | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 否 |

**返回值：**

| 类型 |
| --- |
| buffer.Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200038](../errorcode-utils.md#10200038-doread接口未实现) |

## resume

```TypeScript
resume(): Readable
```

恢复已显式暂停的可读流。可以使用**isPaused**检查流是否已暂停。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-resume(): Readable--><!--Device-Readable-resume(): Readable-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.resume();
console.info("Readable test resume", !readableStream.isPaused()); // 切换流动模式成功时，此处日志将打印"Readable test resume true"
```

## setEncoding

```TypeScript
setEncoding(encoding?: string): boolean
```

设置可读流的字符编码类型。 当缓冲区有数据时，不允许设置字符编码类型，返回值为**false**。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-setEncoding(encoding?: string): boolean--><!--Device-Readable-setEncoding(encoding?: string): boolean-End-->

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
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
let result = readableStream.setEncoding("utf8");
console.info("Readable result", result); // Readable result true
```

## unpipe

```TypeScript
unpipe(destination?: Writable): Readable
```

将之前附加到可读流的可写流分离。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Readable-unpipe(destination?: Writable): Readable--><!--Device-Readable-unpipe(destination?: Writable): Readable-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| destination | [Writable](arkts-arkts-stream-writable-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## 示例

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    this.push("test");
    this.push(null);
  }
}

class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let readableStream = new TestReadable();
let writableStream = new TestWritable();
readableStream.pipe(writableStream);
readableStream.unpipe(writableStream);
readableStream.on("data", () => {
  console.info("Readable test unpipe data event triggered");
});
// unpipe成功断开连接之后，data事件将不会触发，不会打印"Readable test unpipe data event triggered"
```
