# AuthStatus（系统接口）

```TypeScript
enum AuthStatus
```

表示授权状态枚举。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-enum AuthStatus--><!--Device-abilityToolAccessCtrl-enum AuthStatus-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## AUTHORIZED

```TypeScript
AUTHORIZED = 2
```

已授权。

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatus-AUTHORIZED = 2--><!--Device-AuthStatus-AUTHORIZED = 2-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## FORBIDDEN

```TypeScript
FORBIDDEN = 1
```

禁止授权。

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatus-FORBIDDEN = 1--><!--Device-AuthStatus-FORBIDDEN = 1-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## REMOTE_RESTRICTED

```TypeScript
REMOTE_RESTRICTED = 4
```

远程首先，不允许在远程授权场景下授予权限。

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatus-REMOTE_RESTRICTED = 4--><!--Device-AuthStatus-REMOTE_RESTRICTED = 4-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## REQUIRE_AUTH

```TypeScript
REQUIRE_AUTH = 0
```

需要授权。

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatus-REQUIRE_AUTH = 0--><!--Device-AuthStatus-REQUIRE_AUTH = 0-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## RESTRICTED

```TypeScript
RESTRICTED = 3
```

受系统或策略限制，当前授权被拒绝。

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatus-RESTRICTED = 3--><!--Device-AuthStatus-RESTRICTED = 3-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
