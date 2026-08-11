# off

## off('userAgeGroupDetected')

```TypeScript
function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void
```

取消订阅年龄群组检测功能。

> **说明：**
> 
> 该接口仅在部分Phone中支持使用，当Phone设备不支持时返回33900003错误码。

**起始版本：** 20

**废弃版本：** 24

<!--Device-userStatus-function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void--><!--Device-userStatus-function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'userAgeGroupDetected' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserClassification&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-服务异常) |
| [33900003](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900003-取消订阅失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    userStatus.off('userAgeGroupDetected');
    console.info("off succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed off and err code is " + error.code);
}
```
