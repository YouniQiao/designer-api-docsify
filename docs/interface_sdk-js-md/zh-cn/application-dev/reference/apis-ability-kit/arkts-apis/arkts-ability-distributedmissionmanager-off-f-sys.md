# off（系统接口）

## 导入模块

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## off('continueStateChange')

```TypeScript
function off(type: 'continueStateChange', callback?: Callback<ContinueCallbackInfo>): void
```

取消当前任务流转的状态监听。此接口需与on('continueStateChange')成对使用，在不需要监听时应及时调用以释放资源。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'continueStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinueCallbackInfo](arkts-ability-distributedmissionmanager-continuecallbackinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
