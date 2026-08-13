# @ohos.web.webNativeMessagingExtensionManager

webNativeMessagingExtensionManager模块是ArkWeb提供的Web原生消息扩展管理模块，用于在应用侧（调用方）发起并管理到 [WebNativeMessagingExtensionAbility](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md#WebNativeMessagingExtensionAbility)的连接。开发者可通过 [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md#connectNative)方法指定目标扩展Ability并建立连接，通过返回的连接ID与 [WebExtensionConnectionCallback](arkts-arkweb-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md#WebExtensionConnectionCallback)监听连接建立、断开及失败 事件，也可通过[disconnectNative](arkts-arkweb-webnativemessagingextensionmanager-disconnectnative-f.md#disconnectNative)主动释放连接。该模块适用于浏览器扩展与应用通信的场景；使用前需申请 ohos.permission.WEB_NATIVE_MESSAGING 权限，且仅在Stage模型下可用。 > **说明：**> > 本模块接口仅可在Stage模型下使用。

**起始版本：** 21

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace webNativeMessagingExtensionManager--><!--Device-unnamed-declare namespace webNativeMessagingExtensionManager-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 汇总

### 函数

| 名称 |
| --- |
| [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md#connectNative) |
| [disconnectNative](arkts-arkweb-webnativemessagingextensionmanager-disconnectnative-f.md#disconnectNative) |

### 接口

| 名称 |
| --- |
| [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) |
| [WebExtensionConnectionCallback](arkts-arkweb-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md) |

### 枚举

| 名称 |
| --- |
| [NmErrorCode](arkts-arkweb-webnativemessagingextensionmanager-nmerrorcode-e.md) |
