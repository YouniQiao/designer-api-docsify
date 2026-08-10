# Writable

可写入数据的流。可写流允许将数据写入到目标中，这个目标可以是文件、HTTP响应、标准输出、另一个流等。可写流采用缓冲区机制：数据通过write()写入缓冲区，缓冲区数据通过doWrite()自动写出到目标，开发者需实现doWrite以定义数据写出的具体行为。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-stream-class Writable--><!--Device-stream-class Writable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { stream } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

**Writable**的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-constructor()--><!--Device-Writable-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
let writableStream = new stream.Writable();
```

## cork

```TypeScript
cork(): boolean
```

强制将后续写入的数据缓存起来。调用此API可优化连续写入操作的性能。调用此API后，**writableCorked**的值加1。建议与[uncork()](arkts-arkts-stream-writable-c.md#uncork)配合使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-cork(): boolean--><!--Device-Writable-cork(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 操作结果。**true**表示成功；**false**表示失败。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
let result = writableStream.cork();
console.info("Writable cork result", result); // Writable cork result true
```

## doInitialize

```TypeScript
doInitialize(callback: Function): void
```

需要由开发者实现此API，但不要直接调用。此API在可写流初始化期间自动调用。使用异步回调返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-doInitialize(callback: Function): void--><!--Device-Writable-doInitialize(callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Function | Yes | 回调函数。 |

## Examples

```TypeScript
class MyWritable extends stream.Writable {
  doInitialize(callback: Function) {
    super.doInitialize(callback);
    console.info("Writable doInitialize"); // Writable doInitialize
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    super.doWrite(chunk, encoding, callback);
  }
}

new MyWritable();
```

## doWrite

```TypeScript
doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void
```

数据写入API。需要由开发者实现此API，但不要直接调用。此API在写入数据时自动调用。使用异步回调返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void--><!--Device-Writable-doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chunk | string \| Uint8Array | Yes | 待写入的数据。 |
| encoding | string | Yes | 编码格式。目前支持**'utf8'**、**'gb18030'**、**'gbk'**和**'gb2312'**。 |
| callback | Function | Yes | 回调函数。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Writable chunk is", chunk); // Writable chunk is data
    callback();
  }
}

let writableStream = new TestWritable();
writableStream.write('data', 'utf8');
```

## doWritev

```TypeScript
doWritev(chunks: string[] | Uint8Array[], callback: Function): void
```

批量数据写入API。需要由开发者实现此API，但不要直接调用。此API在写入数据时自动调用。使用异步回调返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-doWritev(chunks: string[] | Uint8Array[], callback: Function): void--><!--Device-Writable-doWritev(chunks: string[] | Uint8Array[], callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chunks | string[] \| Uint8Array[] | Yes | 批量写入的数据数组。 |
| callback | Function | Yes | 回调函数。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWritev(chunks: string[] | Uint8Array[], callback: Function) {
    console.info("Writable chunk", chunks);
    callback();
  }
  // Writable chunk data1
  // Writable chunk data2
}

let writableStream = new TestWritable();
writableStream.write('data1', 'utf8');
writableStream.write('data2', 'utf8');
writableStream.uncork();
writableStream.end();
```

## end

```TypeScript
end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable
```

结束可写流的写入过程。如果**writableCorked**的值大于0，则将其置为**0**，并输出缓冲区中的剩余数据。如果传入**chunk**参数，则将其视为最后一个数据块，根据当前执行上下文使用**write**或**doWrite** API写入。如果使用**doWrite**写入，**encoding**参数的有效性检查由**doWrite**决定。如果单独使用**end**（不使用**write**）且传入**chunk**参数，则数据通过**doWrite**写入。使用异步回调返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable--><!--Device-Writable-end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chunk | string \| Uint8Array | No | 待写入的数据。默认值为**undefined**。 |
| encoding | string | No | 编码格式。默认值为**'utf8'**。目前支持**'utf8'**、**'gb18030'**、**'gbk'**和**'gb2312'**。 |
| callback | Function | No | 用于返回结果的回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Writable](arkts-arkts-stream-writable-c.md) | 当前**Writable**对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200035 | The doWrite method has not been implemented. |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Writable chunk is", chunk);
    callback();
  }
  // Writable chunk is test
  // Writable chunk is finish
}

let writableStream = new TestWritable();
writableStream.write('test', 'utf8');
writableStream.end('finish', 'utf8', () => {
  console.info("Writable is end"); // Writable is end
});
```

## off

```TypeScript
off(event: string, callback?: Callback<emitter.EventData>): void
```

移除通过on注册的事件处理函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-off(event: string, callback?: Callback<emitter.EventData>): void--><!--Device-Writable-off(event: string, callback?: Callback<emitter.EventData>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 事件回调类型，支持的事件包括：'close' \| 'drain' \| 'error' \| 'finish'。 - 'close'：完成end()调用，结束写入操作，触发该事件。 - 'drain'：在可写流缓冲区中数据清空时触发该事件。 - 'error'：在可写流发生异常时触发该事件。 - 'finish'：在数据缓冲区全部写入到目标后触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | No | 指定事件的要注销的回调函数。不传入时注销指定事件的所有回调函数。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
 }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
let testListenerCalled = false;
let testListener = () => {
  testListenerCalled = true;
};
writableStream.on('finish', testListener);
writableStream.off('finish');
writableStream.write('test');
writableStream.end();
setTimeout(() => {
  console.info("Writable off test", testListenerCalled.toString()); // Writable off test false
}, 0);
```

