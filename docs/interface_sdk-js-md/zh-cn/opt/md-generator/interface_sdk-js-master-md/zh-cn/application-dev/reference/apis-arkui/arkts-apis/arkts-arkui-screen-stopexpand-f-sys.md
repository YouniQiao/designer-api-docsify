# stopExpand（系统接口）

## stopExpand

```TypeScript
function stopExpand(expandScreen:Array<number>, callback: AsyncCallback<void>): void
```

停止屏幕的扩展模式，使用callback异步回调。

**起始版本：** 10

**废弃版本：** 20

<!--Device-screen-function stopExpand(expandScreen:Array<long>, callback: AsyncCallback<void>): void--><!--Device-screen-function stopExpand(expandScreen:Array<long>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| expandScreen | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let expandScreenIds: Array<number> = [1, 2, 3]; // 扩展屏幕ID集合
// 停止屏幕的扩展模式
screen.stopExpand(expandScreenIds, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to stop expand screens. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in stopping expand screens.');
});
```


## stopExpand

```TypeScript
function stopExpand(expandScreen:Array<number>): Promise<void>
```

停止屏幕的扩展模式，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 20

<!--Device-screen-function stopExpand(expandScreen:Array<long>): Promise<void>--><!--Device-screen-function stopExpand(expandScreen:Array<long>): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| expandScreen | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let expandScreenIds: Array<number> = [1, 2, 3]; // 扩展屏幕ID集合
// 停止屏幕的扩展模式
screen.stopExpand(expandScreenIds).then(() => {
  console.info('Succeeded in stopping expand screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to stop expand screens. Code: ${err.code}, message: ${err.message}`);
});
```
