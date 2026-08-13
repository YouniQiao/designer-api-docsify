# setScreenRotationLocked（系统接口）

## setScreenRotationLocked

```TypeScript
function setScreenRotationLocked(isLocked:boolean, callback: AsyncCallback<void>): void
```

设置自动转屏开关是否锁定，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-screen-function setScreenRotationLocked(isLocked:boolean, callback: AsyncCallback<void>): void--><!--Device-screen-function setScreenRotationLocked(isLocked:boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isLocked | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let isLocked: boolean = false;
// 设置自动转屏开关为未锁定
screen.setScreenRotationLocked(isLocked, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to unlock auto rotate. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in unlocking auto rotate.');
});
```


## setScreenRotationLocked

```TypeScript
function setScreenRotationLocked(isLocked:boolean): Promise<void>
```

设置自动转屏开关是否锁定，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-screen-function setScreenRotationLocked(isLocked:boolean): Promise<void>--><!--Device-screen-function setScreenRotationLocked(isLocked:boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isLocked | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let isLocked: boolean = false;
// 设置自动转屏开关为未锁定
screen.setScreenRotationLocked(isLocked).then(() => {
  console.info('Succeeded in unlocking auto rotate');
}).catch((err: BusinessError) => {
  console.error(`Failed to unlock auto rotate. Code: ${err.code}, message: ${err.message}`);
});
```
