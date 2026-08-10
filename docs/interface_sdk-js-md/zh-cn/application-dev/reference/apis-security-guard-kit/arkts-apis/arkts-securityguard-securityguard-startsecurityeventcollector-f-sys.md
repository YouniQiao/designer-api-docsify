# startSecurityEventCollector（系统接口）

## 导入模块

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## startSecurityEventCollector

```TypeScript
function startSecurityEventCollector(rule: CollectorRule): void
```

start the collector to collect data

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.QUERY_SECURITY_EVENT

<!--Device-securityGuard-function startSecurityEventCollector(rule: CollectorRule): void--><!--Device-securityGuard-function startSecurityEventCollector(rule: CollectorRule): void-End-->

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | [CollectorRule](arkts-securityguard-securityguard-collectorrule-i-sys.md) | 是 | rule of collect security event information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | check permission fail. |
| 202 | non-system application uses the system API. |

