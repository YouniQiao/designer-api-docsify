# getDate

## 导入模块

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## getDate

```TypeScript
function getDate(callback: AsyncCallback<Date>): void
```

获取当前系统日期，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDate](arkts-basicservices-systemdatetime-getdate-f.md)

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Date&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| -1 |


## getDate

```TypeScript
function getDate(): Promise<Date>
```

获取当前系统日期，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDate](arkts-basicservices-systemdatetime-getdate-f.md)

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 |
| --- |
| Promise & lt;Date & gt; |

**错误码：**

| 错误码ID |
| --- |
| -1 |
