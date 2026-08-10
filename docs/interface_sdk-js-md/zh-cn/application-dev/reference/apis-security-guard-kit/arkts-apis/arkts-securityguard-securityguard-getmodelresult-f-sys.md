# getModelResult（系统接口）

## 导入模块

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## getModelResult

```TypeScript
function getModelResult(rule: ModelRule): Promise<ModelResult>
```

Request security model result from security guard.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.QUERY_SECURITY_MODEL_RESULT

<!--Device-securityGuard-function getModelResult(rule: ModelRule): Promise<ModelResult>--><!--Device-securityGuard-function getModelResult(rule: ModelRule): Promise<ModelResult>-End-->

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | [ModelRule](arkts-securityguard-securityguard-modelrule-i-sys.md) | 是 | indicates the security model rule. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ModelResult&gt; | model Results with Promises. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | check permission fail. |
| 202 | non-system application uses the system API. |

