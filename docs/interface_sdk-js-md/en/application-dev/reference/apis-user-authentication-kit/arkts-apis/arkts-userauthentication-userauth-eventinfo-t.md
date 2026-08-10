# EventInfo

```TypeScript
type EventInfo = AuthResultInfo | TipInfo
```

表示认证过程中事件信息的类型。

该类型为下表类型取值中的联合类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [userAuth.UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md)

<!--Device-userAuth-type EventInfo = AuthResultInfo | TipInfo--><!--Device-userAuth-type EventInfo = AuthResultInfo | TipInfo-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

| Type | Description |
| --- | --- |
| AuthResultInfo | 获取到的认证结果信息。 |
| TipInfo | 认证过程中的提示信息。 |

