# @ohos.web.webNativeMessagingExtensionManager

webNativeMessagingExtensionManager模块是ArkWeb提供的Web原生消息扩展管理模块，用于在应用侧（调用方）发起并管理到 [WebNativeMessagingExtensionAbility](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md)的连接。开发者可通过 [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md)方法指定目标扩展Ability并建立连接，通过返回的连接ID与 [WebExtensionConnectionCallback](arkts-arkweb-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md)监听连接建立、断开及失败 事件，也可通过[disconnectNative](arkts-arkweb-webnativemessagingextensionmanager-disconnectnative-f.md)主动释放连接。该模块适用于浏览器扩展与应用通信的场景；使用前需申请 ohos.permission.WEB_NATIVE_MESSAGING 权限，且仅在Stage模型下可用。

> **说明：**&gt;
> 本模块接口仅可在Stage模型下使用。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
```

## 汇总

### 函数

| 名称 |
| --- |
| [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md) |
| [disconnectNative](arkts-arkweb-webnativemessagingextensionmanager-disconnectnative-f.md) |

### 接口

| 名称 |
| --- |
| [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) |
| [WebExtensionConnectionCallback](arkts-arkweb-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md) |

### 枚举

| 名称 |
| --- |
| [NmErrorCode](arkts-arkweb-webnativemessagingextensionmanager-nmerrorcode-e.md) |
