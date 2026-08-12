# getRealActiveTime

## getRealActiveTime

```TypeScript
function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void
```

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime)

<!--Device-systemDateTime-function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void--><!--Device-systemDateTime-function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isNano | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
}
```


## getRealActiveTime

```TypeScript
function getRealActiveTime(callback: AsyncCallback<number>): void
```

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime)

<!--Device-systemDateTime-function getRealActiveTime(callback: AsyncCallback<number>): void--><!--Device-systemDateTime-function getRealActiveTime(callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
}
```


## getRealActiveTime

```TypeScript
function getRealActiveTime(isNano?: boolean): Promise<number>
```

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime)

<!--Device-systemDateTime-function getRealActiveTime(isNano?: boolean): Promise<number>--><!--Device-systemDateTime-function getRealActiveTime(isNano?: boolean): Promise<number>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
}
```
