# getRealActiveTime

## 导入模块

```TypeScript
```

## getRealActiveTime

```TypeScript
function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void
```

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getuptime)

<!--Device-systemTime-function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void--><!--Device-systemTime-function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isNano | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| -1 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```


## getRealActiveTime

```TypeScript
function getRealActiveTime(callback: AsyncCallback<number>): void
```

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getuptime)

<!--Device-systemTime-function getRealActiveTime(callback: AsyncCallback<number>): void--><!--Device-systemTime-function getRealActiveTime(callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| -1 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```


## getRealActiveTime

```TypeScript
function getRealActiveTime(isNano?: boolean): Promise<number>
```

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getuptime)

<!--Device-systemTime-function getRealActiveTime(isNano?: boolean): Promise<number>--><!--Device-systemTime-function getRealActiveTime(isNano?: boolean): Promise<number>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isNano | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| -1 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```
