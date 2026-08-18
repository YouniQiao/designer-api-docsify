# offCaptureStatusChange

## 导入模块

```TypeScript
```

## offCaptureStatusChange

```TypeScript
function offCaptureStatusChange(callback?: Callback<boolean>): void
```

Unregister the callback for device capture, casting, or recording status changes.

**起始版本：** 23

<!--Device-display-function offCaptureStatusChange(callback?: Callback<boolean>): void--><!--Device-display-function offCaptureStatusChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
