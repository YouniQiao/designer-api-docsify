# destroyTimer（系统接口）

## destroyTimer

```TypeScript
function destroyTimer(timer: number, callback: AsyncCallback<void>): void
```

销毁定时器，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-systemTimer-function destroyTimer(timer: long, callback: AsyncCallback<void>): void--><!--Device-systemTimer-function destroyTimer(timer: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timer | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat:false
};
let triggerTime: number = new Date().getTime();
triggerTime += 3000;

try {
  systemTimer.createTimer(options).then((timerId: number) => {
    systemTimer.startTimer(timerId, triggerTime);
    systemTimer.stopTimer(timerId);
    systemTimer.destroyTimer(timerId, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to destroy timer. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info(`Succeeded in destroying timer.`);
    });
    console.info(`Succeeded in creating timer. timerId: ${timerId}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to operate timer. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to destroy timer. Code: ${error.code}, message: ${error.message}`);
}
```


## destroyTimer

```TypeScript
function destroyTimer(timer: number): Promise<void>
```

销毁定时器，使用Promise进行异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-systemTimer-function destroyTimer(timer: long): Promise<void>--><!--Device-systemTimer-function destroyTimer(timer: long): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timer | number | 是 |

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

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat:false
};
let triggerTime: number = new Date().getTime();
triggerTime += 3000;

try {
  systemTimer.createTimer(options).then((timerId: number) => {
    systemTimer.startTimer(timerId, triggerTime);
    systemTimer.stopTimer(timerId);
    systemTimer.destroyTimer(timerId).then(() => {
      console.info(`Succeeded in destroying timer.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to destroy timer. Code: ${error.code}, message: ${error.message}`);
    });
    console.info(`Succeeded in creating timer. timerId: ${timerId}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to operate timer. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to destroy timer. Code: ${error.code}, message: ${error.message}`);
}
```
