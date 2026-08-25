# RequestCallback

用于设置模态弹框请求结果的callback接口。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## setRequestResult

```TypeScript
setRequestResult(result: RequestResult): void
```

设置请求结果

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | [RequestResult](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-requestresult-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
