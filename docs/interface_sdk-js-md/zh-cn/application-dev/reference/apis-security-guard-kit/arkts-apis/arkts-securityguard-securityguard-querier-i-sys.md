# Querier（系统接口）

用于接收安全数据的回调函数。

@interface Querier

**起始版本：** 12

<!--Device-securityGuard-interface Querier--><!--Device-securityGuard-interface Querier-End-->

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { securityGuard } from '@kit.SecurityGuardKit';
```

## onComplete

```TypeScript
onComplete: () => void
```

获取数据结束时触发。

**类型：** () =&gt; void

**起始版本：** 12

<!--Device-Querier-onComplete: () => void--><!--Device-Querier-onComplete: () => void-End-->

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

## onError

```TypeScript
onError: (message: string) => void
```

查询存在失败时触发。

**类型：** (message: string) =&gt; void

**起始版本：** 12

<!--Device-Querier-onError: (message: string) => void--><!--Device-Querier-onError: (message: string) => void-End-->

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

## onQuery

```TypeScript
onQuery: (events: Array<SecurityEvent>) => void
```

返回数据时触发。

**类型：** (events: Array&lt;[SecurityEvent](arkts-securityguard-securityguard-securityevent-i-sys.md)&gt;) =&gt; void

**起始版本：** 12

<!--Device-Querier-onQuery: (events: Array<SecurityEvent>) => void--><!--Device-Querier-onQuery: (events: Array<SecurityEvent>) => void-End-->

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

