# @ohos.distributedSoftBus.conversation(Cross-Device Wakeup and Message Transfer)

The DSoftBus module **conversation** provides APIs for cross-device interaction of apps, including obtaining the trusted device list, and sending and receiving session data. With this module, your app can obtain trusted devices under the same account, register a listener to receive cross-device data, and send data to a specified device through a session channel. This module is applicable to scenarios that require cross-device collaboration and multi-device data transfer, simplifying the development of cross-device interaction.

> **NOTE：**&gt;
> The APIs provided by this module are system APIs and can be used only in the stage model.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getTrustedDevices(Cross-Device Wakeup and Message Transfer)](arkts-distributedservice-conversation-gettrusteddevices-f-sys.md) |
| [postConversationData(Cross-Device Wakeup and Message Transfer)](arkts-distributedservice-conversation-postconversationdata-f-sys.md) |
| [registerConversationListener(Cross-Device Wakeup and Message Transfer)](arkts-distributedservice-conversation-registerconversationlistener-f-sys.md) |
| [unregisterConversationListener(Cross-Device Wakeup and Message Transfer)](arkts-distributedservice-conversation-unregisterconversationlistener-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceNodeInfo(Cross-Device Wakeup and Message Transfer)](arkts-distributedservice-conversation-devicenodeinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataCallback(Cross-Device Wakeup and Message Transfer)](arkts-distributedservice-conversation-datacallback-t-sys.md) |
<!--DelEnd-->
