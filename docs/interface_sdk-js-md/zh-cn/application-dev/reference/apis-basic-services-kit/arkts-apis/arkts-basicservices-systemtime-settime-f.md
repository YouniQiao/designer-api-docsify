# setTime

## 导入模块

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## setTime

```TypeScript
function setTime(time: number, callback: AsyncCallback<void>): void
```

设置系统时间，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md)

**需要权限：** ohos.permission.SET_TIME

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


## setTime

```TypeScript
function setTime(time: number): Promise<void>
```

设置系统时间，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md)

**需要权限：** ohos.permission.SET_TIME

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
