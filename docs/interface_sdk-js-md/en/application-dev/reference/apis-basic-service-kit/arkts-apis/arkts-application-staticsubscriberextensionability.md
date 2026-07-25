# @ohos.application.StaticSubscriberExtensionAbility

## Modules to Import

```TypeScript
import { StaticSubscriberExtensionAbility } from '@kit.BasicServicesKit';
```

## Summary

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [StaticSubscriberExtensionAbility](arkts-basicservices-application-staticsubscriberextensionability-staticsubscriberextensionability-c-sys.md) | This module provides extension abilities of Basic Services Kit for static subscribers,which can be used to subscribe to common events in static mode. Static subscription enables receiving common events without keeping the app running in the background. This ability is applicable to scenarios where system services or system apps need to perform background processing when specific common events occur.  **StaticSubscriberExtensionAbility** provides the **onReceiveEvent** method and the **context** attribute. The **context** attribute is of the **StaticSubscriberExtensionContext** type, which is the running context of the extension ability. It is inherited from **ExtensionContext** and provides **startAbility** to start other abilities in the same app during event processing.  **APIs used in combination**  The typical process of this module is as follows: Inherit the base class, override **onReceiveEvent**, start a callback, read the event data, and start the target ability. Note that **context.startAbility** can start only the abilities that belong to the same app as the current **StaticSubscriberExtensionAbility**. |
<!--DelEnd-->

