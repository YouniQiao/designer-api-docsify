# isScreenRotationLocked（系统接口）

## isScreenRotationLocked

```TypeScript
function isScreenRotationLocked(callback: AsyncCallback<boolean>): void
```

查询当前自动转屏是否锁定，使用callback异步回调。

**起始版本：** 9

<!--Device-screen-function isScreenRotationLocked(callback: AsyncCallback<boolean>): void--><!--Device-screen-function isScreenRotationLocked(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 查询当前自动转屏是否锁定
screen.isScreenRotationLocked((err: BusinessError, isLocked: boolean) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to get the screen rotation lock status. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting the screen rotation lock status. isLocked: ${isLocked}`);
});
```


## isScreenRotationLocked

```TypeScript
function isScreenRotationLocked(): Promise<boolean>
```

查询当前自动转屏是否锁定，使用Promise异步回调。

**起始版本：** 9

<!--Device-screen-function isScreenRotationLocked(): Promise<boolean>--><!--Device-screen-function isScreenRotationLocked(): Promise<boolean>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 查询当前自动转屏是否锁定
screen.isScreenRotationLocked().then((isLocked: boolean) => {
  console.info(`Succeeded in getting the screen rotation lock status. isLocked: ${isLocked}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get the screen rotation lock status. Code: ${err.code}, message: ${err.message}`);
});
```
