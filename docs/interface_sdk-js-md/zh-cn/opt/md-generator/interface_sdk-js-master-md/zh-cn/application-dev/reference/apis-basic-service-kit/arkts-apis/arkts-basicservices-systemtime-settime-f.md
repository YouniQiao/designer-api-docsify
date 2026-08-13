# setTime

## setTime

```TypeScript
function setTime(time: number, callback: AsyncCallback<void>): void
```

设置系统时间，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md#setTime（系统接口）)

**需要权限：** ohos.permission.SET_TIME

<!--Device-systemTime-function setTime(time: number, callback: AsyncCallback<void>): void--><!--Device-systemTime-function setTime(time: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| time | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| -1 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25
let time = 1611081385000;
try {
  systemTime.setTime(time, (error: BusinessError) => {
    if (error) {
      console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting time`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```


## setTime

```TypeScript
function setTime(time: number): Promise<void>
```

设置系统时间，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md#setTime（系统接口）)

**需要权限：** ohos.permission.SET_TIME

<!--Device-systemTime-function setTime(time: number): Promise<void>--><!--Device-systemTime-function setTime(time: number): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| time | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| -1 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25
let time = 1611081385000;
try {
  systemTime.setTime(time).then(() => {
    console.info(`Succeeded in setting time.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```
