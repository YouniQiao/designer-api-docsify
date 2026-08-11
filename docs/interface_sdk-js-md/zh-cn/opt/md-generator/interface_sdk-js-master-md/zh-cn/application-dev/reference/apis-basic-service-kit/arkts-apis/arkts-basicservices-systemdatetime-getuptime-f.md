# getUptime

## getUptime

```TypeScript
function getUptime(timeType: TimeType, isNanoseconds?: boolean): number
```

使用同步方式获取自系统启动以来经过的时间。

**起始版本：** 10

<!--Device-systemDateTime-function getUptime(timeType: TimeType, isNanoseconds?: boolean): long--><!--Device-systemDateTime-function getUptime(timeType: TimeType, isNanoseconds?: boolean): long-End-->

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeType | [TimeType](arkts-basicservices-systemdatetime-timetype-e.md) | 是 |
| isNanoseconds | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getUptime(systemDateTime.TimeType.ACTIVE, false);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get uptime. Code: ${error.code}, message: ${error.message}`);
}
```