## off

```TypeScript
off(event: string, callback?: Function): void
```

取消事件消息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Writable-off(event: string, callback?: Function): void--><!--Device-Writable-off(event: string, callback?: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 注册的事件。 |
| callback | Function | No | 事件回调。 |

## on

```TypeScript
on(event: string, callback: Callback<emitter.EventData>): void
```

注册事件处理函数来监听可写流上的不同事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-on(event: string, callback: Callback<emitter.EventData>): void--><!--Device-Writable-on(event: string, callback: Callback<emitter.EventData>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 事件回调类型，支持的事件包括：'close' \| 'drain' \| 'error' \| 'finish'。 - 'close'：完成end()调用，结束写入操作，触发该事件。 - 'drain'：在可写流缓冲区中数据清空时触发该事件。 - 'error'：在可写流发生异常时触发该事件。 - 'finish'：在数据缓冲区全部写入到目标后触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | Yes | 回调函数，返回事件传输的数据。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback(new Error());
  }
}

let callbackCalled = false;
let writable = new TestWritable();
writable.on('error', () => {
  console.info("Writable event test", callbackCalled.toString()); // Writable event test false
});
writable.write('hello', 'utf8', () => {
});
```

## on

```TypeScript
on(event: string, callback: Function): void
```

注册事件消息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Writable-on(event: string, callback: Function): void--><!--Device-Writable-on(event: string, callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 注册的事件。 |
| callback | Function | Yes | 事件回调。 |

## setDefaultEncoding

```TypeScript
setDefaultEncoding(encoding?: string): boolean
```

设置可写流的默认编码格式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-setDefaultEncoding(encoding?: string): boolean--><!--Device-Writable-setDefaultEncoding(encoding?: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | 默认编码格式。默认值为**'utf8'**。目前支持**'utf8'**、**'gb18030'**、**'gbk'**和**'gb2312'**。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 操作结果。**true**表示成功；**false**表示失败。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
let result = writableStream.setDefaultEncoding('utf8');
console.info("Writable is result", result); // Writable is result true
```

## uncork

```TypeScript
uncork(): boolean
```

释放cork状态，刷新缓冲区中的数据并写入目标位置。调用此API后，**writableCorked**的值减1。如果值变为**0**，则流不再处于cork状态；否则，流仍处于cork状态。建议与[cork()](arkts-arkts-stream-writable-c.md#cork)配合使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-uncork(): boolean--><!--Device-Writable-uncork(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 操作结果。**true**表示成功；**false**表示失败。 |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let writableStream = new TestWritable();
writableStream.cork();
writableStream.write('data1', 'utf8');
writableStream.write('data2', 'utf8');
writableStream.uncork();
writableStream.end();
writableStream.on('finish', () => {
  console.info("all Data is End"); // all Data is End
});
```

## write

```TypeScript
write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean
```

将数据写入流的缓冲区中。数据写入缓冲区后，当缓冲区数据被消耗时，会自动调用doWrite()将数据写出。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean--><!--Device-Writable-write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chunk | string \| Uint8Array | No | 需要写入的数据。默认值为undefined。当前版本不支持传入null、undefined和空字符串，会抛出异常。 |
| encoding | string | No | 字符编码类型。默认值是**'utf8'**，当前版本支持**'utf8'**、**'gb18030'**、**'gbk'**以及**'gb2312'**。 |
| callback | Function | No | 回调函数，用于在数据写入完成后执行特定逻辑。传入callback时，数据写入缓冲区后会调用该回调函数；不传入时，不调用回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 可写流的缓冲区中是否还有空间。**true**表示缓冲区还有空间，**false**表示流的内部缓冲区数据量已达到设定水位线，不建议继续写入以避免内存溢出。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200035 | The doWrite method has not been implemented. |
| 10200037 | The callback is invoked multiple times consecutively. |
| 10200036 | The stream has been ended. |

## Examples

```TypeScript
class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Writable chunk is", chunk); // Writable chunk is test
    callback();
  }
}

let writableStream = new TestWritable();
writableStream.write('test', 'utf8');
```

## writable

```TypeScript
get writable(): boolean
```

如果调用writable.write()是安全的，返回true，即表示流未被销毁、未出错或未结束。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writable(): boolean--><!--Device-Writable-get writable(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## writableCorked

```TypeScript
get writableCorked(): int
```

为完全释放流，需要调用writable.uncork()的次数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writableCorked(): int--><!--Device-Writable-get writableCorked(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## writableEnded

```TypeScript
get writableEnded(): boolean
```

是否已调用Writable.end。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writableEnded(): boolean--><!--Device-Writable-get writableEnded(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## writableFinished

```TypeScript
get writableFinished(): boolean
```

是否已调用Writable.end并刷新了所有缓冲区。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writableFinished(): boolean--><!--Device-Writable-get writableFinished(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## writableHighWatermark

```TypeScript
get writableHighWatermark(): int
```

highWatermark的值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writableHighWatermark(): int--><!--Device-Writable-get writableHighWatermark(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## writableLength

```TypeScript
get writableLength(): int
```

可刷新的数据大小，单位为字节或对象。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writableLength(): int--><!--Device-Writable-get writableLength(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## writableObjectMode

```TypeScript
get writableObjectMode(): boolean
```

返回布尔值，表示是否处于ObjectMode。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Writable-get writableObjectMode(): boolean--><!--Device-Writable-get writableObjectMode(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

