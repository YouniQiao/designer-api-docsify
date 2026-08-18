# offRotationAxesStatusChange（系统接口）

## 导入模块

```TypeScript
```

## offRotationAxesStatusChange

```TypeScript
function offRotationAxesStatusChange(callback?: Callback<RotationAxesStateChangeInfo>): void
```

Unregister a listener for axis state changes.

**起始版本：** 23

<!--Device-mechanicManager-function offRotationAxesStatusChange(callback?: Callback<RotationAxesStateChangeInfo>): void--><!--Device-mechanicManager-function offRotationAxesStatusChange(callback?: Callback<RotationAxesStateChangeInfo>): void-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationAxesStateChangeInfo](arkts-mechanic-mechanicmanager-rotationaxesstatechangeinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
