# @ohos.distributedSoftBus.conversation(Cross-Device Wakeup and Message Transfer)

The DSoftBus module **conversation** provides APIs for cross-device interaction of apps, including obtaining the trusted device list, and sending and receiving session data. With this module, your app can obtain trusted devices under the same account, register a listener to receive cross-device data, and send data to a specified device through a session channel. This module is applicable to scenarios that require cross-device collaboration and multi-device data transfer, simplifying the development of cross-device interaction.

> **NOTE：**
> 
> The APIs provided by this module are system APIs and can be used only in the stage model.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace conversation--><!--Device-unnamed-declare namespace conversation-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getTrustedDevices](arkts-distributedservice-conversation-gettrusteddevices-f-sys.md#gettrusteddevices) |
| [postConversationData](arkts-distributedservice-conversation-postconversationdata-f-sys.md#postconversationdata) |
| [registerConversationListener](arkts-distributedservice-conversation-registerconversationlistener-f-sys.md#registerconversationlistener) |
| [unregisterConversationListener](arkts-distributedservice-conversation-unregisterconversationlistener-f-sys.md#unregisterconversationlistener) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceNodeInfo](arkts-distributedservice-conversation-devicenodeinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataCallback](arkts-distributedservice-conversation-datacallback-t-sys.md) |
<!--DelEnd-->
