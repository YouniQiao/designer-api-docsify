# getUptime

## 导入模块

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getUptime

```TypeScript
function getUptime(timeType: TimeType, isNanoseconds?: boolean): number
```

使用同步方式获取自系统启动以来经过的时间。

**起始版本：** 10

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
