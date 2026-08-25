# getRealTime

## 导入模块

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getRealTime

```TypeScript
function getRealTime(isNano: boolean, callback: AsyncCallback<number>): void
```

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md)

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isNano | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getRealTime

```TypeScript
function getRealTime(callback: AsyncCallback<number>): void
```

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md)

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getRealTime

```TypeScript
function getRealTime(isNano?: boolean): Promise<number>
```

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md)

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
