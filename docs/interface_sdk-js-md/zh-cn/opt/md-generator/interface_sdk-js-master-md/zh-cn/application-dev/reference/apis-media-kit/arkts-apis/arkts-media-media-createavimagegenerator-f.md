# createAVImageGenerator

## createAVImageGenerator

```TypeScript
function createAVImageGenerator(): Promise<AVImageGenerator>
```

创建AVImageGenerator对象。使用Promise异步回调。

**起始版本：** 12

**废弃版本：** -1

<!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator>--><!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator().then((generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error('Failed to create AVImageGenerator');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
});
```


## createAVImageGenerator

```TypeScript
function createAVImageGenerator(): Promise<AVImageGenerator | undefined>
```

Creates an **AVImageGenerator** instance. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator | undefined>--><!--Device-media-function createAVImageGenerator(): Promise<AVImageGenerator | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |


## createAVImageGenerator

```TypeScript
function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void
```

创建AVImageGenerator实例。使用callback异步回调。

**起始版本：** 12

**废弃版本：** -1

<!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void--><!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator((error: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
  }
});
```


## createAVImageGenerator

```TypeScript
function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator | undefined>): void
```

Creates an **AVImageGenerator** instance. This API uses an asynchronous callback to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator | undefined>): void--><!--Device-media-function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVImageGenerator](arkts-media-media-avimagegenerator-i.md) \| undefined & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
