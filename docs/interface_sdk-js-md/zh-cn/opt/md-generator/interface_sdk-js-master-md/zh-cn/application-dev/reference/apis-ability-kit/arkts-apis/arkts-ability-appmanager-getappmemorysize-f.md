# getAppMemorySize

## getAppMemorySize

```TypeScript
function getAppMemorySize(): Promise<number>
```

获取当前应用程序可以使用的最大内存（RAM）值。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-appManager-function getAppMemorySize(): Promise<int>--><!--Device-appManager-function getAppMemorySize(): Promise<int>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.getAppMemorySize().then((data) => {
  console.info(`The size of app memory is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`code: ${error.code}, msg:${error.message}`);
});
```


## getAppMemorySize

```TypeScript
function getAppMemorySize(callback: AsyncCallback<number>): void
```

获取当前应用程序可以使用的最大内存（RAM）值。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-appManager-function getAppMemorySize(callback: AsyncCallback<int>): void--><!--Device-appManager-function getAppMemorySize(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';

appManager.getAppMemorySize((err, data) => {
  if (err) {
    console.error(`getAppMemorySize fail, code: ${err.code}, msg:${err.message}`);
  } else {
    console.info(`The size of app memory is: ${JSON.stringify(data)}`);
  }
});
```
