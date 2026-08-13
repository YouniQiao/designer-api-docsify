# setTime（系统接口）

## setTime

```TypeScript
function setTime(time: number, callback: AsyncCallback<void>): void
```

设置系统时间，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TIME

<!--Device-systemDateTime-function setTime(time: long, callback: AsyncCallback<void>): void--><!--Device-systemDateTime-function setTime(time: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| time | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25。
let time: number = 1611081385000;
try {
  systemDateTime.setTime(time, (error: BusinessError) => {
    if (error) {
      console.error(`Failed to set time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in setting time`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to set time. Code: ${error.code}, message: ${error.message}`);
}
```


## setTime

```TypeScript
function setTime(time: number): Promise<void>
```

设置系统时间，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TIME

<!--Device-systemDateTime-function setTime(time: long): Promise<void>--><!--Device-systemDateTime-function setTime(time: long): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25。
let time: number = 1611081385000;
try {
  systemDateTime.setTime(time).then(() => {
    console.info(`Succeeded in setting time.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to set time. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to set time. Code: ${error.code}, message: ${error.message}`);
}
```
