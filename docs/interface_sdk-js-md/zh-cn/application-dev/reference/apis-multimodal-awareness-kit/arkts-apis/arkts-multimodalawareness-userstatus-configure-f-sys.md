# configure（系统接口）

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## configure

```TypeScript
function configure(featureId: UserStatusFeature, detail: string): int
```

Configures feature parameters.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-userStatus-function configure(featureId: UserStatusFeature, detail: string): int--><!--Device-userStatus-function configure(featureId: UserStatusFeature, detail: string): int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| featureId | [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) | 是 | Feature to configure. |
| detail | string | 是 | Detailed feature parameters in JSON format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns 0 if the operation succeeds; otherwise, returns a non-zero value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 33900001 | Service exception. Possible causes: &lt;br&gt;1. System error, such as a null pointer and container-related exception. &lt;br&gt;2. Node-API invocation exception, such as invalid Node-API status. |
| 202 | Permission verification failed. A non-system application calls a system API. |

