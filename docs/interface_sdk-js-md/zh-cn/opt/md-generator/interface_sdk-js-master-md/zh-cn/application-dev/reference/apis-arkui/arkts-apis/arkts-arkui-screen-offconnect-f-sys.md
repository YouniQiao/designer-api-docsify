# offConnect（系统接口）

## 导入模块

```TypeScript
```

## offConnect

```TypeScript
function offConnect(callback?: Callback<number>): void
```

Unregister the callback for screen connection events.

**起始版本：** 23

<!--Device-screen-function offConnect(callback?: Callback<long>): void--><!--Device-screen-function offConnect(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
