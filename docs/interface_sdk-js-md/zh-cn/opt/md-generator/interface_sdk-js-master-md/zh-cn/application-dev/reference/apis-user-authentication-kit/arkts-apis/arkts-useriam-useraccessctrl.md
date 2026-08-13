# @ohos.userIAM.userAccessCtrl

**userAccessCtrl**模块是OpenHarmony用户身份认证体系（UserIAM）的核心组件，专门用于认证令牌的验证和管理。该模块提供了验证认证令牌（AuthToken）的API，能够解析和验证用户身份认证结果，并返回 详细的认证信息。 该模块主要用于以下场景： - 系统级应用需要验证用户身份认证令牌的有效性，确保访问的安全性。 - 需要获取认证令牌的详细信息（如认证类型、信任级别、用户ID等），用于精确识别用户身份。 - 需要基于认证结果进行访问控制决策的场景，实现精细化权限管理。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace userAccessCtrl--><!--Device-unnamed-declare namespace userAccessCtrl-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [verifyAuthToken](arkts-userauthentication-useraccessctrl-verifyauthtoken-f-sys.md#verifyAuthToken（系统接口）) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AuthToken](arkts-userauthentication-useraccessctrl-authtoken-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AuthTokenType](arkts-userauthentication-useraccessctrl-authtokentype-e-sys.md) |
<!--DelEnd-->
