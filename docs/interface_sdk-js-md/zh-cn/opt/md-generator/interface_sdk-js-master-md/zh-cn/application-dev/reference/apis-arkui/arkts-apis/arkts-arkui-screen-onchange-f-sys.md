# onChange（系统接口）

## onChange

```TypeScript
function onChange(callback: Callback<number>): void
```

Register the callback for screen change.

**起始版本：** 23

**废弃版本：** -1

<!--Device-screen-function onChange(callback: Callback<long>): void--><!--Device-screen-function onChange(callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
