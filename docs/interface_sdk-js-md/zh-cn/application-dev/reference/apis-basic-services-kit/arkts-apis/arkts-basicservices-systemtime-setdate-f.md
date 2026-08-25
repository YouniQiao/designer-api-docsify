# setDate

## 导入模块

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## setDate

```TypeScript
function setDate(date: Date, callback: AsyncCallback<void>): void
```

设置系统日期，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md)

**需要权限：** ohos.permission.SET_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| -1 |


## setDate

```TypeScript
function setDate(date: Date): Promise<void>
```

设置系统日期，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md)

**需要权限：** ohos.permission.SET_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| -1 |
