# off

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('userAgeGroupDetected')

```TypeScript
function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void
```

Disables the age group detection function.

> **NOTE：**
> 
> This API is supported only on some phones. Error code **33900003** is returned if it is called on unsupported
> phones.

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**废弃版本：** 24

<!--Device-userStatus-function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void--><!--Device-userStatus-function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'userAgeGroupDetected' | 是 | Event type. The value **userAgeGroupDetected** indicates the event of enabling age group detection. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserClassification&gt; | 否 | Callback used to return the detection result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| 33900001 | Service exception. Possible causes: &lt;br&gt;1. System error, such as a null pointer and container-related exception. &lt;br&gt;2. Node-API invocation exception, such as invalid Node-API status. |
| 33900003 | Unsubscription failed. Possible causes: &lt;br&gt;1. Callback failure. &lt;br&gt;2. Node-API invocation exception, such as invalid Node-API status. &lt;br&gt;3. IPC request exception. |

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

