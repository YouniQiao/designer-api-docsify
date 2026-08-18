# @ohos.userIAM.companionDeviceAuth

**companionDeviceAuth**模块是OpenHarmony用户身份认证体系（UserIAM）的重要组成部分，专门用于伴随设备认证管理。该模块为系统应用提供伴随设备查询、订阅和服务范围管理等能力。 设计逻辑：伴随设备认证采用主设备（Host）与伴随设备（Companion）协作的模式。主设备通过绑定流程将另一台设备添加为伴随设备，绑定过程中双端完成密钥协商并分发初始认证令牌。认证模式包括令牌认证和委托认证：令牌认证基于主设备签发 至伴随设备的令牌计算消息认证码（MAC）完成身份校验；委托认证由主设备委托伴随设备执行本地认证并返回结果。主设备签发的令牌携带认证可信等级（authTrustLevel），令牌生命周期包括签发、超时、吊销及关联设备离线等阶段。伴随设备 的认证状态由令牌生命周期与认证保持状态（如佩戴状态、连接状态等）共同决定。应用通过状态监听器订阅模板状态、可用设备变化和持续认证状态，系统通过回调主动通知变化。 该模块主要用于以下场景： - 管理伴随设备与主设备之间的认证关系。 - 查询和订阅伴随设备的状态变化。 - 管理伴随设备支持的业务范围。 - 实现持续认证功能。 - 处理设备选择和注册。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace companionDeviceAuth--><!--Device-unnamed-declare namespace companionDeviceAuth-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getStatusMonitor](arkts-userauthentication-companiondeviceauth-getstatusmonitor-f-sys.md#getstatusmonitor系统接口) |
| [registerDeviceSelectCallback](arkts-userauthentication-companiondeviceauth-registerdeviceselectcallback-f-sys.md#registerdeviceselectcallback系统接口) |
| [registerPasscodePromptCallback](arkts-userauthentication-companiondeviceauth-registerpasscodepromptcallback-f-sys.md#registerpasscodepromptcallback系统接口) |
| [unregisterDeviceSelectCallback](arkts-userauthentication-companiondeviceauth-unregisterdeviceselectcallback-f-sys.md#unregisterdeviceselectcallback系统接口) |
| [unregisterPasscodePromptCallback](arkts-userauthentication-companiondeviceauth-unregisterpasscodepromptcallback-f-sys.md#unregisterpasscodepromptcallback系统接口) |
| [updateEnabledBusinessIds](arkts-userauthentication-companiondeviceauth-updateenabledbusinessids-f-sys.md#updateenabledbusinessids系统接口) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ContinuousAuthParam](arkts-userauthentication-companiondeviceauth-continuousauthparam-i-sys.md) |
| [DeviceKey](arkts-userauthentication-companiondeviceauth-devicekey-i-sys.md) |
| [DeviceSelectResult](arkts-userauthentication-companiondeviceauth-deviceselectresult-i-sys.md) |
| [DeviceStatus](arkts-userauthentication-companiondeviceauth-devicestatus-i-sys.md) |
| [PasscodePromptParams](arkts-userauthentication-companiondeviceauth-passcodepromptparams-i-sys.md) |
| [StatusMonitor](arkts-userauthentication-companiondeviceauth-statusmonitor-i-sys.md) |
| [TemplateStatus](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [BusinessId](arkts-userauthentication-companiondeviceauth-businessid-e-sys.md) |
| [DeviceIdType](arkts-userauthentication-companiondeviceauth-deviceidtype-e-sys.md) |
| [SelectPurpose](arkts-userauthentication-companiondeviceauth-selectpurpose-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AvailableDeviceStatusCallback](arkts-userauthentication-companiondeviceauth-availabledevicestatuscallback-t-sys.md) |
| [ContinuousAuthStatusCallback](arkts-userauthentication-companiondeviceauth-continuousauthstatuscallback-t-sys.md) |
| [DeviceSelectCallback](arkts-userauthentication-companiondeviceauth-deviceselectcallback-t-sys.md) |
| [PasscodePromptCallback](arkts-userauthentication-companiondeviceauth-passcodepromptcallback-t-sys.md) |
| [PasscodeSubmitCallback](arkts-userauthentication-companiondeviceauth-passcodesubmitcallback-t-sys.md) |
| [TemplateStatusCallback](arkts-userauthentication-companiondeviceauth-templatestatuscallback-t-sys.md) |
<!--DelEnd-->
