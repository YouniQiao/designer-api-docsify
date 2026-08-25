# off

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('userAgeGroupDetected')

```TypeScript
function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void
```

取消订阅年龄群组检测功能。

> **说明：**&gt;
> 该接口仅在部分Phone中支持使用，当Phone设备不支持时返回33900003错误码。

**起始版本：** 20

**废弃版本：** 24

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'userAgeGroupDetected' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UserClassification](arkts-multimodalawareness-userstatus-userclassification-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [33900001](../errorcode-userStatus.md#33900001-服务异常) |
| [33900003](../errorcode-userStatus.md#33900003-取消订阅失败) |
