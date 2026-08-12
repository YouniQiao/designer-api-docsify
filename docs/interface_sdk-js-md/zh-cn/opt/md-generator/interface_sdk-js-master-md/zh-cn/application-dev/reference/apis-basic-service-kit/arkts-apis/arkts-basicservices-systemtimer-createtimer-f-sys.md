# createTimer（系统接口）

## createTimer

```TypeScript
function createTimer(options: TimerOptions, callback: AsyncCallback<number>): void
```

创建定时器，使用callback异步回调。

> **注意：**
> 
> 需与[systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroyTimer)结合使用，否则会造
> 成内存泄漏

**起始版本：** 7

<!--Device-systemTimer-function createTimer(options: TimerOptions, callback: AsyncCallback<long>): void--><!--Device-systemTimer-function createTimer(options: TimerOptions, callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat: false
};
try {
  systemTimer.createTimer(options, (error: BusinessError, timerId: number) => {
    if (error) {
      console.error(`Failed to create timer. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in creating timer. timerId: ${timerId}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to create timer. Code: ${error.code}, message: ${error.message}`);
}
```


## createTimer

```TypeScript
function createTimer(options: TimerOptions): Promise<number>
```

创建定时器，使用Promise异步回调返回定时器的ID。

> **注意：**
> 
> 需与[systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md#destroyTimer)结合使用，否则会造
> 成内存泄漏

**起始版本：** 7

<!--Device-systemTimer-function createTimer(options: TimerOptions): Promise<long>--><!--Device-systemTimer-function createTimer(options: TimerOptions): Promise<long>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: systemTimer.TimerOptions = {
  type: systemTimer.TIMER_TYPE_REALTIME,
  repeat:false
};
try {
  systemTimer.createTimer(options).then((timerId: number) => {
    console.info(`Succeeded in creating timer. timerId: ${timerId}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to create timer. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to create timer. Code: ${error.code}, message: ${error.message}`);
}
```
