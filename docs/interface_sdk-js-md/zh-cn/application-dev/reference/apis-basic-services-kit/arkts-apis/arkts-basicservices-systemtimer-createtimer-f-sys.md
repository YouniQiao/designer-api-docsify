# createTimer（系统接口）

## 导入模块

```TypeScript
import { systemTimer } from 'kits/@kit.BasicServicesKit';
```

## createTimer

```TypeScript
function createTimer(options: TimerOptions, callback: AsyncCallback<number>): void
```

创建定时器，使用callback异步回调。

> **注意：**&gt;
> 需与[systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md)结合使用，否则会造
> 成内存泄漏

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## createTimer

```TypeScript
function createTimer(options: TimerOptions): Promise<number>
```

创建定时器，使用Promise异步回调返回定时器的ID。

> **注意：**&gt;
> 需与[systemTimer.destroyTimer](arkts-basicservices-systemtimer-destroytimer-f-sys.md)结合使用，否则会造
> 成内存泄漏

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TimerOptions](arkts-basicservices-systemtimer-timeroptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
